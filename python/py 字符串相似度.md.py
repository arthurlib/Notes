# [官方文档]{https://docs.python.org/zh-cn/3/library/difflib.html}
import difflib


def string_similar(s1, s2):
    return difflib.SequenceMatcher(None, s1, s2).quick_ratio()


print(string_similar('python比较字符串相似度', 'python比较字符串相似度'))
print(string_similar('python比较字符串相似度', '1python比较字符串相似度'))

print(string_similar('python比较字符串相似度', 'python比较字符串相似度3'))


# 最主要的是，python原生的模块的效率都比较好。
# 其中None的位置是一个函数，用来去掉自己不想算在内的元素。比如我想把空格排除在外：
a = ''
b = ''
seq = difflib.SequenceMatcher(lambda x: x == " ", a, b)
ratio = seq.ratio()
