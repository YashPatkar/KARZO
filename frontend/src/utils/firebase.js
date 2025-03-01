import { getAuth, sendSignInLinkToEmail, sendEmailVerification } from "firebase/auth";
import { initializeApp } from "firebase/app";
import axios from "axios";

// Firebase Config
const firebaseConfig = {
  apiKey: import.meta.env.VITE_FIREBASE_API_KEY,
  authDomain: import.meta.env.VITE_FIREBASE_AUTH_DOMAIN,
  projectId: import.meta.env.VITE_FIREBASE_PROJECT_ID,
  storageBucket: import.meta.env.VITE_FIREBASE_STORAGE_BUCKET,
  messagingSenderId: import.meta.env.VITE_FIREBASE_MESSAGING_SENDER_ID,
  appId: import.meta.env.VITE_FIREBASE_APP_ID,
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const auth = getAuth(app);

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

// Send sign-in link after validation
export const sendSignInEmail = async (email) => {
  if (!email.toLowerCase().endsWith("@gmail.com")) {
    alert("Only Gmail addresses are allowed.");
    return false;
  }
  else if (!await validateEmail(email)) {
    alert("Invalid or non-existent email. Please use a real email.");
    return;
  }

  const actionCodeSettings = {
    url: import.meta.env.VITE_REDIRECT_URL,
    handleCodeInApp: true,
  };

  try {
    await sendSignInLinkToEmail(auth, email, actionCodeSettings);
    window.localStorage.setItem("emailForSignIn", email);
    alert("Sign-in link sent! Check your email.");
  } catch (error) {
    console.error("Error sending email sign-in link:", error.message);
  }
};
