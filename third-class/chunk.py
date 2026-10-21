from langchain_text_splitters import RecursiveCharacterTextSplitter

your_long_document = """
Once upon a time, in a land far, far away, there lived a wise old owl who had seen many things in his long life. The owl was known throughout the forest for his knowledge and his ability to solve problems that no one else could. Animals from all over the land would come to the owl seeking advice, and he would always listen carefully before offering his guidance.
One day, a young rabbit approached the owl with a dilemma. The rabbit had lost his way in the forest and was afraid he would never find his home again. The owl listened patiently to the rabbit's story and then offered a solution. He told the rabbit to follow the sound of the river, which would lead him back to his burrow safely.
The rabbit thanked the owl and followed his advice. Sure enough, he soon heard the gentle babbling of the river and was able to find his way back home. The rabbit was grateful to the wise old owl and promised to always remember his guidance.
The owl continued to help many other animals in the forest, and his reputation as a wise and kind creature grew even stronger. He taught the animals valuable lessons about friendship, courage, and perseverance, and they all looked up to him as a mentor and a friend.
As time went on, the owl's wisdom became known far and wide, and even humans would come to the forest to seek his counsel. The owl's legacy lived on for generations, and his teachings continued to inspire and guide those who sought his wisdom. The forest thrived under the owl's guidance, and the animals lived in harmony, always remembering the lessons they had learned from their wise old friend.
The owl's story became a legend, passed down from one generation to the next."""

splitter = RecursiveCharacterTextSplitter(
    chunk_size=80,        # aim for ~800 chars per chunk
    chunk_overlap=10,     # adjacent chunks share 100 chars (context glue)
)

chunks = splitter.split_text(your_long_document)
print(chunks[0])          # → first chunk of text
print(len(chunks))    # → e.g. 47 chunks ready to embed
