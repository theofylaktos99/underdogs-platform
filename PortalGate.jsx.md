Create a React component named `PortalGate.jsx`.

🎯 PURPOSE:
Acts as a pre-authentication gateway for the UnderDogs platform. Inspired by the "Gates of Moria" scene in Lord of the Rings: The Fellowship of the Ring.

🔹 FUNCTIONALITY:
- Show a glowing quote: "Speak, friend, and enter."
- Input box appears for the user to write the word
- If user enters "melon" (case-insensitive), redirect to `/auth`
- If wrong, show animated error:  
  ❌ “Λυπούμαστε για την άρνηση πρόσβασης. Για να προχωρήσετε, πρέπει πρώτα να δείτε την ταινία: «Η Συντροφιά του Δαχτυλιδιού».”

🔹 STYLE:
- Dark gradient background
- SVG/Moria-style gate illustration in the center
- Neon glowing text (white or light blue)
- Input box styled as terminal line (glowing borders)
- Subtle ambient music (optional)

🔹 TECH:
- React + Tailwind CSS
- `useState`, `useNavigate` (react-router-dom)
- Responsive for desktop and tablet

Deliver the full code of the component, ideally as `PortalGate.jsx`.
