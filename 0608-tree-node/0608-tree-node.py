import pandas as pd

def tree_node(tree: pd.DataFrame) -> pd.DataFrame:
    # 부모 노드의 아이디를 리스트에 추가
    parents = [x for x in tree.p_id.to_list() if type(x) == int]
    
    def category_func(row):
        if str(row["p_id"]) == "<NA>":
            return "Root"
        elif row["id"] in parents:
            return "Inner"
        else:
            return "Leaf"

    tree["type"] = tree.apply(category_func, axis = 1)
    return tree[["id","type"]]