def compare_strings(str1, str2):
    """
    比较两个字符串，并返回它们的相似度和差异。
    """
    if str1 == str2:
        return "字符串完全相同"
    else:
        differences = []
        len1, len2 = len(str1), len(str2)
        min_len = min(len1, len2)

        for i in range(min_len):
            if str1[i] != str2[i]:
                differences.append(f"位置 {i}: '{str1[i]}' != '{str2[i]}'")
        
        if len1 != len2:
            differences.append(f"字符串长度不同: {len1} != {len2}")
        
        return "字符串不同:\n" + "\n".join(differences)

# 示例输入
string1 = "hello"
string2 = "h3llo"

# 比较字符串
result = compare_strings(string1, string2)
print(result)
