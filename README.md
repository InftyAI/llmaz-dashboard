# Llmaz

**Llmaz**, pronounced as `/lima:z/`, is a building block for users to build their own LLM from A to Z. **We're the aborigines of Kubernetes.**

This is mostly driven by several people who has great enthusiasm about AI at spare time, if you're one of this kind of people, please join us.

🚀 All kinds of contributions are welcomed ! Please follow [Contributing](/CONTRIBUTING.md).

## 🪂 How to run

### Prerequisites

- [Helm](https://helm.sh/)
- [Kind](https://kind.sigs.k8s.io/) (optional)

### Install

```
$ git clone https://github.com/InftyAI/Llmaz.git
$ kind create cluster (ignore this if you already have a Kubernetes cluster)
$ helm install llmaz Llmaz/deploy/llmaz --create-namespace --namespace llmaz --set service.type=NodePort
```

**Visit http://localhost:7860 for WebUI**.

![webui](./images/webui.jpg)

## ✨ Features

- Foundational model management
- Prompt management
- Supervised Fine Tuning
- Model Serving
- Self-Instruct
- Dataset management
- RLHF
- Evaluation
- AI applications, RAG, Chatbot, etc.
- ...

 Still under development, **Let's see what will happen !**

## 👏 Contributors

Thanks to all these contributors. You're the heroes.

<a href="https://github.com/InftyAI/Llmaz/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=InftyAI/Llmaz" />
</a>
