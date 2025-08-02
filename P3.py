import os

def tokenize(expr):
    tokens = []
    i = 0
    n = len(expr)
    while i < n:
        if expr[i] == '\\':
            if i + 1 < n:
                tokens.append(expr[i:i+2])
                i += 2
            else:
                tokens.append(expr[i])
                i += 1
        else:
            tokens.append(expr[i])
            i += 1
    return tokens

def is_operand(token):
    if len(token) == 2 and token.startswith('\\'):
        return True
    if len(token) == 1:
        if token not in ['*', '+', '?', '|', '(', ')', '.']:
            return True
    return False

def insert_concatenation(tokens):
    if not tokens:
        return []
    new_tokens = []
    n = len(tokens)
    for i in range(n - 1):
        t1 = tokens[i]
        t2 = tokens[i+1]
        new_tokens.append(t1)
        cond1 = is_operand(t1) or t1 in ['*', '+', '?'] or t1 == ')'
        cond2 = is_operand(t2) or t2 == '('
        if cond1 and cond2:
            new_tokens.append('.')
    new_tokens.append(tokens[-1])
    return new_tokens

OPERATORS = {
    '*': (3, 'right'),
    '+': (3, 'right'),
    '?': (3, 'right'),
    '.': (2, 'left'),
    '|': (1, 'left')
}

def shunting_yard(tokens):
    output = []
    stack = []
    steps = []

    steps.append(("Inicio", output[:], stack[:]))

    for token in tokens:
        if token == '(':
            stack.append(token)
            steps.append((f"Token '{token}': push '(' a pila", output[:], stack[:]))
        elif token == ')':
            popped = False
            while stack and stack[-1] != '(':
                op = stack.pop()
                output.append(op)
                steps.append((f"Token '{token}': pop '{op}' a salida", output[:], stack[:]))
                popped = True
            if stack and stack[-1] == '(':
                stack.pop()
                steps.append((f"Token '{token}': pop '(' de pila", output[:], stack[:]))
            elif not popped:
                steps.append((f"Token '{token}': no se encontro '('", output[:], stack[:]))
        elif token in OPERATORS:
            prec_token, assoc_token = OPERATORS[token]
            while stack and stack[-1] != '(':
                top = stack[-1]
                if top not in OPERATORS:
                    break
                prec_top, assoc_top = OPERATORS[top]
                if (prec_top > prec_token) or (prec_top == prec_token and assoc_token == 'left'):
                    op = stack.pop()
                    output.append(op)
                    steps.append((f"Token '{token}': pop '{op}' a salida", output[:], stack[:]))
                else:
                    break
            stack.append(token)
            steps.append((f"Token '{token}': push a pila", output[:], stack[:]))
        else:
            output.append(token)
            steps.append((f"Token '{token}': push a salida", output[:], stack[:]))
    
    while stack:
        if stack[-1] == '(':
            steps.append(("Error: '(' sin cerrar", output[:], stack[:]))
            stack.pop()
        else:
            op = stack.pop()
            output.append(op)
            steps.append((f"Fin: pop '{op}' a salida", output[:], stack[:]))
    
    return output, steps

def main():
    input_file = "expresiones.txt"
    
    if not os.path.exists(input_file):
        print(f"XXX Error: El archivo '{input_file}' no existe en la carpeta actual.")
        print("SOS Asegurate de que el archivo este en la misma carpeta que este script.")
        return

    try:
        with open(input_file, 'r') as f:
            lines = [line.strip() for line in f.readlines() if line.strip()]
    except Exception as e:
        print(f"XXX Error al leer el archivo: {e}")
        return

    for expr in lines:
        print("\n" + "="*50)
        print(f"<> Procesando Expresion: '{expr}'")
        print("="*50)
        
        tokens = tokenize(expr)
        print("\n> 1. Tokenizacion:")
        print(f"   ➡ Tokens: {tokens}")
        
        tokens_concatenated = insert_concatenation(tokens)
        print("\n> 2. Insercion de concatenacion:")
        print(f"   ➡ Tokens con concatenacion: {tokens_concatenated}")
        
        postfix, steps = shunting_yard(tokens_concatenated)
        print("\n> 3. Postfix:")
        print(f"   ➡ Notacion Postfix: {' '.join(postfix)}")
        
        print("\n> 4. Pasos del Algoritmo Shunting-Yard:")
        for i, (desc, out, stk) in enumerate(steps):
            print(f"   #Paso {i+1}: {desc}")
            print(f"      ➡ Salida: {out}")
            print(f"      ➡ Pila: {stk}")

        # Preguntar si continuar
        while True:
            user_input = input("\n¿Continuar con la siguiente expresion? (s/n): ").strip().lower()
            if user_input == 's':
                break
            elif user_input == 'n':
                print("\n Ejecucion terminada por el usuario.")
                return
            else:
                print("XXX Entrada no valida. Ingresa 's' para continuar o 'n' para terminar.")

if __name__ == "__main__":
    main()