import streamlit as st

st.set_page_config(
    page_title="Research Support AI",
    page_icon="📊",
    layout="wide"
)

st.title("Research Support AI")

st.markdown("""
Welcome to the AI-powered research support platform.

Research Support AI was developed to provide researchers with on-demand guidance for common research support needs.
            The tool is designed to complement, not replace, consultation services by helping users explore ideas, 
            learn new methods, and receive immediate assistance throughout the research process.

In addition to providing recommendations, code, and research guidance, the tool is designed to educate users on the workflows 
            and best practices involved in conducting research. 
            By explaining not only what to do but also why and how tasks are performed, Research Support AI aims 
            to support skill development, independent learning, and increased confidence in research-related activities.            

Research Support AI provides:
- Immediate access to research guidance
- A conversational and interactive experience
- Support across multiple stages of the research lifecycle
- Educational explanations designed to build research skills
- Practical examples, code, and recommendations tailored to user needs
- Guidance on research workflows and best practices to help users develop their own analytical and research capabilities
                                   
[Provide feedback about this tool](https://docs.google.com/forms/d/e/1FAIpQLScCBY8vTlE80Rhr5S3RHXPAc993UZvimgGZun01T4Ns3ZFsyw/viewform?usp=sharing&ouid=102398091446876440103) 
""")

st.warning(
    "Important Disclaimer: "

    "Research Support AI is an educational and consultation-support tool. AI-generated content may contain inaccuracies, " \
    "omissions, or outdated information. Users should independently verify important information, statistical methods, code, " \
    "interpretations, and research decisions before applying them in academic, clinical, professional, or publication settings."
)

