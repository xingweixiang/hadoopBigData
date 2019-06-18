hadoop大数据
=========
## 说明
     学习笔记
## 目录
* [hadoop大数据](#hadoop大数据)
	* [一、主要组件](#一主要组件)
		* [1、HDFS](#1HDFS)
		* [2、MapReduce](#2MapReduce)
		* [3、HBase](#3HBase)
		* [4、ZooKeeper](#4ZooKeeper)
		* [5、Hive](#5Hive)
		* [6、Sqoop](#6Sqoop)
		* [7、Flume](#7Flume)
		* [8、Mahout](#8Mahout)
		* [9、YARN](#9YARN)
		* [10、Mesos](#10Mesos)
		* [11、Spark](#11Spark)
		* [12、kafka](#12kafka)
		* [13、Phoenix](#13Phoenix)
		* [14、Ambari](#14Ambari)
	* [二、大数据平台集群搭建](#二大数据平台集群搭建)
		* [1、Hadoop HDFS安装与配置](#1Hadoop HDFS安装与配置)	
	
### 一、主要组件
以Hadoop为核心，Hadoop大数据应用生态中最主要的组件，在整个大数据应用于研发已经形成了一个基本完善的生态系统。
### 1、HDFS
- Hadoop分布式文件系统，通过流式数据访问，提供高吞吐量应用程序数据访问功能，适合大型数据集的应用程序。
### 2、MapReduce
- 分布式离线计算框架，用Map和Reduce两个函数编程实现基本的并行计算任务。实时流计算一般用Storm
### 3、HBase
- 是一个高可靠性、高性能、面向列、可伸缩的分布式存储系统，利用HBase技术可在廉价PC上搭建起大规模结构化存储集群。
### 4、ZooKeeper
- 是一个分布式的，开放源码的分布式应用程序协调服务，是Hadoop和Hbase的重要组件。
### 5、Hive
- 是建立在 Hadoop 上的数据仓库基础构架，可以将结构化的数据文件映射为一张数据库表，并提供简单的sql查询功能，可以将sql语句转换为MapReduce任务进行运行。
### 6、Sqoop
- 是一个用来将Hadoop和关系型数据库中的数据相互转移的工具，可以将一个关系型数据库<br>
（如 ： MySQL ,Oracle ,Postgres等）中的数据导进到Hadoop的HDFS中，也可以将HDFS的数据导进到关系型数据库中。
### 7、Flume
- 是Cloudera提供的日志收集系统，目前是Apache下的一个孵化项目，Flume支持在日志系统中定制各类数据发送方，用于收集数据。
### 8、Mahout
- 一个开源项目，提供一些可扩展的机器学习领域经典算法的实现，Mahout包含许多实现，包括聚类、分类、推荐过滤、频繁子项挖掘。
### 9、YARN
- 是一个通用资源管理系统，可为上层应用提供统一的资源管理和调度，是MapReduce的改进。
### 10、Mesos
- 是一个通用的集群管理器，是Apache下的开源分布式资源管理框架。
### 11、Spark
- 是一种与 Hadoop 相似的开源集群计算环境，Spark 启用了内存分布数据集，在某些工作负载方面表现得更加优越。
### 12、kafka
- 是一种高吞吐量的分布式发布订阅消息系统，它可以处理消费者在网站中的所有动作流数据。（如：网页浏览，搜索和其他用户的行动）。
### 13、Phoenix
- 是构建在HBase上的一个SQL层，能让我们用标准的JDBC APIs而不是HBase客户端APIs来创建表，插入数据和对HBase数据进行查询。
### 14、Ambari
- i是一种基于Web的工具，支持Apache Hadoop集群的供应、管理和监控。Ambari已支持大多数Hadoop组件，包括HDFS、MapReduce、Hive、Pig、 Hbase、Zookeeper、Sqoop等。