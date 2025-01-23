from datetime import date
from django.shortcuts import render

# Create your views here.

all_post = [
    {
        "slug" : "The_Art_of_Mindfulness",
        "date" : date(2025, 1, 20),
        "image" : "01.webp",
        "author" : "Emily Harper",
        "title" : "The Art of Mindfulness: Finding Peace in Chaos",
        "content" : """Mindfulness has become a buzzword in recent years, but its roots lie in ancient practices that emphasize being present in the moment. 
        By focusing on your breath, the sensations in your body, and your immediate surroundings, you can find clarity even in the most chaotic environments. 
        Incorporating mindfulness into your daily routine can reduce stress, improve concentration, and enhance your overall well-being. 
        Start small—try a five-minute mindful breathing exercise today and experience the difference it can make."""
    },
    {
        "slug" : "How_to_Stay_Motivated_in_Your_Fitness_Journey",
        "date" : date(2025, 1, 15),
        "image" : "02.webp",
        "author" : "Alex Johnson",
        "title" : "How to Stay Motivated in Your Fitness Journey",
        "content" : """Starting a fitness journey is easy, but staying motivated is where the challenge lies. 
        To keep the momentum, set realistic goals, track your progress, and celebrate small victories. 
        Surround yourself with a supportive community that shares your goals and passions. 
        Remember, fitness is a lifelong commitment to your health, not a short-term project. 
        By focusing on the joy of movement and the benefits it brings to your life, you'll find the motivation to keep going."""
    },
    {
        "slug" : "Budget-Friendly_Travel_Destinations_for_2025",
        "date" : date(2025, 1, 10),
        "image" : "03.webp",
        "author" : "Samantha Lee",
        "title" : "Budget-Friendly Travel Destinations for 2025",
        "content" : """Traveling doesn't have to break the bank. 
        This year, explore hidden gems like Vietnam, Portugal, and Georgia (the country, not the state). 
        These destinations offer rich cultural experiences, stunning landscapes, and delicious cuisine at affordable prices. 
        Don't forget to research budget airlines and local accommodation options like hostels or guesthouses. 
        Traveling smart can make your dream adventures more accessible than you think."""
    },
    {
        "slug" : "The_Future_of_AI",
        "date" : date(2025, 1, 18),
        "image" : "05.webp",
        "author" : "Dr. Ryan Carter",
        "title" : "The Future of AI: Opportunities and Challenges",
        "content" : """Artificial Intelligence is transforming the way we live and work. 
        From personalized medicine to self-driving cars, the possibilities are endless.
          However, with great power comes great responsibility. 
          The ethical use of AI, job displacement, and data privacy are pressing concerns that need to be addressed. 
          As we move forward, collaboration between governments, industries, and researchers is essential to ensure AI benefits everyone."""
    },
    {
        "slug" : "The_Secret_to_Perfect_Home-Baked_Bread",
        "date" : date(2025, 1, 22),
        "image" : "04.webp",
        "author" : "Clara Nguyen",
        "title" : "The Secret to Perfect Home-Baked Bread",
        "content" : """There's nothing quite like the aroma of freshly baked bread wafting through your home. 
        The secret to the perfect loaf lies in patience and practice. 
        Start with a simple recipe, use high-quality ingredients, and don’t rush the fermentation process. 
        Letting your dough rest allows the flavors to develop, resulting in a soft, airy interior and a golden crust. 
        Baking bread is both an art and a science—embrace the process and enjoy the delicious rewards!"""
    },
]

def landing_page(request):
    sorted_list = sorted(all_post, key=lambda d: d["date"])
    latest_post = sorted_list[-3:]
    return render(request, "blog/landing_page.html", {
        "latest_post" : latest_post,
    })

def all_post_page(request):
    return render(request, "blog/all_post.html", {
        "all_post" : all_post
    })

def post_detail_page(request, slug):
    for post in all_post:
        if post["slug"] == slug:
            single_post = post
            return render(request, "blog/post_detail.html", {
                "post" : single_post
            })
    return render(request, "blog/404.html")