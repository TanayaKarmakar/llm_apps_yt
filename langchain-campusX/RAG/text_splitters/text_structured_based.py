from langchain.text_splitter import RecursiveCharacterTextSplitter


text = """
Yes, space exploration has driven significant technological advancements that have benefited society on Earth. Challenges like surviving in the harsh environment of space have forced innovation in areas like health, medicine, transportation, and more. These advancements are often referred to as "spin-offs" or "technology transfer," where technologies initially developed for space exploration find practical applications in everyday life.
Here are some examples of how space exploration has led to technological advancements:
Medical advancements:
Space-related research has led to advancements in areas like heart monitors, implantable devices, and even light-based cancer treatments.
Materials science:
Technologies for creating lightweight, high-temperature alloys for spacecraft have led to innovations in consumer products like scratch-resistant eyeglass lenses.
"""

splitter = RecursiveCharacterTextSplitter(
    chunk_size=300,
    chunk_overlap=0
)

chunks = splitter.split_text(text)

print(len(chunks))