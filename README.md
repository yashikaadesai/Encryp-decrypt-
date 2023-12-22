------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
INTRODUCTION:

This project, aptly named "dumbcrypt," is a playful yet insightful endeavor into the world of cryptography. 
This project amalgamates two distinct cryptographic techniques - the Affine Cipher and the Caesar Cipher - to craft an
innovative encryption and decryption system. While the Affine Cipher encrypts letters and numbers, the Caesar Cipher takes 
charge of encrypting punctuation. Users can input a string, comprising of alphanumeric characters and punctuation, 
which undergoes a unique encryption process.

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

WHAT ARE AFFINE CIPHERS AND CEASER CIPHERS?

Affine Cipher:

The Affine Cipher is a bit more intricate. Imagine you have a secret equation for each letter. You use this equation to transform each letter 
into another letter. This equation involves two secret numbers: one decides how you change the letter, and the other decides where you start counting from.
The magic here is that this transformation has a specific method, ensuring that even if someone intercepts the coded message, it's hard for them to decipher
without knowing those secret numbers. In the project, the Affine Cipher handles the encryption and decryption of letters and numbers in the message.

Caesar Cipher:

Think of a Caesar Cipher as a secret shift code. Imagine you have a secret message, and you shift each letter in the message by a fixed number of positions
in the alphabet. For example, if you shift by 3, 'A' becomes 'D', 'B' becomes 'E', and so on. This shifting is what the Caesar Cipher does. In the project, 
Caesar Cipher is used mainly for encrypting and decrypting punctuation marks in a message by shifting them.

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
So, when you look at the project's code, you'll see functions for shifting characters (Caesar Cipher) and more complex functions that use a formula with
two numbers to change characters (Affine Cipher). By combining these methods, the project creates a unique "dumbcrypt" that adds layers of secrecy to a message!

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Attached is a sample output screenshot below:


<img width="490" alt="Screenshot 2023-12-21 at 8 09 13 PM" src="https://github.com/yashikaadesai/Encryp-decrypt-/assets/143465326/6ca77920-52d1-4b6a-b26b-1e4a6491462c">
