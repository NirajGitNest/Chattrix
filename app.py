import streamlit as st
import preprocessor
import helper
import pandas as pd

st.sidebar.title("Chattrix 📊")
st.sidebar.subheader("WhatsApp Chat Analyzer")

uploaded_file = st.sidebar.file_uploader("Choose a file")

if uploaded_file is not None:

    data = uploaded_file.getvalue().decode("utf-8")

    df = preprocessor.preprocess(data)

    st.title("Chattrix – WhatsApp Chat Analyzer")

      # RAW DATA SECTION
    with st.expander("📄 View Processed Chat Data"):

        st.dataframe(df)

        csv = df.to_csv(index=False)

        st.download_button(
            label="Download Data as CSV",
            data=csv,
            file_name="chattrix_chat_data.csv",
            mime="text/csv"
        )

    if st.sidebar.button("Analyze Chat"):

        # Fetch stats
        num_messages, words, num_media_messages, num_links = helper.fetch_stats(df)

        st.header("Top Statistics")

        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.metric("Total Messages", num_messages)

        with col2:
            st.metric("Total Words", words)

        with col3:
            st.metric("Media Shared", num_media_messages)

        with col4:
            st.metric("Links Shared", num_links)


        st.header("Most Active Users")

        x, new_df = helper. most_activate_users(df)

        col1, col2 = st.columns(2)

        with col1:
            st.bar_chart(x)

        with col2:
            st.dataframe(new_df)

        st.header("Most Common Words")

        common_words = helper.most_common_words(df)
        common_words_df = pd.DataFrame(common_words)

        st.bar_chart(common_words_df)

        st.header("Emoji Analysis")

        emoji_df = helper.emoji_analysis(df)
        emoji_df = pd.DataFrame(emoji_df, columns=["Emoji", "Count"])

        st.dataframe(emoji_df)

        st.bar_chart(emoji_df.set_index("Emoji"))