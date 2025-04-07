#include <SFML/Graph.hpp>
#include "Graph.hpp"

int main() {
    sf::RenderWindow window(sf::VideoMode(800, 600), "Shortest Path Finder");
    
    // Set up your Graph, Nodes, etc.

    while (window.isOpen()) {
        sf::Event event;
        while (window.pollEvent(event)) {
            if (event.type == sf::Event::Closed)
                window.close();
            // handle clicks for adding nodes/edges
        }

        window.clear(sf::Color::White);

        // draw graph nodes
        // draw edges
        // highlight shortest path if found

        window.display();
    }

    return 0;
}
