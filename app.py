import streamlit as st
import requests

st.title("⚕️ Tabibot")

# Input fields
symptoms = st.text_area("ادخل الأعراض التي تعاني منها: 🧠")
image_url = st.text_input("الرجاء ادخال الصورة التي تعرض عليك الأعراض: 🔍")

# Submit button
if st.button("احصل على التشخيص"):
    if not symptoms:
        st.warning("الرجاء ادخال الأعراض التي تعاني منها.")
    #elif not image_url:
      #  st.warning("Please provide an image URL.")
    else:
        with st.spinner("جاري ارسال البيانات الى التشخيص الآلي"):

            # Replace with your actual webhook URL
            webhook_url = "https://abdallah330.app.n8n.cloud/webhook/e4177812-a0b1-4c2f-9fb2-9bd7827cb9eb"

            payload = {
                "symptoms": symptoms,
                "image_url": image_url
            }

            try:
                response = requests.post(webhook_url, json=payload)
                response.raise_for_status()

                result = response.json()

                st.success("✅ Diagnosis received!")
                st.markdown("### 🔬 Extracted Symptoms")
                st.write(result.get("symptoms"))

                st.markdown("### 🧾 Predicted Conditions (Text-Based)")
                st.write(result.get("text_based_conditions"))

                if result.get("needs_image_analysis"):
                    st.markdown("### 🖼️ Image-Based Condition")
                    st.write(result.get("image_based_condition"))

                st.markdown("### 👨‍⚕️ Recommended Specialist")
                st.write(result.get("recommended_specialist"))

                st.markdown("---")
                st.markdown("### 📋 Final Recommendation")
                st.write(result.get("recommendation", "No final recommendation available."))

            except Exception as e:
                st.error(f"❌ Error: {e}")

