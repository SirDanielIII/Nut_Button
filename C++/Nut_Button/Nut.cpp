#include <SFML\Graphics.hpp>
#include <SFML\Audio.hpp>
#include <iostream>
#include <deque>

// Function to calculate distance
float distance(int x1, int y1, int x2, int y2)
{
	// Calculating distance
	return sqrt(pow(x2 - x1, 2) +
		pow(y2 - y1, 2) * 1.0);
}

class Sound
{
private:
	sf::SoundBuffer soundBuffer;
	std::deque<sf::Sound> soundInstances;

public:
	void Load(std::string filename)
	{
		soundBuffer.loadFromFile(filename);
	}

	void Update(void)
	{
		for (int i = 0; i < soundInstances.size(); ++i)
		{
			if (soundInstances[i].getStatus() == sf::Sound::Stopped)
			{
				soundInstances.erase(soundInstances.begin() + i);
				--i;
			}
		}
	}

	void Play(void)
	{
		soundInstances.push_back(sf::Sound(soundBuffer));
		soundInstances.back().play();
	}

	unsigned int Count()
	{
		soundInstances.size();
	}
};

int main()
{
	sf::Vector2i resolution{ 800,800 };

	sf::RenderWindow window(sf::VideoMode(resolution.x, resolution.y), "Press Me!", sf::Style::Close);
	window.setFramerateLimit(60);

	// Load an image file as texture
	sf::Texture texture;
	if (!texture.loadFromFile("assets/Empty_Nut_Button.png"))
	{
		std::cout << "Error loading image as texture" << std::endl;
	}

	// Create sprite from texture
	sf::Sprite nut_button_empty;
	nut_button_empty.setTexture(texture);

	// Load font
	sf::Font font;
	if (!font.loadFromFile("assets/HelveticaLTStd-Roman.otf"))
	{
		std::cout << "Error loading font file" << std::endl;
	}

	// Create text
	sf::Text nut_text;
	nut_text.setFont(font);
	nut_text.setString("NUT");
	nut_text.setCharacterSize(resolution.x / 3.5);
	nut_text.setFillColor(sf::Color::White);
	nut_text.setPosition(300, 0);

	// Center Text
	sf::FloatRect textRect = nut_text.getLocalBounds();
	nut_text.setOrigin(textRect.left + textRect.width / 2.0f, textRect.top + textRect.height / 2.0f);
	nut_text.setPosition(window.getView().getCenter());

	sf::CircleShape circle(390.F); // This circle covers the image
	circle.setFillColor(sf::Color(36, 116, 255));
	circle.setPosition((window.getSize().x / 2.f) - circle.getRadius(), (window.getSize().y / 2.f) - circle.getRadius());

	// Sound
	Sound nut_sfx;
	nut_sfx.Load("assets/Nut.wav");

	// Game loop
	while (window.isOpen())
	{
		sf::Event event;
		while (window.pollEvent(event))
		{
			switch (event.type)
			{
			case sf::Event::Closed:
				window.close();
				break;
			case sf::Event::MouseButtonPressed:
				if (distance(window.getView().getCenter().x, window.getView().getCenter().y,
					sf::Mouse::getPosition(window).x, sf::Mouse::getPosition(window).y) <= circle.getRadius()) {
					nut_sfx.Play();
				}
			}
		}

		nut_sfx.Update();

		window.clear(sf::Color(255, 255, 255));
		window.draw(nut_button_empty);
		window.draw(nut_text);
		//window.draw(circle);
		window.display();
	}

	return 0;
}