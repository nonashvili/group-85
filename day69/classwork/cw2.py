def longest(a1, a2):
    new = a1 + a2
    empty= ""
    for i in new:
        if i not in empty:
            empty+=i
    return "".join(sorted(empty))
        



  #      def longest(a1, a2):
   # return "".join(sorted(set(a1 + a2)))