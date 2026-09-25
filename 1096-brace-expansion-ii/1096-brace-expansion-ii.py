class Solution(object):
    def braceExpansionII(self, expression):
        """
        :type expression: str
        :rtype: List[str]
        """
        def dfs(exp):
            ans = set()
            groups = [[]]
            layer, left = 0, 0
            for i, ch in enumerate(exp):
                if ch == '{':
                    layer += 1
                    if layer == 1:
                        left = i + 1
                elif ch == '}':
                    layer -= 1
                    if layer == 0:
                        merge(groups, dfs(exp[left:i]))
                elif ch == ',' and layer == 0:
                    groups.append([])
                elif layer == 0:
                    merge(groups, [ch])

            for group in groups:
                for word in group:
                    ans.add(word)
            return sorted(ans)
        def merge(groups, group):
            if not groups[-1]:
                groups[-1] = group
                return
            groups[-1] = [w1 + w2 for w1 in groups[-1] for w2 in group]
        return dfs(expression)
