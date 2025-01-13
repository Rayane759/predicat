class CacheManager:

    """
    classe simple qui permet, de stocker des résultats
    """
    def __init__(self):
        self.cache = {}

    def get_in_cache_else_return(self,function_call, function_name, argument):
        """
        Appelle une fonction si son nom et l'argument précisé n'a pas déjà été utilisé
        Sinon va chercher dans le dictionnaire Cache la valeur stockée lors d'un précédent appel de fonction
        """
        cache_key=f"{function_name}-{argument}"
        if cache_key in self.cache:
            return self.cache[cache_key]
        else:
            self.cache[cache_key] = function_call
        return self.cache[cache_key]