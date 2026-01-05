# Nova Math Video Solution - Prompt Template

## Character Description

* Species: Anthropomorphic geometric low-poly fox
* Name: Nova
* Gender: Gender-neutral
* Age: Appears as a cool older high school student (17-18)
* Professional Background: Math tutor and guide for SAT preparation
* Key Traits: Smart, confident, approachable, and encouraging. Nova has the vibe of a cool upperclassman who actually makes math make sense. Not condescending or overly enthusiastic - just genuinely helpful and relatable.
* Communication Style: Conversational and clear. Uses "we" and "let's" to make it collaborative. Explains the "why" not just the "how." Avoids being preachy or talking down to students.

### Voice Description

* Tone: Confident, friendly, and encouraging. The tone is supportive without being patronizing - like a peer who's good at math helping you out.
* Pitch: Mid-range, slightly energetic.
* Pace: Moderate with natural variation. Slows down for key concepts, picks up slightly during straightforward steps. Uses pauses effectively before revealing answers or important insights.
* Accent: Neutral American, teen-friendly.
* Vocal Characteristics: Clear and natural. Sounds like an actual teenager, not an adult trying to sound young. Authentic and relatable.

### Visual Appearance

> **Design Style:** Simple geometric low-poly (Mint Mobile fox style) - flat colors, triangular shapes, minimalist
> **Head:** Fox head made of geometric triangular shapes. Blue-purple coloring with orange inner ears. Simple black-framed rectangular glasses.
> **Body:** Simple geometric fox body, NOT humanized. Fox proportions with geometric styling.
> **Colors:** Deep blue and purple with gold/orange accents. Flat colors, no gradients.
> **Accessories:** Simple black-framed glasses only. NO clothing, NO hoodie.
> **Expression:** Friendly and smart. Slight confident smile.

## Video Shot Instructions

**Video:** 1080p high quality. Clean white or light gradient background.
**Animation:** Subtle, natural movements. Ears may twitch slightly. Tail gentle sway. Facial expressions match the script emotion (curious when posing question, satisfied when solving).
**Camera:** Minimal movement. Very slow zoom-in during key revelations. Character positioned to left third of frame, leaving right side for Desmos graph overlay.
**Layout:** Split-screen or overlay format:
  - Left/Bottom: Nova character (30-40% of frame)
  - Right/Top: Desmos graph visualization (60-70% of frame)
**Audio:** High quality voice. No background music during explanation. Optional subtle "ding" sound effect on correct answer reveal.
**Text:** Math expressions shown on Desmos graph. Answer highlighted/circled at conclusion.
**Pacing:** 8-second chunks maximum per scene for video-avatars-agent compatibility.

---

# Example: System of Equations Solution

## Question
```
y = 4x
y = x² - 12

A system of two equations is shown. If (x, y) is a solution to the system and x > 0, what is the value of x?
```

## Correct Answer: 6

## Script

[SCRIPT START]

**[SCENE 1 - 8 sec | Nova: Waving pose | Graph: Empty]**

Hey! Let's solve this system of equations together. We've got y equals 4x and y equals x squared minus 12. We need to find where these two equations intersect.

**[SCENE 2 - 8 sec | Nova: Pointing pose | Graph: Shows y = 4x as blue line]**

First, let's graph the linear equation. I'm typing y equals 4x into Desmos. See that? It's a straight line going through the origin with a slope of 4.

**[SCENE 3 - 8 sec | Nova: Pointing pose | Graph: Adds y = x² - 12 as red parabola]**

Now let's add the quadratic. Y equals x squared minus 12. This gives us a parabola that opens upward, shifted down 12 units.

**[SCENE 4 - 10 sec | Nova: Thinking pose | Graph: Zooms to show both curves and intersections]**

Now here's the key insight - we're looking for where these graphs cross each other. Those intersection points are our solutions. I can see two points where the line crosses the parabola.

**[SCENE 5 - 8 sec | Nova: Pointing pose | Graph: Highlights intersection at (6, 24)]**

Let me click on the intersection on the right side - that's where x is positive. Desmos shows us the point is at x equals 6, y equals 24.

**[SCENE 6 - 8 sec | Nova: Confident pose | Graph: Shows (6, 24) highlighted with x = 6 emphasized]**

Let's verify: if x equals 6, then y equals 4 times 6, which is 24. And 6 squared minus 12 is also 24. Both equations check out!

**[SCENE 7 - 7 sec | Nova: Excited pose | Graph: Answer "6" displayed prominently]**

So our answer is 6. Remember - when you see a system of equations on the SAT, Desmos is your best friend for finding those intersection points quickly!

[SCRIPT END]

---

## Scene Breakdown for Video-Avatars-Agent

| Scene | Duration | Nova Pose | Desmos State | Key Action |
|-------|----------|-----------|--------------|------------|
| 1 | 8s | waving | empty grid | Introduction |
| 2 | 8s | pointing | y=4x added | Graph line |
| 3 | 8s | pointing | y=x²-12 added | Graph parabola |
| 4 | 10s | thinking | zoom to intersections | Find solutions |
| 5 | 8s | pointing | highlight (6,24) | Identify answer |
| 6 | 8s | confident | verify point | Confirm solution |
| 7 | 7s | excited | show answer | Conclusion |

**Total Duration:** ~57 seconds

---

## Reference Images Required (4 images for video-avatars-agent)

1. `nova_waving.png` - Welcome/intro pose
2. `nova_pointing.png` - Teaching/explaining pose
3. `nova_thinking.png` - Problem-solving pose
4. `nova_excited_celebrating.png` - Correct answer celebration

---

## Desmos Graph States (Screenshots needed)

1. Empty Desmos grid
2. Grid with y = 4x (blue line)
3. Grid with both equations (line + parabola)
4. Zoomed view showing intersections
5. Intersection point (6, 24) highlighted
6. Final answer display

---

## Production Notes

- Each scene should be generated as a separate 8-second video chunk
- Nova character composited with Desmos screenshots in post-production
- Alternatively: Use screen recording of Desmos with Nova overlay
- Voice can be generated via ElevenLabs or similar TTS with teen voice preset
- Final video assembled from chunks in sequence

---

## Adapting This Template

To create a new math solution video:

1. **Replace the Question** with the new SAT question
2. **Update the Script** with step-by-step Desmos solution
3. **Adjust Scene Count** based on solution complexity (aim for 45-90 seconds total)
4. **Match Nova Poses** to the emotional arc (curious → working → success)
5. **Specify Desmos States** for each scene's graph visualization
