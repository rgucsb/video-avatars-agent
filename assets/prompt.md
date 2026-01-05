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

**Video:** 4K high quality.
**Animation:** Modest facial expressions. Mouth animation in perfect sync with the script. Teeth and lips barely noticeable but synchronized. Subtle body movements only.
**Camera:** NO CAMERA MOVEMENT. Super slow zoom-in or zoom-out only if needed.
**Audio:** High quality. Clear voice. No background noise. No music.
**Text:** No text overlays. No generated text. Nothing added to the image.
**Background:** Keep completely frozen/static. Do not modify, animate, or add anything to the background.
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

**[SCENE 1 - 8 sec | VIEW: view1.png | Nova: Waving + Question screen]**

Hey! Let's solve this system of equations together. We've got y equals 4x and y equals x squared minus 12. We need to find where these two equations intersect.

**[SCENE 2 - 8 sec | VIEW: view2.png | Nova: Pointing + Empty Desmos]**

First, let's open up Desmos and graph these equations. I'm going to type in our first equation.

**[SCENE 3 - 8 sec | VIEW: view3.png | Nova: Pointing + Desmos with y=4x]**

Here's y equals 4x. See that? It's a straight line going through the origin with a slope of 4.

**[SCENE 4 - 8 sec | VIEW: view4.png | Nova: Pointing + Both equations graphed]**

Now let's add the quadratic. Y equals x squared minus 12. This gives us a parabola that opens upward, shifted down 12 units.

**[SCENE 5 - 8 sec | VIEW: view5.png | Nova: Thinking + Zoomed to intersections]**

Now here's the key insight - we're looking for where these graphs cross each other. Those intersection points are our solutions. I can see two points where the line crosses the parabola.

**[SCENE 6 - 8 sec | VIEW: view6.png | Nova: Pointing + Point (6,24) highlighted]**

Let me click on the intersection on the right side - that's where x is positive. Desmos shows us the point is at x equals 6, y equals 24. Let's verify: 4 times 6 is 24, and 6 squared minus 12 is also 24. It checks out!

**[SCENE 7 - 8 sec | VIEW: view7.png | Nova: Celebrating + Answer C selected]**

So our answer is C, which is 6! This is why Desmos is amazing - it helps you avoid calculation mistakes and solve questions super fast. With practice, you can solve even tough problems like this in under 30 seconds. Now try one on your own!

[SCRIPT END]

---

## Scene Breakdown for Video-Avatars-Agent

| Scene | View | Duration | Nova Pose | Visual State | Key Action |
|-------|------|----------|-----------|--------------|------------|
| 1 | view1.png | 8s | waving | Question + choices | Introduction |
| 2 | view2.png | 8s | pointing | Empty Desmos | Open Desmos |
| 3 | view3.png | 8s | pointing | y=4x graphed | First equation |
| 4 | view4.png | 8s | pointing | Both equations | Add parabola |
| 5 | view5.png | 8s | thinking | Zoomed view | Find intersections |
| 6 | view6.png | 8s | pointing | (6,24) highlighted | Verify answer |
| 7 | view7.png | 8s | celebrating | Answer C selected | Conclusion |

**Total Duration:** ~56 seconds (7 scenes × 8 seconds)

---

## VIEW IMAGES (Starting frames for each scene)

The following view images are provided as starting frames. Each scene should use the specified view:

| View # | Filename | Description | Used In Scene |
|--------|----------|-------------|---------------|
| 1 | `view1.png` | Nova waving + Question with answer choices | Scene 1 (Intro) |
| 2 | `view2.png` | Nova pointing + Empty Desmos grid | Scene 2 (Open Desmos) |
| 3 | `view3.png` | Nova pointing + Desmos with y=4x graphed | Scene 3 (First equation) |
| 4 | `view4.png` | Nova pointing + Desmos with both equations | Scene 4 (Both equations) |
| 5 | `view5.png` | Nova thinking + Desmos zoomed to intersections | Scene 5 (Find intersection) |
| 6 | `view6.png` | Nova pointing + Point (6,24) highlighted | Scene 6 (Verify answer) |
| 7 | `view7.png` | Nova celebrating + Answer screen with C) 6 selected | Scene 7 (Conclusion) |

**IMPORTANT:** When generating video for each scene, use the view_index that matches the scene number:
- Scene 1 → view_index: 1
- Scene 2 → view_index: 2
- Scene 3 → view_index: 3
- Scene 4 → view_index: 4
- Scene 5 → view_index: 5
- Scene 6 → view_index: 6
- Scene 7 → view_index: 7

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
