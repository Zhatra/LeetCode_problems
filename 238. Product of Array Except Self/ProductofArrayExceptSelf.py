# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         res = [1]*len(nums)

#         prefix=1
#         for i in range(len(nums)):
#             res[i] = prefix
#             prefix *= nums[i]
#         postfix=1
#         for i in range(len(nums) - 1,-1,-1):
#             res[i] *= postfix
#             postfix *= nums[i]
#         return res

from typing import List

class Solution:
    
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        list_length = len(nums)
        
        # Inicializar listas para almacenar productos acumulativos
        left_products = [1] * list_length
        right_products = [1] * list_length
        final_products = [1] * list_length
        
        # Calcular productos acumulativos desde la izquierda
        left_accumulator = 1
        for i in range(list_length):
            left_products[i] = left_accumulator
            left_accumulator *= nums[i]
        
        # Calcular productos acumulativos desde la derecha
        right_accumulator = 1
        for i in reversed(range(list_length)):
            right_products[i] = right_accumulator
            right_accumulator *= nums[i]
        
        # Combinar productos acumulativos izquierdos y derechos
        for i in range(list_length):
            final_products[i] = left_products[i] * right_products[i]
        
        return final_products
#pruebas
if __name__ == "__main__":
    sol = Solution()
    result = sol.productExceptSelf([1, 2, 3, 4])
    print(result)  # Debería imprimir [24, 12, 8, 6]