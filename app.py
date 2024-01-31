import streamlit as st
import numpy as np

# Load the visual acuity data
data = np.array([
    [0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 1, 0.666],
    [0, 0, 0, 0, 0, 1, 1, 0.5],
    [0, 0, 0, 0, 1, 1, 1, 0.333],
    [0, 0, 0, 1, 1, 1, 1, 0.25],
    [0, 0, 1, 1, 1, 1, 1, 0.166],
    [0, 1, 1, 1, 1, 1, 1, 0.1]
])

input_patterns = {(0, 0, 0, 0, 0, 0, 0): 1,
                  (0, 0, 0, 0, 0, 0, 1): 0.666,
                  (0, 0, 0, 0, 0, 1, 1): 0.5,
                  (0, 0, 0, 0, 1, 1, 1): 0.333,
                  (0, 0, 0, 1, 1, 1, 1): 0.25,
                  (0, 0, 1, 1, 1, 1, 1): 0.166,
                  (0, 1, 1, 1, 1, 1, 1): 0.1}

# Function to convert Visual Acuity values to the specified format
def format_visual_acuity(acuity):
    if acuity == 1:
        return "6/6 : Normal vision"
    elif acuity == 0.666:
        return "6/9: Slightly reduced vision"
    elif acuity == 0.5:
        return "6/12: Moderate visual impairment"
    elif acuity == 0.333:
        return "6/18: Significant visual impairment; consultation with an eye care professional is advisable."
    elif acuity == 0.25:
        return "6/24: Considerable visual reduction; consultation with an eye care professional advice is recommended."
    elif acuity == 0.166:
        return "6/36: Severe visual impairment; consultation with an eye care professional is crucial."
    elif acuity == 0.1:
        return "6/60: Significant vision compromise; consultation with an eye care professional immediate medical attention is advised."
    else:
        return "Unknown Visual Acuity"

# Streamlit App
def main():
    st.set_page_config(page_title="Far Eyesight Prediction Model", page_icon=":eye:")

    # Navigation bar
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["Home", "About"])

    if page == "Home":
        st.title("Far Eyesight Prediction Model")
        st.header("Important Note:")
        st.markdown("It is crucial to maintain a distance of 6 meters from the screen while evaluating your eyesight.")

        user_responses = []

        for i in range(7):
            st.header(f"Image {i + 1}")
            # Load and display the image
            image_path = f"/content/eyechart_images/image_{i + 1}.png"  # replace with the actual path
            st.image(image_path, caption=f"Image {i + 1}")

            # Collect user response
            response = st.radio(f"Is TextVisibility{i + 1} visible?", ('Yes', 'No'))
            user_responses.append(0 if response == 'Yes' else 1)
            st.write("")  # Add some space between questions       

        # Button to trigger prediction
        if st.button("Predict Visual Acuity"):
            # Use the function to get predictions based on user input
            result = format_visual_acuity(input_patterns[tuple(user_responses)])
            if "consult" in result.lower():
                st.error(f'Predicted Visual Acuity: {result}')
            else:
                st.success(f'Predicted Visual Acuity: {result}')

    elif page == "About":
        st.title("About This Model")
        st.header("Visual Acuity Values:")
        st.markdown(
            """
            - **6/6 : Normal vision:** Clear vision at a standard distance.
            - **6/9: Slightly reduced vision:** Some visual impairment but still functional.
            - **6/12: Moderate visual impairment:** Reduced vision; might need visual aids.
            - **6/18: Significant visual impairment:** Consultation with an eye care professional is advisable.
            - **6/24: Considerable visual reduction:** Seeking professional advice is recommended.
            - **6/36: Severe visual impairment:** Consultation with an eye care professional is crucial.
            - **6/60: Significant vision compromise:** Immediate medical attention is advised.
            """
        )

        st.header("Note:")
        st.markdown("The predictions provided by this model are approximate and not a substitute for professional eye care.")
        st.markdown("It is recommended to consult an eye care professional for accurate assessment and advice.")

        st.header("Reference Eye Chart:")
        eye_chart_path = "eyechart.png"  # replace with the actual path
        st.image(eye_chart_path, caption="Reference Eye Chart", use_column_width=True)

if __name__ == "__main__":
    main()


