import Groq from "groq-sdk";

const groq_api_key = import.meta.env.VITE_GROQ_API_KEY;

const groq = new Groq({
    apiKey: groq_api_key,
    dangerouslyAllowBrowser: true,
});

/**
 * Generate or improve an event description.
 * @param {string} eventName - Name of the event.
 * @param {string} location - Event location.
 * @param {string} date - Event date.
 * @param {string} time - Event time.
 * @param {string} existingDescription - (Optional) If provided, improves the existing description.
 * @returns {Promise<string>} - AI-generated event description.
 */
export const getGroqChatCompletion = async (eventName, location, date, time, existingDescription = "") => {
    try {
        const isImprovement = existingDescription.trim().length > 0;

        const response = await groq.chat.completions.create({
            model: "llama-3.3-70b-versatile",
            messages: [
                {
                    role: "system",
                    content: `You are a fun, engaging, bindas bhidu, chilled indian dude and persuasive assistant. Your goal is to create the most exciting and lively event descriptions that make people want to attend and take a Karzo bike ride 🛵 there. Use casual Indian dude vibes, simple words, and include emoji to make it more fun! and you can generate in english and in hinglish.`,
                },
                {
                    role: "user",
                    content: isImprovement
                        ? `Make this event description even better, more engaging, and persuasive with emoji for an event named "${eventName}" happening at "${location}" on "${date}" at "${time}". The existing description is: "${existingDescription}". Make it more fun and lively under 70 words and dont add timing and date.!`
                        : `Create a fun, engaging 50-word event description for an event named "${eventName}" happening at "${location}" on "${date}" at "${time}". Make it exciting, persuasive, and include emoji! but keep it under 70 words and dont add timing and date.`,
                },
            ],
            max_tokens: 100,
            temperature: 0.8,
        });

        return response.choices[0]?.message?.content || "No response from AI.";
    } catch (error) {
        console.error("Groq AI request failed:", error);
        return "Error generating description.";
    }
};
