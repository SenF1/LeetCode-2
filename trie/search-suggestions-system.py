class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        suggestions = []
        currentWord = ""
        products.sort()
        for letter in searchWord:
            currentWord += letter
            currSuggestions = []
            currIdx = 0
            while len(currSuggestions) < 3 and currIdx < len(products):
                if len(products[currIdx]) >= len(currentWord) and products[currIdx][:len(currentWord)] == currentWord:
                    currSuggestions.append(products[currIdx])
                currIdx += 1
            suggestions.append(currSuggestions)
        return suggestions
        
        