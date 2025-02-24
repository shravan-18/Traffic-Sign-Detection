# Traffic Sign Classification with WCM-DCGAN and Xception-Enhanced Vision Transformer (X-ViT)

This repository is the code implementation of our work on **Traffic Sign Classification** under **adverse weather conditions**, combining a **Weather Conditioning Module-Enhanced DCGAN (WCM-DCGAN)** for generating realistic weather-based transformations and an **Xception-ViT hybrid (X-ViT)** for improving classification accuracy.  

Many existing Vision Transformers (ViTs) perform well under normal conditions but struggle when signs are affected by **fog, rain, or low lighting**. Real-world datasets also tend to have **limited variation** in adverse weather samples, making models biased toward specific conditions. To tackle these issues, this work introduces:  

- **WCM-DCGAN**, a **GAN-based data augmentation model** that generates **synthetic weather transformations** using **$\sigma$-scaled fog density** and **$\gamma$-adjusted light diffusion** for more realistic variations.  
- **X-ViT**, a **hybrid Vision Transformer** that integrates **Xception’s convolutional layers** with **patch-adaptive tokenization**, improving recognition of small, high-frequency details in traffic signs.  

## **Architecture Overview**

### **WCM-DCGAN: Data Augmentation with Physically-Based Weather Transformations**
Standard datasets for traffic sign recognition don’t always reflect real-world conditions, especially when it comes to **diverse weather effects**. The **WCM-DCGAN** extends the **DCGAN architecture** by introducing a **Weather Conditioning Module (WCM)** that applies **realistic fog, rain, and snow** to generated images. This allows models to be trained on a more **varied and representative dataset**, improving performance in real-world settings.

<p align="center">
  <img src="https://github.com/shravan-18/Traffic-Sign-Detection/blob/main/Results/Architecture%20Diagrams/GAN-Architecture.png" width="600"/>
</p>

### **X-ViT: Combining Xception with Vision Transformers for Better Feature Extraction**
Instead of using a standard Vision Transformer, **X-ViT** improves classification by combining **Xception’s convolutional layers** with the **self-attention of ViTs**. This hybrid approach helps retain fine details that are often lost in the tokenization process, making it more **effective at recognizing degraded or partially obscured traffic signs**. The model preserves high-frequency textures while still benefiting from the **global reasoning power of transformers**.

<p align="center">
  <img src="https://github.com/shravan-18/Traffic-Sign-Detection/blob/main/Results/Architecture%20Diagrams/Classification-Architecture.png" alt="Xception Vision Transformer Architecture" width="600"/>
</p>

## **Why This Approach?**
- **Traffic sign recognition in bad weather is challenging.** Many datasets don’t fully capture the **range of visual degradations** seen in real life.  
- **Data augmentation alone isn't enough.** Standard augmentation techniques (e.g., brightness shifts, noise) don’t always **match real-world weather effects**. The **WCM-DCGAN** is designed to create physically-based transformations rather than simple distortions.  
- **ViTs struggle with small details.** Traffic signs are often **small objects in high-resolution images**. ViTs work well for general classification but tend to lose fine details when tokenizing images. The **X-ViT** bridges this gap by **incorporating convolutional layers** to extract important **local** features before applying **self-attention**.  

## **Summary**
This work introduces a **weather-aware dataset augmentation method** and a **hybrid ViT model** that improves **traffic sign classification under adverse conditions**. Instead of collecting massive real-world datasets, this approach **expands and enhances existing datasets** through controlled synthetic transformations. The **X-ViT** then ensures that **key details are preserved**, making it more reliable for autonomous driving and other real-world applications.

## **Contributors**
- [Shravan Venkatraman](https://github.com/shravan-18)
- [Abeshek A](https://github.com/Abeshek-03)
- [Santhosh Malarvannan](https://github.com/Sandy055)
- [Shriyans Anumalasetty](https://github.com/Shriyans03)
- [Jashwanth R](https://github.com/jashwanthrk)
- [Joe Dhanith P R](https://github.com)
