from chatbot import RequirementsChatbot
import os
import questionary

def main():
    chatbot = RequirementsChatbot()
    
    while True:
        # Start a conversation to gather requirements
        story = chatbot.start_conversation()
        
        # Show the generated story
        print("\n📝 Generated User Story:")
        print("------------------------")
        for key, value in story.items():
            if key == 'acceptance_criteria':
                print(f"\n{key}:")
                for criterion in value:
                    print(f"  - {criterion}")
            else:
                print(f"{key}: {value}")
        
        # Ask if user wants to save the story
        if questionary.confirm("Would you like to save this story to a file?").ask():
            # Create stories directory if it doesn't exist
            os.makedirs('stories', exist_ok=True)
            
            # Generate filename from title
            filename = f"stories/{story['title'].lower().replace(' ', '_')}.yaml"
            chatbot.save_story(story, filename)
            print(f"\n✅ Story saved to {filename}")
        
        # Ask if user wants to create another story
        if not questionary.confirm("Would you like to create another user story?").ask():
            print("\n👋 Thank you for using the Requirements Chatbot!")
            break

if __name__ == "__main__":
    main() 