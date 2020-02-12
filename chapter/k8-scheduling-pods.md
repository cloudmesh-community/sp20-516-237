# Kubernetes Scheduling - Assinging pods to nodes  Jonathan Beckford  sp20-516-237

* Jonathan Beckford
* [sp20-516-237](https://github.com/cloudmesh-community/sp20-516-237)
* [report](https://github.com/cloudmesh-community/sp20-516-237/blob/master/chapter/k8-scheduling-pods.md)

## Introduction

A container is an abstraction that in a nutshell represents the local environment where an application will execute.  It is very similar to a physical server or VM but unique in that it does not represent actual infrastructure but rather an abstraction of said infrastructure.  This allows you to decouple your application needs from your infrastructure needs.  This local environment has everything an app needs to run such as programming language packages for example.  Once in a container the application is portable to any infrastructure that can host it.  Kubernetes at a high level is an orchestrator that allows you to place your container on a given piece of infrastructure. It does this by first placing the container in a pod and then deploying that pod to a physical or virtual node (server).  Therefore, pods in Kubernetes are a packaged unit of work that are in a runnable or executable state.  They represent the smallest unit of work in Kubernetes that can be created or deployed.  A pod includes inside of it one or more containers.  Kubernetes supports several different container runtimes but Docker is the most commonly used (1).  There is a one to many relationship between pods and containers.  Meaning that you can design your app to run across several containers within the same pod or you can stick to one container in one pod, it's up to the developer.  See Fig 1 for a more detailed view of a pod.

So how does Kubernetes determine how to assign a pod, it's smallest unit of work, to a given node?  The main way is through the Kubernetes Scheduler.  The Scheduler is responsible for identifying pods with no assigned pod and then assigning those pods to a particular node to run on.  The scheduler uses certain principles to make it's decision of where to assign pods.  These principles and other scheduler details are described in the subsequent section.  See Fig 2 for a view of the Kubernetes echo system and where the Scheduler sits in it.


## Assigning Pods to Nodes


## References (temporary...will use bibtex)
1. https://kubernetes.io/docs/concepts/workloads/pods/pod-overview/
2. https://kubernetes.io/docs/concepts/scheduling/kube-scheduler/

Please work with:

<https://github.com/cloudmesh-community/sp20-516-231/blob/master/chapter/report.md>

:o2: revise ttle if needed 

Default scheduler but showcasing some of the more interesting criteria for routing pods to nodes
  
