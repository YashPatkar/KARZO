import { createClient } from "@supabase/supabase-js";
import axios from "axios";

// Supabase Config
const supabase = createClient(
  import.meta.env.VITE_SUPABASE_URL,
  import.meta.env.VITE_SUPABASE_ANON_KEY
);

// Validate email before sending sign-in link
const validateEmail = async (email) => {
  try {
    const response = await axios.get(
      `https://emailvalidation.abstractapi.com/v1/?api_key=${import.meta.env.VITE_ABSTRACT_API_KEY}&email=${email}`
    );
    return response.data.deliverability === "DELIVERABLE"; // Checks if email is real
  } catch (error) {
    console.error("Email validation error:", error);
    return false;
  }
};

// Send magic link after validation
export const sendSignInEmail = async (email) => {
  if (!email.toLowerCase().endsWith("@gmail.com")) {
    alert("Only Gmail addresses are allowed.");
    return false;
  } else if (!(await validateEmail(email))) {
    alert("Invalid or non-existent email. Please use a real email.");
    return false;
  }

  try {
    let { error } = await supabase.auth.signInWithOtp({
      email,
      options: { emailRedirectTo: import.meta.env.VITE_REDIRECT_URL },
    });

    if (error) {
      console.error("Error sending magic link:", error.message);
      return;
    }

    window.localStorage.setItem("emailForSignIn", email);
    alert("Magic link sent! Check your email.");
  } catch (error) {
    console.error("Unexpected error:", error.message);
  }
};