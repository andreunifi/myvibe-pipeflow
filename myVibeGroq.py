from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.pydantic_v1 import BaseModel, Field
from langchain_groq import ChatGroq
from typing import Optional
import json
api_key = "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" 
model = ChatGroq(temperature=0, groq_api_key=api_key, model_name="llama3-8b-8192")

class Event(BaseModel):
    name: str = Field(description="Name of the event")
    location: str = Field(description="Location of the event")
    datetime: Optional[str] = Field(description="Datetime of the event")
    description: Optional[str] = Field(description="Description of the event")
    price: Optional[float] = Field(description="Price of the event")
    capiency: Optional[int] = Field(description="Capacity of the event")

event_query = """
Milan is buzzing with a plethora of events this year, each promising to bring excitement, culture, and joy to locals and visitors alike. Let’s dive into the heart of Milan and explore some of the most anticipated happenings.

First up, we have the Milan Fashion Week. This grand spectacle, held from September 15th to 21st, 2024, transforms Milan into the epicenter of the fashion world. Designers from all corners of the globe flock to showcase their latest creations. Venues across the city become runways, with the most innovative and chic designs gracing the catwalks. Whether you’re a fashion aficionado or just looking to catch a glimpse of the glitz and glamour, this week is not to be missed. The whole city buzzes with energy, from high-profile after-parties to exclusive designer meet-and-greets.

Following closely is the Leonardo da Vinci Exhibition at the Museo Nazionale della Scienza e della Tecnologia Leonardo da Vinci. Running from July 1st to October 31st, 2024, this exhibition offers a deep dive into the genius of Leonardo. Marvel at his intricate sketches, engineering marvels, and timeless artworks. This is more than just an exhibition; it’s an immersive experience that transports you back to the Renaissance, showcasing the brilliance of one of history’s greatest minds. Perfect for art lovers, history buffs, and curious minds of all ages.

In April, from the 10th to the 16th, the city celebrates creativity during Milan Design Week. This event is a testament to Milan’s innovative spirit. Spread across various locations, you’ll find cutting-edge designs, thought-provoking installations, and engaging workshops. It’s a playground for designers and a feast for the eyes for anyone who appreciates the art of design. From furniture to digital innovations, Milan Design Week is a melting pot of creativity that leaves a lasting impression on all who attend.

Music lovers, mark your calendars for December 7th, 2024. The La Scala Opera Season Opening is an event that promises to be a cultural highlight. Held at the historic Teatro alla Scala, this opening night is a celebration of opera at its finest. Expect world-class performances, a glittering audience, and an atmosphere steeped in tradition. It’s a night where the who’s who of the opera world come together to celebrate the timeless art form in one of the most prestigious opera houses.

For foodies, the Milan Food Festival from June 5th to 8th, 2024, is a culinary paradise. This festival brings together the best of Milan’s gastronomy. Think of it as a four-day feast where you can indulge in local delicacies, watch live cooking demonstrations, and participate in interactive workshops. Whether you’re a fan of traditional Milanese cuisine or eager to try modern culinary innovations, this festival caters to all tastes. It’s a delightful journey through the rich food culture of Milan.
"""
def classify_and_describe_events(event_query):
    parser = JsonOutputParser(pydantic_object=Event)
    prompt = PromptTemplate(
        template="Classify and describe events.\n{format_instructions}\n{query}\n",
        input_variables=["query"],
        partial_variables={"format_instructions": parser.get_format_instructions()},
    )
    chain = prompt | model | parser
    output = chain.invoke({"query": event_query})

    json_output = json.dumps(output, indent=4)
    return json_output

# Example usage
result = classify_and_describe_events(event_query)
print(result)

