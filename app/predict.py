import joblib

class predict():
    def __init__(self, model, input):
        self.model = model
        self.input = input

    def __remove_html_markup(s):
        tag = False
        quote = False
        out = ""

        for c in s:
                if c == '<' and not quote:
                    tag = True
                elif c == '>' and not quote:
                    tag = False
                elif (c == '"' or c == "'") and tag:
                    quote = not quote
                elif not tag:
                    out = out + c

        return out

    def clean_data(self, input):
        to_clean = ['name', 'description', 'org_name', 'org_desc']
        for column in to_clean:
            self.input.column = self.input.column.map(lambda x: __remove_html_markup(x))


    def predict(self, input):
        result = self.model.predict(self.input)
        self.input['fraud'] = result
        return self.input

if __name__ == '__main__':
    input = <'path_to_input'>
    models = [<'path_to_models'>]
    predict.predict(input, models)