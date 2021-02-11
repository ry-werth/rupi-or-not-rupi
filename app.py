import flask
import random
import pickle

app = flask.Flask(__name__)


@app.route('/')
def main():

    poem_data = generate_poem()

    return flask.render_template('main.html', poem=poem_data["poem"], is_rupi=poem_data["is_rupi"])

@app.route('/api/new-poem', methods=["POST"])
def grabNewPoem():
    poem_data = generate_poem()
    print("here")
    return(poem_data)


def generate_poem():
    pickle_off = open("corpus.pkl","rb")
    corpus = pickle.load(pickle_off)

    pickle_off_fake = open("fake-corpus.pkl","rb")
    fake_corpus = pickle.load(pickle_off_fake)

    poem = ""
    is_rupi = True

    rand = random.uniform(0, 1)
    if rand > 0.5:
        is_rupi = False
        poem = random.choice(fake_corpus)
    else:
        poem = random.choice(corpus)

    data = {"poem":poem, "is_rupi": is_rupi}

    return(data)

if __name__ == '__main__':
    app.run()
