import string

class TextProcessor():

    def get_clean_string(self, text):
        res = text
        for symbol in text:
            a = self.__is_punctuation(symbol)
            if a == 'True':
                res = res.replace(symbol, '')
        return res

    def __is_punctuation(self, symbol):
        self._res = 'False'
        if symbol in string.punctuation:
            self._res = 'True'
        return self._res


class TextLoader():

    def set_clean_text(self, out_string, n):
        __text_processor = TextProcessor()
        __clean_string = __text_processor.get_clean_string(out_string)
        print(f'clean_string {n}:')
        return __clean_string


class DataInterface():

    def process_texts(self, out_list):
        n = 1
        for i in out_list:
            _atr = TextLoader()
            res = _atr.set_clean_text(i, n)
            n += 1
            print(res)


# my list of strings before
my_list = ['a1.', 'b2!!', 'c3.&^%$#@']
print('List of strings before:', my_list)

# launching the process
c = DataInterface()
c.process_texts(my_list)



