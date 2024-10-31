## 0x04. UTF-8 Validation

For this project, I needed to apply my knowledge in bitwise operations, understanding of the UTF-8 encoding scheme, and Python programming skills to validate whether a given dataset represents a valid UTF-8 encoding.

### Solution 

1. **Iterate Through Input Data**
   - The function iterates through each byte in the input list.

2. **Determine Number of Subsequent Bytes**
   - The first byte indicates how many bytes follow:
     - **1-byte character**: Byte starts with `0`.
     - **2-byte character**: Byte starts with `110`.
     - **3-byte character**: Byte starts with `1110`.
     - **4-byte character**: Byte starts with `11110`.

3. **Bit Manipulation**
   - The function uses bit manipulation to check the binary representation of each byte:
     - It examines the leading bits using the right shift operator (`>>`).

4. **Validate Continuation Bytes**
   - If additional bytes are expected, they must start with `10`.
   - If any byte does not follow this format, the function returns `False`.

5. **Ensure All Bytes Are Accounted For**
   - The function checks that all expected bytes are accounted for by ensuring `num_bytes` is 0 after processing.
