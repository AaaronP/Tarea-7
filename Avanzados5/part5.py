def Arbol(preorder, inorder):
    if not preorder or not inorder:
        return []

    raiz = preorder[0]
    raizIndex = inorder.index(raiz)

    linorder = inorder[:raizIndex]
    rinorder = inorder[raizIndex + 1 :]

    lpreorder = [i for i in preorder if i in linorder]
    rpreorder = [i for i in preorder if i in rinorder]

    root = [raiz, Arbol(lpreorder, linorder), Arbol(rpreorder, rinorder)]

    return root
