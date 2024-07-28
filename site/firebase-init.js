  // Import the functions you need from the SDKs you need
  import { initializeApp } from "https://www.gstatic.com/firebasejs/10.12.4/firebase-app.js";
  import { getAnalytics } from "https://www.gstatic.com/firebasejs/10.12.4/firebase-analytics.js";
  // TODO: Add SDKs for Firebase products that you want to use
  // https://firebase.google.com/docs/web/setup#available-libraries

  // Your web app's Firebase configuration
  // For Firebase JS SDK v7.20.0 and later, measurementId is optional
  const firebaseConfig = {
    apiKey: "AIzaSyAWT5vXVy2P-B2_DM9zgUPNlOeHMzJdi9Q",
    authDomain: "wthrly-5b5e7.firebaseapp.com",
    projectId: "wthrly-5b5e7",
    storageBucket: "wthrly-5b5e7.appspot.com",
    messagingSenderId: "718671076737",
    appId: "1:718671076737:web:3a6c11ec1c44d4f59e5c80",
    measurementId: "G-QEBCL6EFZ7"
  };

  // Initialize Firebase
  const app = initializeApp(firebaseConfig);
  const analytics = getAnalytics(app);
