'''
DECRYPTION PROGRAM
------------------
An encryption program was used to generate the following secret code. The encryption program converted each character 
of the string into its ASCII decimal number, applied a +/-20 algorithm to it and then converted it back to
characters. Your task is to write a Decryption program to decipher the following secret code. Don't waste time changing 
your program 40 times. Use a FOR loop from -20 to +20 to generate all the possibilities in one run of your program.

Secret Message: Lxwp{j}~uj}rxw|*)bx~)l{jltnm)}qn)lxmn7)]qn)ox{ln)r|)\][XWP)r}q)x~*
'''

secret_message = 'Lxwp{j}~uj}rxw|*)bx~)l{jltnm)}qn)lxmn7)]qn)ox{ln)r|)\][XWP)r}q)x~*'
decrypted_text = ''

for i in range(40):
    decrypted_text = ''
    for c in secret_message:
        x = ord(c)
        x += -20 + i
        c2 = chr(x)
        decrypted_text += c2
    print('\n' + decrypted_text)

# # Code is 'Congratulations! You cracked the code. The force is STRONG with you!'
