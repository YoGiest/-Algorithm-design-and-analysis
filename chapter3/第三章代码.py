#第三章代码

#读入文件
def read_file(filename)：
    try:
        fp=open(filename)
        L=fp.readlines()
    except IOError:
        print("Error opening or reading input file:",filename)
        ays.exit()
    return L

#得到文档的单词
def get_words_from_line_list(L):
    word_list=[]
    for line in L:
        words_in_line=get_words_from_string(line)
    return word_list

#计算文件中每一个单词出现的频率
def count_frequency(word_list):
    L=[]
    for new_word in word_list:
        for entry in L:
            if new_word==entry[0]:
                entry[1]=entry[1]+1
                break
        else:
            L.append([new_word,1])
    return L


    #计算两向量内积
    def inner_product(L1,L2):
        sum==0.0
        for word1,count1 in L1:
            for word2,count2 in L2:
                if word1==word2:
                    sum+=count1*count2
        return sum

    #计算两向量夹角
    def vector_angle(L1,L2):
        numerator=inner_product(L1,L2)
        denomination=math.sort(inner_product(L1,L2)*inner_product(L1,L2))
        return math.acos(numerator/denomination)

    #文档比较主函数
    def main():
        filename_1="t1.verne.txt"
        filename_2="t1.varne.txt"
        sorted_word_list_1=word_frequencies_for_file(filename_1)
        sorted_word_list_2=word_fruquencies_for_file(filename_2)
        distance=vector_angle(sorted_word_list_1,sorted_word_list_2)
        print("The distance bewteen the document is:%0.6f (radians)"%distance)

    If __name__=="__main__":
        import cProfile
        cProfile.run("main()")

        #对向量内的元素进行排序预处理
        def word_frequencies_for_file(filename):
            line_list=read_file(filename)
            word_list=get_words_from_line_list(line_list)
            freq_mapping=count_frequency(word_list)
            sorted_freq_mapping=sorted(freq_mapping)
        print('File',filename,":",)
        print(len(line_list),"lines,",)
        print(len(word_list),"words,",)
        print(len(sorted_freq_mapping),"distinct words")

        #内积计算优化
        def inner_product(L1,L2):
            sum=0.0
            i=0
            j=0
            while i<len(L1) and len(L2):
                if L1[i][0]==L2[j][0]:
                    sum+=L[i][1]*L2[j][1]
                    i+=1
                    j+=1
                elif L1[i][0]<L2[j][0]:
                    i+=1
                else:
                    j+=1
            return sum

        #利用字典数据结构计算每一个单词出现的频次
        def count_frequency(word_list):
            D={}
            for new_word in word_list:
                if D.has_key(new_word):
                    D[new_word]=D[new_word]+1
                else:
                    D[new_word]=1
            return D.items()

        #将文件分解成单词序列
        def wordss(text):
            return re.findall('[a-z]+',text.lower())

        #计算单词出现次数
        def train(features):
            model=collection.defaultdict(lambda:1)
            for f in features:
                model[f]+=1
            return model

        #单词是否存在
        def known(words):
            wordintxt=set([])
            for w in words:
                if w in NWORDS:
                    wordintxt.add(w)
            return wordintxt

        #单词纠正主程序
        def correct(word):
            candidates=known([word] or known(edist(word)) or known_edist2(word) or [word]
            return max(candidate,key=lambda w:NWORDS[w])
