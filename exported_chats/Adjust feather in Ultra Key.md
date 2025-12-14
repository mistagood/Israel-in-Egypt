# Adjust feather in Ultra Key



---



---



---

how do i adjust the feather etc on my video layer with the ultra key

---



---



---

Got it — you’re in Premiere Pro with **Ultra Key** applied, and you want to soften/blend the keyed edge. Here’s the precise path:  

1. **Select your video layer** in the timeline (the one with Ultra Key applied).  
2. Go to the **Effect Controls** panel.  
3. Under **Ultra Key**, open the section called **Matte Generation**.  
   - Here you’ll see **Pedestal**, **Highlight**, **Shadow**, and **Tolerance**. These adjust the strength of the key.  
4. Just below, expand **Matte Cleanup**. This is where **Choke**, **Soften**, and **Feather** live:  
   - **Choke**: shrinks the matte inward (tightens edges).  
   - **Soften**: blurs the matte edge, smoothing jagged lines.  
   - **Feather**: controls how gradually the keyed edge blends into the background. Increasing this value gives you a softer fade instead of a hard line.  
5. If needed, open **Spill Suppression** to clean up green edges after feathering.  

Tip: Start small (Feather around 5–15) and watch the composite in motion. If edges look too “ghostly,” reduce feather and instead rely more on **Soften**.  

Do you want me to also walk you through how to make only part of the keyed area feather (like just one side of your frame), using a mask + Ultra Key together? That’s often useful in a side-by-side setup like your screenshot.