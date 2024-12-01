from semantic_router import Route
from semantic_router.encoders import FastEmbedEncoder
from semantic_router.layer import RouteLayer

politics = Route(
    name="politics",
    utterances=[
        "isn't politics the best thing ever",  # 정치가 최고의 것이 아니냐
        "why don't you tell me about your political opinions",  # 너의 정치적 의견에 대해 말해줘
        "don't you just love the president",  # 대통령을 좋아하지 않니
        "they're going to destroy this country!",  # 그들은 이 나라를 파괴할 것이다!
        "they will save the country!",  # 그들은 나라를 구할 것이다!
    ]
)

chitchat = Route(
    name="chitchat",
    utterances=[
        "how are you",  # 어떻게 지내니
        "what's up",  # 뭐해
        "how's the weather",  # 날씨 어때
        "what's your favorite color",  # 네가 좋아하는 색은 뭐야
        "let's go to the chippy",  # 수다 떨러 가자
    ]
)

routes = [politics, chitchat]

encoder = FastEmbedEncoder(name='sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2')

rl = RouteLayer(encoder=encoder, routes=routes)
