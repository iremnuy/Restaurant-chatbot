import gzip
import shutil
import fasttext
import fasttext.util




#ft = fasttext.load_model('cc.en.300.bin.gz')
#ft.get_dimension()


def prep_embedding_model():
    ft_path = 'fastText/cc.en.300.bin.gz'
    with gzip.open(ft_path, 'rb') as f_in:
        with open('fastText/cc.en.300.bin', 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)


if __name__ == '__main__':
    prep_embedding_model()
