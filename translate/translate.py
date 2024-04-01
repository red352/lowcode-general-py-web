from googletrans import Translator

translator = Translator()



def translate(**params):
    res = translator.translate(**params)
    return {key: getattr(res, key) for key in res.__dict__ if not key.startswith("_")}
