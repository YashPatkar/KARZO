import { createClient } from "@supabase/supabase-js";
import axios from "axios";

// Supabase Config
const supabase = createClient(
  import.meta.env.VITE_SUPABASE_URL,
  import.meta.env.VITE_SUPABASE_ANON_KEY
);

export { supabase };  // ✅ Now it exports correctly

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

export { validateEmail }; // ✅ Also export validateEmail

// Send magic link after validation & ensure driver exists in the database
export const sendSignInEmail = async (email) => {
  if (!email.toLowerCase().endsWith("@gmail.com")) {
    alert("Only Gmail addresses are allowed.");
    return false;
  } else if (!(await validateEmail(email))) {
    alert("Invalid or non-existent email. Please use a real email.");
    return false;
  }

  try {
    // Check driver status in Supabase
    const { data: driver, error: fetchError } = await supabase
      .from("driver")
      .select("registration_status")
      .eq("email", email)
      .maybeSingle();

    if (fetchError) {
      console.log(fetchError);
      console.log('-----------------');
    }

    let redirectUrl = import.meta.env.VITE_PENDING; // Default to PENDING
    if (driver?.registration_status === "COMPLETED") {
      redirectUrl = import.meta.env.VITE_COMPLETED;
    }

    if (!driver) {
      // Insert driver if not exists
      await supabase.from("driver").insert([
        { email, registration_status: "PENDING" }, // Default state
      ]);
    }

    // Send magic link with the correct redirect URL
    let { error } = await supabase.auth.signInWithOtp({
      email,
      options: { emailRedirectTo: redirectUrl },
    });

    if (error) {
      console.error("Error sending Verification link:", error.message);
      return;
    }

    window.localStorage.setItem("emailForSignIn", email);
    alert("Verification link sent! Check your email.");
  } catch (error) {
    console.error("Unexpected error:", error.message);
  }
};
