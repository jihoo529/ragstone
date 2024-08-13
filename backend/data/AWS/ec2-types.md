##### Instance Types
# Amazon EC2

Copyright © 2024 Amazon Web Services, Inc. and/or its affiliates. All rights reserved.


-----

#### Amazon EC2: Instance Types

Copyright © 2024 Amazon Web Services, Inc. and/or its affiliates. All rights reserved.

Amazon's trademarks and trade dress may not be used in connection with any product or service
that is not Amazon's, in any manner that is likely to cause confusion among customers, or in any
manner that disparages or discredits Amazon. All other trademarks not owned by Amazon are
the property of their respective owners, who may or may not be affiliated with, connected to, or
sponsored by Amazon.


-----

### Table of Contents

**Instance types .................................................................................................................................. 1**

Current generation instances ..................................................................................................................... 1
Previous generation instances ................................................................................................................... 2
Instance performance .................................................................................................................................. 2
Pricing ............................................................................................................................................................. 3

**Naming conventions ........................................................................................................................ 4**
**Specifications ................................................................................................................................... 6**

General purpose ............................................................................................................................................ 7

Available sizes .......................................................................................................................................... 8
Platform summary ................................................................................................................................ 11
Performance specifications ................................................................................................................. 14
Network specifications ......................................................................................................................... 36
Amazon EBS specifications ................................................................................................................. 51
Instance store specifications ............................................................................................................... 70
Security specifications .......................................................................................................................... 76

Compute optimized ................................................................................................................................... 98

Available sizes ........................................................................................................................................ 99
Platform summary ............................................................................................................................. 101
Performance specifications ............................................................................................................... 103
Network specifications ...................................................................................................................... 121
Amazon EBS specifications ............................................................................................................... 131
Instance store specifications ............................................................................................................ 146
Security specifications ....................................................................................................................... 150

Memory optimized .................................................................................................................................. 168

Available sizes ..................................................................................................................................... 169
Platform summary ............................................................................................................................. 172
Performance specifications ............................................................................................................... 176
Network specifications ...................................................................................................................... 204
Amazon EBS specifications ............................................................................................................... 222
Instance store specifications ............................................................................................................ 243
Security specifications ....................................................................................................................... 253

Storage optimized ................................................................................................................................... 278

Available sizes ..................................................................................................................................... 279
Platform summary ............................................................................................................................. 280

iii


-----

Performance specifications ............................................................................................................... 281
Network specifications ...................................................................................................................... 289
Amazon EBS specifications ............................................................................................................... 293
Instance store specifications ............................................................................................................ 299
Security specifications ....................................................................................................................... 305

Accelerated computing ........................................................................................................................... 309

Available sizes ..................................................................................................................................... 309
Platform summary ............................................................................................................................. 311
Performance specifications ............................................................................................................... 313
Network specifications ...................................................................................................................... 326
Amazon EBS specifications ............................................................................................................... 331
Instance store specifications ............................................................................................................ 338
Security specifications ....................................................................................................................... 342

High-performance computing ............................................................................................................... 349

Available sizes ..................................................................................................................................... 350
Platform summary ............................................................................................................................. 350
Performance specifications ............................................................................................................... 351
Network specifications ...................................................................................................................... 352
Amazon EBS specifications ............................................................................................................... 353
Instance store specifications ............................................................................................................ 355
Security specifications ....................................................................................................................... 356

Previous generation ................................................................................................................................. 357

Available sizes ..................................................................................................................................... 358
Platform summary ............................................................................................................................. 359
Performance specifications ............................................................................................................... 360
Network specifications ...................................................................................................................... 366
Amazon EBS specifications ............................................................................................................... 370
Instance store specifications ............................................................................................................ 374
Security specifications ....................................................................................................................... 376

**Instance types by Region ............................................................................................................ 382**

US East (Ohio) .......................................................................................................................................... 382
US East (N. Virginia) ................................................................................................................................ 382
US West (N. California) ........................................................................................................................... 383
US West (Oregon) .................................................................................................................................... 383
Africa (Cape Town) .................................................................................................................................. 384
Asia Pacific (Hong Kong) ........................................................................................................................ 384

iv


-----

Asia Pacific (Hyderabad) ......................................................................................................................... 384
Asia Pacific (Jakarta) ............................................................................................................................... 385
Asia Pacific (Melbourne) ......................................................................................................................... 385
Asia Pacific (Mumbai) .............................................................................................................................. 385
Asia Pacific (Osaka) .................................................................................................................................. 386
Asia Pacific (Seoul) .................................................................................................................................. 386
Asia Pacific (Singapore) .......................................................................................................................... 386
Asia Pacific (Sydney) ................................................................................................................................ 387
Asia Pacific (Tokyo) .................................................................................................................................. 387
Canada (Central) ....................................................................................................................................... 388
Canada West (Calgary) ............................................................................................................................ 388
Europe (Frankfurt) ................................................................................................................................... 389
Europe (Ireland) ........................................................................................................................................ 389
Europe (London) ....................................................................................................................................... 390
Europe (Milan) .......................................................................................................................................... 390
Europe (Paris) ............................................................................................................................................ 390
Europe (Spain) .......................................................................................................................................... 391
Europe (Stockholm) ................................................................................................................................. 391
Europe (Zurich) ......................................................................................................................................... 391
Israel (Tel Aviv) ......................................................................................................................................... 392
Middle East (Bahrain) .............................................................................................................................. 392
Middle East (UAE) .................................................................................................................................... 392
South America (São Paulo) .................................................................................................................... 393
AWS GovCloud (US-East) ....................................................................................................................... 393
AWS GovCloud (US-West) ...................................................................................................................... 393

**AWS Nitro System ....................................................................................................................... 395**

Nitro components .................................................................................................................................... 395
Network feature support ....................................................................................................................... 395
Virtualized instances ............................................................................................................................... 397
Bare metal instances ............................................................................................................................... 398
Nitro instance requirements .................................................................................................................. 399

Linux instances with AWS Graviton processors ............................................................................ 402

**Quotas .......................................................................................................................................... 403**

On-Demand Instance quotas ................................................................................................................. 403
Spot Instance quotas .............................................................................................................................. 404
Dedicated Host quotas ........................................................................................................................... 404


-----

**Document history ........................................................................................................................ 411**

vi


-----

## Amazon EC2 instance types

When you launch an EC2 instance, the instance type that you specify determines the hardware of
the host computer used for your instance. Each instance type offers different compute, memory,
and storage capabilities, and is grouped in an instance family based on these capabilities. Select
an instance type based on the requirements of the application or software that you plan to run on
your instance.

Amazon EC2 dedicates some resources of the host computer, such as CPU, memory, and instance
storage, to a particular instance. Amazon EC2 shares other resources of the host computer, such as
the network and the disk subsystem, among instances. If each instance on a host computer tries
to use as much of one of these shared resources as possible, each receives an equal share of that
resource. However, when a resource is underused, an instance can consume a higher share of that

resource while it's available.

Each instance type provides higher or lower minimum performance from a shared resource. For
example, instance types with high I/O performance have a larger allocation of shared resources.
Allocating a larger share of shared resources also reduces the variance of I/O performance. For
most applications, moderate I/O performance is more than enough. However, for applications that
require greater or more consistent I/O performance, consider an instance type with higher I/O
performance.

**Contents**

-  Current generation instances

-  Previous generation instances

-  Amazon EC2 instance type naming conventions

-  Amazon EC2 instance type specifications

-  Instances built on the AWS Nitro System

-  Amazon EC2 instance type quotas

### Current generation instances

For the best performance, we recommend that you use the following instance types when you
[launch new instances. For more information, see Amazon EC2 Instance Types.](https://aws.amazon.com/ec2/instance-types/)

Current generation instances 1


-----

-  General purpose: M5 | M5a | M5ad | M5d | M5dn | M5n | M5zn | M6a | M6g | M6gd | M6i | M6id

| M6idn | M6in | M7a | M7g | M7gd | M7i | M7i-flex | Mac1 | Mac2 | Mac2-m1ultra | Mac2-m2 |
Mac2-m2pro | T2 | T3 | T3a | T4g

-  Compute optimized: C5 | C5a | C5ad | C5d | C5n | C6a | C6g | C6gd | C6gn | C6i | C6id | C6in | C7a

| C7g | C7gd | C7gn | C7i | C7i-flex

-  Memory optimized: R5 | R5a | R5ad | R5b | R5d | R5dn | R5n | R6a | R6g | R6gd | R6i | R6idn |

R6in | R6id | R7a | R7g | R7gd | R7i | R7iz | R8g | U-3tb1 | U-6tb1 | U-9tb1 | U-12tb1 | U-18tb1
| U-24tb1 | U7i-12tb | U7in-16tb | U7in-24tb | U7in-32tb | X1 | X2gd | X2idn | X2iedn | X2iezn |
X1e | z1d

-  Storage optimized: D2 | D3 | D3en | H1 | I3 | I3en | I4g | I4i | Im4gn | Is4gen

-  Accelerated computing: DL1 | DL2q | F1 | G4ad | G4dn | G5 | G5g | G6 | Gr6 | Inf1 | Inf2 | P2 | P3 |

P3dn | P4d | P4de | P5 | Trn1 | Trn1n | VT1

-  High-performance computing: Hpc6a | Hpc6id | Hpc7a | Hpc7g

### Previous generation instances

Amazon Web Services offers previous generation instance types for users who have optimized their
applications around them and have yet to upgrade. We encourage you to use current generation
instance types to get the best performance, but we continue to support the following previous
generation instance types. For more information about which current generation instance type
[would be a suitable upgrade, see Previous Generation Instances.](https://aws.amazon.com/ec2/previous-generation/)

-  General purpose: A1 | M1 | M2 | M3 | M4 | T1

-  Compute optimized: C1 | C3 | C4

-  Memory optimized: R3 | R4

-  Storage optimized: I2

-  Accelerated computing: G3

### Instance performance

**Fixed performance instances**

Fixed performance instances provide fixed CPU resources. These instances can deliver and sustain
full CPU performance at any time, and for as long as a workload needs it. If you need consistently

Previous generation instances 2


-----

high CPU performance for applications such as video encoding, high volume websites, or HPC
applications, we recommend that you use fixed performance instances.

**Burstable performance instances**

Burstable performance (T) instances provide a baseline level of CPU performance with the
ability to burst above the baseline. The baseline CPU is designed to meet the needs of the
majority of general purpose workloads, such as large-scale micro-services, web servers, small and
medium databases, data logging, code repositories, virtual desktops, and development and test
environments.

The baseline utilization and ability to burst are governed by CPU credits. Each burstable
performance instance continuously earns credits when it stays below the CPU baseline, and
[continuously spends credits when it bursts above the baseline. For more information, see Burstable](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/burstable-performance-instances.html)
[performance instances in the Amazon EC2 User Guide.](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/burstable-performance-instances.html)

**Flex instances**

M7i-flex and C7i-flex instances offer a balance of compute, memory, and network resources, and
they provide the most cost-effective way to run a broad spectrum of general purpose applications.
These instances provide reliable CPU resources to deliver a baseline CPU performance of 40
percent, which is designed to meet the compute requirements for a majority of general purpose
workloads. When more performance is needed, these instances provide the ability to exceed the
baseline CPU performance and deliver up to 100 percent CPU performance for 95 percent of the
time over a 24-hour window.

M7i-flex and C7i-flex instances running at a high CPU utilization that is consistently above the
baseline for long periods of time might see a gradual reduction in the maximum burst CPU
[throughput. For more information, see M7i-flex instances and C7i-flex instances.](https://aws.amazon.com/ec2/instance-types/m7i/)

### Pricing

[For pricing information, see Amazon EC2 Pricing.](https://aws.amazon.com/ec2/pricing/)

Pricing 3


-----

## Amazon EC2 instance type naming conventions

Amazon EC2 provides a variety of instance types so you can choose the type that best meets
your requirements. Instance types are named based on their family, generation, processor family,
additional capabilities, and size. The first position of the instance type name indicates the instance

family, for example c. The second position indicates the instance generation, for example 7. The

third position indicates the processor family, for example g. The remaining letters before the period

indicate additional capabilities, such as instance store volumes. After the period (.) is the instance

size, such as small or 4xlarge, or metal for bare metal instances.

|Instance families|Processor families|Additional capabilities|
|---|---|---|
|• C – Compute optimized • D – Dense storage • F – FPGA • G – Graphics intensive|• a – AMD processors • g – AWS Graviton processor s • i – Intel processors|• b – Block storage optimizat ion • d – Instance store volumes • e – Extra storage or memory • flex – Flex instance|


-----

|• Hpc – High performance computing • I – Storage optimized • Im – Storage optimized (1 to 4 ratio of vCPU to memory) • Is – Storage optimized (1 to 6 ratio of vCPU to memory) • Inf – AWS Inferentia • M – General purpose • Mac – macOS • P – GPU accelerated • R – Memory optimized • T – Burstable performance • Trn – AWS Trainium • U – High memory • VT – Video transcoding • X – Memory intensive|Col2|• n – Network and EBS optimized • q – Qualcomm inference accelerators • z – High performance|
|---|---|---|


**Instance families** **Processor families** **Additional capabilities**


-----

## Amazon EC2 instance type specifications

Amazon EC2 provides a wide selection of instance types optimized to fit different use cases.
Instance types comprise varying combinations of CPU, memory, storage, and networking capacity
and give you the flexibility to choose the appropriate mix of resources for your applications. Each
instance type includes one or more instance sizes, allowing you to scale your resources to the

requirements of your target workload.

We group EC2 instance into the following categories:

-  General purpose – Provide a balance of compute, memory, and networking resources. These

instances are ideal for applications that use these resources in equal proportions, such as web
servers and code repositories.

**Burstable performance – The T instance family is also referred to as burstable performance**
instances. These instances provide a baseline CPU performance with the ability to burst above
[the baseline at any time. For more information, see Burstable performance instances in the](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/burstable-performance-instances.html)
_Amazon EC2 User Guide._

-  Compute optimized – Designed for compute intensive applications that benefit from high

performance processors. These instances are ideal for batch processing workloads, media
transcoding, high performance web servers, high performance computing (HPC), scientific
modeling, dedicated gaming servers, ad server engines, and machine learning inference.

-  Memory optimized – Designed to deliver fast performance for workloads that process large data

sets in memory.

-  Storage optimized – Designed for workloads that require high, sequential read and write access

to very large data sets on local storage. They are optimized to deliver tens of thousands of lowlatency, random I/O operations per second (IOPS) to applications.

-  Accelerated computing – Use hardware accelerators, or co-processors, to perform functions,

such as floating point number calculations, graphics processing, or data pattern matching, more
efficiently than is possible in software running on CPUs.

-  High-performance computing – Purpose built to offer the best price performance for running

HPC workloads at scale on AWS. These instances are ideal for applications that benefit from
high-performance processors, such as large, complex simulations and deep learning workloads.

-  Previous generation – AWS offers previous generation instance types for users who have

optimized their applications around them and have yet to upgrade. We encourage you to use


-----

current generation instance types to get the best performance, but we continue to support
previous generation instance types.

To determine which instance types meet your requirements, such as supported Regions, compute
[resources, or storage resources, see Find an Amazon EC2 instance type in the Amazon EC2 User](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-discovery.html)
_Guide._

**Categories**

-  Specifications for Amazon EC2 general purpose instances

-  Specifications for Amazon EC2 compute optimized instances

-  Specifications for Amazon EC2 memory optimized instances

-  Specifications for Amazon EC2 storage optimized instances

-  Specifications for Amazon EC2 accelerated computing instances

-  Specifications for Amazon EC2 high-performance computing instances

-  Specifications for Amazon EC2 previous generation instances

**Pricing**

[For pricing information, see Amazon EC2 On-Demand Pricing.](https://aws.amazon.com/ec2/pricing/on-demand/)

### Specifications for Amazon EC2 general purpose instances

General purpose instances provide a balance of compute, memory, and networking resources.
These instances are ideal for applications that use these resources in equal proportions, such as
web servers and code repositories.

For information on previous generation instance types of this category, such as M4 instances, see
Specifications for Amazon EC2 previous generation instances.

**Contents**

-  Available sizes

-  Platform summary

-  Performance specifications

-  Network specifications

General purpose


-----

-  Amazon EBS specifications

-  Instance store specifications

-  Security specifications

**Pricing**

[For pricing information, see Amazon EC2 On-Demand Pricing.](https://aws.amazon.com/ec2/pricing/on-demand/)

#### Available sizes

|Instance type|Available sizes|
|---|---|
|M5|m5.large | m5.xlarge | m5.2xlarge | m5.4xlarge | m5.8xlarge | m5.12xlarge | m5.16xlarge | m5.24xlarge | m5.metal|
|M5a|m5a.large | m5a.xlarge | m5a.2xlarge | m5a.4xlarge | m5a.8xlar ge | m5a.12xlarge | m5a.16xlarge | m5a.24xlarge|
|M5ad|m5ad.large | m5ad.xlarge | m5ad.2xlarge | m5ad.4xlarge | m5ad.8xlarge | m5ad.12xlarge | m5ad.16xlarge | m5ad.24xlarge|
|M5d|m5d.large | m5d.xlarge | m5d.2xlarge | m5d.4xlarge | m5d.8xlar ge | m5d.12xlarge | m5d.16xlarge | m5d.24xlarge | m5d.metal|
|M5dn|m5dn.large | m5dn.xlarge | m5dn.2xlarge | m5dn.4xlarge | m5dn.8xlarge | m5dn.12xlarge | m5dn.16xlarge | m5dn.24xlarge | m5dn.metal|
|M5n|m5n.large | m5n.xlarge | m5n.2xlarge | m5n.4xlarge | m5n.8xlar ge | m5n.12xlarge | m5n.16xlarge | m5n.24xlarge | m5n.metal|
|M5zn|m5zn.large | m5zn.xlarge | m5zn.2xlarge | m5zn.3xlarge | m5zn.6xlarge | m5zn.12xlarge | m5zn.metal|
|M6a|m6a.large | m6a.xlarge | m6a.2xlarge | m6a.4xlarge | m6a.8xlar ge | m6a.12xlarge | m6a.16xlarge | m6a.24xlarge | m6a.32xlarge | m6a.48xlarge | m6a.metal|



Available sizes


-----

|Instance type|Available sizes|
|---|---|
|M6g|m6g.medium | m6g.large | m6g.xlarge | m6g.2xlarge | m6g.4xlarge | m6g.8xlarge | m6g.12xlarge | m6g.16xlarge | m6g.metal|
|M6gd|m6gd.medium | m6gd.large | m6gd.xlarge | m6gd.2xlarge | m6gd.4xlarge | m6gd.8xlarge | m6gd.12xlarge | m6gd.16xlarge | m6gd.metal|
|M6i|m6i.large | m6i.xlarge | m6i.2xlarge | m6i.4xlarge | m6i.8xlar ge | m6i.12xlarge | m6i.16xlarge | m6i.24xlarge | m6i.32xlarge | m6i.metal|
|M6id|m6id.large | m6id.xlarge | m6id.2xlarge | m6id.4xlarge | m6id.8xlarge | m6id.12xlarge | m6id.16xlarge | m6id.24xlarge | m6id.32xlarge | m6id.metal|
|M6idn|m6idn.large | m6idn.xlarge | m6idn.2xlarge | m6idn.4xlarge | m6idn.8xlarge | m6idn.12xlarge | m6idn.16xlarge | m6idn.24x large | m6idn.32xlarge | m6idn.metal|
|M6in|m6in.large | m6in.xlarge | m6in.2xlarge | m6in.4xlarge | m6in.8xlarge | m6in.12xlarge | m6in.16xlarge | m6in.24xlarge | m6in.32xlarge | m6in.metal|
|M7a|m7a.medium | m7a.large | m7a.xlarge | m7a.2xlarge | m7a.4xlar ge | m7a.8xlarge | m7a.12xlarge | m7a.16xlarge | m7a.24xlarge | m7a.32xlarge | m7a.48xlarge | m7a.metal-48xl|
|M7g|m7g.medium | m7g.large | m7g.xlarge | m7g.2xlarge | m7g.4xlarge | m7g.8xlarge | m7g.12xlarge | m7g.16xlarge | m7g.metal|
|M7gd|m7gd.medium | m7gd.large | m7gd.xlarge | m7gd.2xlarge | m7gd.4xlarge | m7gd.8xlarge | m7gd.12xlarge | m7gd.16xlarge | m7gd.metal|


Available sizes


**Available sizes**


-----

|Instance type|Available sizes|
|---|---|
|M7i|m7i.large | m7i.xlarge | m7i.2xlarge | m7i.4xlarge | m7i.8xlar ge | m7i.12xlarge | m7i.16xlarge | m7i.24xlarge | m7i.48xlarge | m7i.metal-24xl | m7i.metal-48xl|
|M7i-flex|m7i-flex.large | m7i-flex.xlarge | m7i-flex.2xlarge | m7i-flex. 4xlarge | m7i-flex.8xlarge|
|Mac1|mac1.metal|
|Mac2|mac2.metal|
|Mac2- m1ultra|mac2-m1ultra.metal|
|Mac2-m2|mac2-m2.metal|
|Mac2- m2pro|mac2-m2pro.metal|
|T2|t2.nano | t2.micro | t2.small | t2.medium | t2.large | t2.xlarge | t2.2xlarge|
|T3|t3.nano | t3.micro | t3.small | t3.medium | t3.large | t3.xlarge | t3.2xlarge|
|T3a|t3a.nano | t3a.micro | t3a.small | t3a.medium | t3a.large | t3a.xlarge | t3a.2xlarge|
|T4g|t4g.nano | t4g.micro | t4g.small | t4g.medium | t4g.large | t4g.xlarge | t4g.2xlarge|


Available sizes 10


-----

#### Platform summary

|Instance type|Hyperviso r|Processor type (architec ture)|Metal instance available|Dedicated s Hosts support|Spot support|Hibernati on support|Supported operating systems|
|---|---|---|---|---|---|---|---|
|M5|Nitro v2|Intel (x86_64)|✓|✓|✓|✓|Windows | Linux|
|M5a|Nitro v2|AMD (x86_64)|✗|✓|✓|✓|Windows | Linux|
|M5ad|Nitro v2|AMD (x86_64)|✗|✗|✓|✓|Windows | Linux|
|M5d|Nitro v2|Intel (x86_64)|✓|✓|✓|✓|Windows | Linux|
|M5dn|Nitro v3|Intel (x86_64)|✓|✓|✓|✗|Windows | Linux|
|M5n|Nitro v3|Intel (x86_64)|✓|✓|✓|✗|Windows | Linux|
|M5zn|Nitro v3|Intel (x86_64)|✓|✓|✓|✗|Windows | Linux|
|M6a|Nitro v4|AMD (x86_64)|✓|✓|✓|✗|Windows | Linux|
|M6g|Nitro v2|AWS Graviton (arm64)|✓|✓|✓|✓|Linux|
|M6gd|Nitro v2|AWS Graviton (arm64)|✓|✓|✓|✓|Linux|



Platform summary 11


-----

|Col1|Col2|ture)|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|M6i|Nitro v4|Intel (x86_64)|✓|✓|✓|✓|Windows | Linux|
|M6id|Nitro v4|Intel (x86_64)|✓|✓|✓|✓|Windows | Linux|
|M6idn|Nitro v4|Intel (x86_64)|✓|✓|✓|✗|Windows | Linux|
|M6in|Nitro v4|Intel (x86_64)|✓|✓|✓|✗|Windows | Linux|
|M7a|Nitro v4|AMD (x86_64)|✓|✓|✓|✗|Windows | Linux|
|M7g|Nitro v4|AWS Graviton (arm64)|✓|✓|✓|✓|Linux|
|M7gd|Nitro v4|AWS Graviton (arm64)|✓|✓|✓|✓|Linux|
|M7i|Nitro v4|Intel (x86_64)|✓|✓|✓|✓|Windows | Linux|
|M7i-flex|Nitro v4|Intel (x86_64)|✗|✗|✓|✓|Windows | Linux|
|Mac1|Nitro v2|Intel (x86_64_m ac)|✓|✓|✗|✗|Linux|


**Instance** **Hyperviso** **Processor** **Metal** **Dedicated** **Spot** **Hibernati** **Supported**
**type** **r** **type** **instances Hosts** **support** **on** **operating**

**(architec** **available** **support** **support** **systems**
**ture)**


Platform summary 12


-----

|Col1|Col2|ture)|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|Mac2|Nitro v2|Apple (arm64_ma c)|✓|✓|✗|✗|Linux|
|Mac2- m1ultra|Nitro v2|Apple (arm64_ma c)|✓|✓|✗|✗|Linux|
|Mac2- m2|Nitro v2|Apple (arm64_ma c)|✓|✓|✗|✗|Linux|
|Mac2- m2pro|Nitro v2|Apple (arm64_ma c)|✓|✓|✗|✗|Linux|
|T2|Xen|Intel (x86_64)|✗|✗|✓|✓|Windows | Linux|
|T3|Nitro v2|Intel (x86_64)|✗|✓|✓|✓|Windows | Linux|
|T3a|Nitro v2|AMD (x86_64)|✗|✗|✓|✓|Windows | Linux|
|T4g|Nitro v2|AWS Graviton (arm64)|✗|✗|✓|✗|Linux|


**Instance** **Hyperviso** **Processor** **Metal** **Dedicated** **Spot** **Hibernati** **Supported**
**type** **r** **type** **instances Hosts** **support** **on** **operating**

**(architec** **available** **support** **support** **systems**
**ture)**


Platform summary 13


-----

#### Performance specifications

|Instance type|Burstabl|eMemor (GiB)|y Processor|vCPUs|CPU cores|Thread per core|s Accelerat ors|Acceler or memor|
|---|---|---|---|---|---|---|---|---|
|M5|||||||||
|m5.large|✗|8.00|Intel Xeon Platinum 8175|2|1|2|✗|✗|
|m5.xlarge|✗|16.00|Intel Xeon Platinum 8175|4|2|2|✗|✗|
|m5.2xlarge|✗|32.00|Intel Xeon Platinum 8175|8|4|2|✗|✗|
|m5.4xlarge|✗|64.00|Intel Xeon Platinum 8175|16|8|2|✗|✗|
|m5.8xlarge|✗|128.00|Intel Xeon Platinum 8175|32|16|2|✗|✗|
|m5.12xlarge|✗|192.00|Intel Xeon Platinum 8175|48|24|2|✗|✗|
|m5.16xlarge|✗|256.00|Intel Xeon Platinum 8175|64|32|2|✗|✗|



Performance specifications 14


-----

**Instance**


**BurstableMemory**


**Processor** **vCPUs CPU**


**Threads Accelerat**


**Accelerat**

|type|Col2|(GiB)|Col4|Col5|cores|per core|ors|or memor|
|---|---|---|---|---|---|---|---|---|
|m5.24xlarge|✗|384.00|Intel Xeon Platinum 8175|96|48|2|✗|✗|
|m5.metal|✗|384.00|Intel Xeon Platinum 8175|96|48|2|✗|✗|
|M5a|||||||||
|m5a.large|✗|8.00|AMD EPYC 7571|2|1|2|✗|✗|
|m5a.xlarge|✗|16.00|AMD EPYC 7571|4|2|2|✗|✗|
|m5a.2xlarge|✗|32.00|AMD EPYC 7571|8|4|2|✗|✗|
|m5a.4xlarge|✗|64.00|AMD EPYC 7571|16|8|2|✗|✗|
|m5a.8xlarge|✗|128.00|AMD EPYC 7571|32|16|2|✗|✗|
|m5a.12xla rge|✗|192.00|AMD EPYC 7571|48|24|2|✗|✗|
|m5a.16xla rge|✗|256.00|AMD EPYC 7571|64|32|2|✗|✗|
|m5a.24xla rge|✗|384.00|AMD EPYC 7571|96|48|2|✗|✗|
|M5ad|||||||||


Performance specifications 15


-----

**Instance**


**BurstableMemory**


**Processor** **vCPUs CPU**


**Threads Accelerat**


**Accelerat**

|type|Col2|(GiB)|Col4|Col5|cores|per core|ors|or memor|
|---|---|---|---|---|---|---|---|---|
|m5ad.large|✗|8.00|AMD EPYC 7571|2|1|2|✗|✗|
|m5ad.xlarge|✗|16.00|AMD EPYC 7571|4|2|2|✗|✗|
|m5ad.2xla rge|✗|32.00|AMD EPYC 7571|8|4|2|✗|✗|
|m5ad.4xla rge|✗|64.00|AMD EPYC 7571|16|8|2|✗|✗|
|m5ad.8xla rge|✗|128.00|AMD EPYC 7571|32|16|2|✗|✗|
|m5ad.12xl arge|✗|192.00|AMD EPYC 7571|48|24|2|✗|✗|
|m5ad.16xl arge|✗|256.00|AMD EPYC 7571|64|32|2|✗|✗|
|m5ad.24xl arge|✗|384.00|AMD EPYC 7571|96|48|2|✗|✗|
|M5d|||||||||
|m5d.large|✗|8.00|Intel Xeon Platinum 8175|2|1|2|✗|✗|
|m5d.xlarge|✗|16.00|Intel Xeon Platinum 8175|4|2|2|✗|✗|


Performance specifications 16


-----

**Instance**


**BurstableMemory**


**Processor** **vCPUs CPU**


**Threads Accelerat**


**Accelerat**

|type|Col2|(GiB)|Col4|Col5|cores|per core|ors|or memor|
|---|---|---|---|---|---|---|---|---|
|m5d.2xlarge|✗|32.00|Intel Xeon Platinum 8175|8|4|2|✗|✗|
|m5d.4xlarge|✗|64.00|Intel Xeon Platinum 8175|16|8|2|✗|✗|
|m5d.8xlarge|✗|128.00|Intel Xeon Platinum 8175|32|16|2|✗|✗|
|m5d.12xla rge|✗|192.00|Intel Xeon Platinum 8175|48|24|2|✗|✗|
|m5d.16xla rge|✗|256.00|Intel Xeon Platinum 8175|64|32|2|✗|✗|
|m5d.24xla rge|✗|384.00|Intel Xeon Platinum 8175|96|48|2|✗|✗|
|m5d.metal|✗|384.00|Intel Xeon Platinum 8175|96|48|2|✗|✗|
|M5dn|||||||||
|m5dn.large|✗|8.00|Intel Xeon Platinum 8259|2|1|2|✗|✗|


Performance specifications 17


-----

**Instance**


**BurstableMemory**


**Processor** **vCPUs CPU**


**Threads Accelerat**


**Accelerat**

|type|Col2|(GiB)|Col4|Col5|cores|per core|ors|or memor|
|---|---|---|---|---|---|---|---|---|
|m5dn.xlarge|✗|16.00|Intel Xeon Platinum 8259|4|2|2|✗|✗|
|m5dn.2xla rge|✗|32.00|Intel Xeon Platinum 8259|8|4|2|✗|✗|
|m5dn.4xla rge|✗|64.00|Intel Xeon Platinum 8259|16|8|2|✗|✗|
|m5dn.8xla rge|✗|128.00|Intel Xeon Platinum 8259|32|16|2|✗|✗|
|m5dn.12xl arge|✗|192.00|Intel Xeon Platinum 8259|48|24|2|✗|✗|
|m5dn.16xl arge|✗|256.00|Intel Xeon Platinum 8259|64|32|2|✗|✗|
|m5dn.24xl arge|✗|384.00|Intel Xeon Platinum 8259|96|48|2|✗|✗|
|m5dn.metal|✗|384.00|Intel Xeon Platinum 8259|96|48|2|✗|✗|
|M5n|||||||||


Performance specifications 18


-----

**Instance**


**BurstableMemory**


**Processor** **vCPUs CPU**


**Threads Accelerat**


**Accelerat**

|type|Col2|(GiB)|Col4|Col5|cores|per core|ors|or memor|
|---|---|---|---|---|---|---|---|---|
|m5n.large|✗|8.00|Intel Xeon Platinum 8259|2|1|2|✗|✗|
|m5n.xlarge|✗|16.00|Intel Xeon Platinum 8259|4|2|2|✗|✗|
|m5n.2xlarge|✗|32.00|Intel Xeon Platinum 8259|8|4|2|✗|✗|
|m5n.4xlarge|✗|64.00|Intel Xeon Platinum 8259|16|8|2|✗|✗|
|m5n.8xlarge|✗|128.00|Intel Xeon Platinum 8259|32|16|2|✗|✗|
|m5n.12xla rge|✗|192.00|Intel Xeon Platinum 8259|48|24|2|✗|✗|
|m5n.16xla rge|✗|256.00|Intel Xeon Platinum 8259|64|32|2|✗|✗|
|m5n.24xla rge|✗|384.00|Intel Xeon Platinum 8259|96|48|2|✗|✗|
|m5n.metal|✗|384.00|Intel Xeon Platinum 8259|96|48|2|✗|✗|


Performance specifications 19


-----

|M5zn|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
|m5zn.large|✗|8.00|Intel Xeon Platinum 8252|2|1|2|✗|✗|
|m5zn.xlarge|✗|16.00|Intel Xeon Platinum 8252|4|2|2|✗|✗|
|m5zn.2xla rge|✗|32.00|Intel Xeon Platinum 8252|8|4|2|✗|✗|
|m5zn.3xla rge|✗|48.00|Intel Xeon Platinum 8252|12|6|2|✗|✗|
|m5zn.6xla rge|✗|96.00|Intel Xeon Platinum 8252|24|12|2|✗|✗|
|m5zn.12xl arge|✗|192.00|Intel Xeon Platinum 8252|48|24|2|✗|✗|
|m5zn.metal|✗|192.00|Intel Xeon Platinum 8252|48|24|2|✗|✗|
|M6a|||||||||
|m6a.large|✗|8.00|AMD EPYC 7R13|2|1|2|✗|✗|


**Instance** **BurstableMemory Processor** **vCPUs CPU** **Threads Accelerat** **Accelerat**
**type** **(GiB)** **cores** **per** **ors** **or**

**core** **memory**

Performance specifications 20


-----

**Instance**


**BurstableMemory**


**Processor** **vCPUs CPU**


**Threads Accelerat**


**Accelerat**

|type|Col2|(GiB)|Col4|Col5|cores|per core|ors|or memor|
|---|---|---|---|---|---|---|---|---|
|m6a.xlarge|✗|16.00|AMD EPYC 7R13|4|2|2|✗|✗|
|m6a.2xlarge|✗|32.00|AMD EPYC 7R13|8|4|2|✗|✗|
|m6a.4xlarge|✗|64.00|AMD EPYC 7R13|16|8|2|✗|✗|
|m6a.8xlarge|✗|128.00|AMD EPYC 7R13|32|16|2|✗|✗|
|m6a.12xla rge|✗|192.00|AMD EPYC 7R13|48|24|2|✗|✗|
|m6a.16xla rge|✗|256.00|AMD EPYC 7R13|64|32|2|✗|✗|
|m6a.24xla rge|✗|384.00|AMD EPYC 7R13|96|48|2|✗|✗|
|m6a.32xla rge|✗|512.00|AMD EPYC 7R13|128|64|2|✗|✗|
|m6a.48xla rge|✗|768.00|AMD EPYC 7R13|192|96|2|✗|✗|
|m6a.metal|✗|768.00|AMD EPYC 7R13|192|96|2|✗|✗|
|M6g|||||||||
|m6g.mediu m|✗|4.00|AWS Graviton2 Processor|1|1|1|✗|✗|


Performance specifications 21


-----

**Instance**


**BurstableMemory**


**Processor** **vCPUs CPU**


**Threads Accelerat**


**Accelerat**

|type|Col2|(GiB)|Col4|Col5|cores|per core|ors|or memor|
|---|---|---|---|---|---|---|---|---|
|m6g.large|✗|8.00|AWS Graviton2 Processor|2|2|1|✗|✗|
|m6g.xlarge|✗|16.00|AWS Graviton2 Processor|4|4|1|✗|✗|
|m6g.2xlarge|✗|32.00|AWS Graviton2 Processor|8|8|1|✗|✗|
|m6g.4xlarge|✗|64.00|AWS Graviton2 Processor|16|16|1|✗|✗|
|m6g.8xlarge|✗|128.00|AWS Graviton2 Processor|32|32|1|✗|✗|
|m6g.12xla rge|✗|192.00|AWS Graviton2 Processor|48|48|1|✗|✗|
|m6g.16xla rge|✗|256.00|AWS Graviton2 Processor|64|64|1|✗|✗|
|m6g.metal|✗|256.00|AWS Graviton2 Processor|64|64|1|✗|✗|
|M6gd|||||||||


Performance specifications 22


-----

**Instance**


**BurstableMemory**


**Processor** **vCPUs CPU**


**Threads Accelerat**


**Accelerat**

|type|Col2|(GiB)|Col4|Col5|cores|per core|ors|or memor|
|---|---|---|---|---|---|---|---|---|
|m6gd.medi um|✗|4.00|AWS Graviton2 Processor|1|1|1|✗|✗|
|m6gd.large|✗|8.00|AWS Graviton2 Processor|2|2|1|✗|✗|
|m6gd.xlarge|✗|16.00|AWS Graviton2 Processor|4|4|1|✗|✗|
|m6gd.2xla rge|✗|32.00|AWS Graviton2 Processor|8|8|1|✗|✗|
|m6gd.4xla rge|✗|64.00|AWS Graviton2 Processor|16|16|1|✗|✗|
|m6gd.8xla rge|✗|128.00|AWS Graviton2 Processor|32|32|1|✗|✗|
|m6gd.12xl arge|✗|192.00|AWS Graviton2 Processor|48|48|1|✗|✗|
|m6gd.16xl arge|✗|256.00|AWS Graviton2 Processor|64|64|1|✗|✗|
|m6gd.metal|✗|256.00|AWS Graviton2 Processor|64|64|1|✗|✗|


Performance specifications 23


-----

|M6i|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
|m6i.large|✗|8.00|Intel Xeon Ice Lake|2|1|2|✗|✗|
|m6i.xlarge|✗|16.00|Intel Xeon Ice Lake|4|2|2|✗|✗|
|m6i.2xlarge|✗|32.00|Intel Xeon Ice Lake|8|4|2|✗|✗|
|m6i.4xlarge|✗|64.00|Intel Xeon Ice Lake|16|8|2|✗|✗|
|m6i.8xlarge|✗|128.00|Intel Xeon Ice Lake|32|16|2|✗|✗|
|m6i.12xla rge|✗|192.00|Intel Xeon Ice Lake|48|24|2|✗|✗|
|m6i.16xla rge|✗|256.00|Intel Xeon Ice Lake|64|32|2|✗|✗|
|m6i.24xla rge|✗|384.00|Intel Xeon Ice Lake|96|48|2|✗|✗|
|m6i.32xla rge|✗|512.00|Intel Xeon Ice Lake|128|64|2|✗|✗|
|m6i.metal|✗|512.00|Intel Xeon Ice Lake|128|64|2|✗|✗|
|M6id|||||||||
|m6id.large|✗|8.00|Intel Xeon Ice Lake|2|1|2|✗|✗|


**Instance** **BurstableMemory Processor** **vCPUs CPU** **Threads Accelerat** **Accelerat**
**type** **(GiB)** **cores** **per** **ors** **or**

**core** **memory**

Performance specifications 24


-----

**Instance**


**BurstableMemory**


**Processor** **vCPUs CPU**


**Threads Accelerat**


**Accelerat**

|type|Col2|(GiB)|Col4|Col5|cores|per core|ors|or memor|
|---|---|---|---|---|---|---|---|---|
|m6id.xlarge|✗|16.00|Intel Xeon Ice Lake|4|2|2|✗|✗|
|m6id.2xla rge|✗|32.00|Intel Xeon Ice Lake|8|4|2|✗|✗|
|m6id.4xla rge|✗|64.00|Intel Xeon Ice Lake|16|8|2|✗|✗|
|m6id.8xla rge|✗|128.00|Intel Xeon Ice Lake|32|16|2|✗|✗|
|m6id.12xl arge|✗|192.00|Intel Xeon Ice Lake|48|24|2|✗|✗|
|m6id.16xl arge|✗|256.00|Intel Xeon Ice Lake|64|32|2|✗|✗|
|m6id.24xl arge|✗|384.00|Intel Xeon Ice Lake|96|48|2|✗|✗|
|m6id.32xl arge|✗|512.00|Intel Xeon Ice Lake|128|64|2|✗|✗|
|m6id.metal|✗|512.00|Intel Xeon Ice Lake|128|64|2|✗|✗|
|M6idn|||||||||
|m6idn.large|✗|8.00|Intel Xeon Ice Lake|2|1|2|✗|✗|
|m6idn.xla rge|✗|16.00|Intel Xeon Ice Lake|4|2|2|✗|✗|


Performance specifications 25


-----

**Instance**


**BurstableMemory**


**Processor** **vCPUs CPU**


**Threads Accelerat**


**Accelerat**

|type|Col2|(GiB)|Col4|Col5|cores|per core|ors|or memor|
|---|---|---|---|---|---|---|---|---|
|m6idn.2xl arge|✗|32.00|Intel Xeon Ice Lake|8|4|2|✗|✗|
|m6idn.4xl arge|✗|64.00|Intel Xeon Ice Lake|16|8|2|✗|✗|
|m6idn.8xl arge|✗|128.00|Intel Xeon Ice Lake|32|16|2|✗|✗|
|m6idn.12x large|✗|192.00|Intel Xeon Ice Lake|48|24|2|✗|✗|
|m6idn.16x large|✗|256.00|Intel Xeon Ice Lake|64|32|2|✗|✗|
|m6idn.24x large|✗|384.00|Intel Xeon Ice Lake|96|48|2|✗|✗|
|m6idn.32x large|✗|512.00|Intel Xeon Ice Lake|128|64|2|✗|✗|
|m6idn.metal|✗|512.00|Intel Xeon Ice Lake|128|64|2|✗|✗|
|M6in|||||||||
|m6in.large|✗|8.00|Intel Xeon Ice Lake|2|1|2|✗|✗|
|m6in.xlarge|✗|16.00|Intel Xeon Ice Lake|4|2|2|✗|✗|
|m6in.2xla rge|✗|32.00|Intel Xeon Ice Lake|8|4|2|✗|✗|


Performance specifications 26


-----

**Instance**


**BurstableMemory**


**Processor** **vCPUs CPU**


**Threads Accelerat**


**Accelerat**

|type|Col2|(GiB)|Col4|Col5|cores|per core|ors|or memor|
|---|---|---|---|---|---|---|---|---|
|m6in.4xla rge|✗|64.00|Intel Xeon Ice Lake|16|8|2|✗|✗|
|m6in.8xla rge|✗|128.00|Intel Xeon Ice Lake|32|16|2|✗|✗|
|m6in.12xl arge|✗|192.00|Intel Xeon Ice Lake|48|24|2|✗|✗|
|m6in.16xl arge|✗|256.00|Intel Xeon Ice Lake|64|32|2|✗|✗|
|m6in.24xl arge|✗|384.00|Intel Xeon Ice Lake|96|48|2|✗|✗|
|m6in.32xl arge|✗|512.00|Intel Xeon Ice Lake|128|64|2|✗|✗|
|m6in.metal|✗|512.00|Intel Xeon Ice Lake|128|64|2|✗|✗|
|M7a|||||||||
|m7a.mediu m|✗|4.00|AMD EPYC 9R14|1|1|1|✗|✗|
|m7a.large|✗|8.00|AMD EPYC 9R14|2|2|1|✗|✗|
|m7a.xlarge|✗|16.00|AMD EPYC 9R14|4|4|1|✗|✗|
|m7a.2xlarge|✗|32.00|AMD EPYC 9R14|8|8|1|✗|✗|


Performance specifications 27


-----

**Instance**


**BurstableMemory**


**Processor** **vCPUs CPU**


**Threads Accelerat**


**Accelerat**

|type|Col2|(GiB)|Col4|Col5|cores|per core|ors|or memor|
|---|---|---|---|---|---|---|---|---|
|m7a.4xlarge|✗|64.00|AMD EPYC 9R14|16|16|1|✗|✗|
|m7a.8xlarge|✗|128.00|AMD EPYC 9R14|32|32|1|✗|✗|
|m7a.12xla rge|✗|192.00|AMD EPYC 9R14|48|48|1|✗|✗|
|m7a.16xla rge|✗|256.00|AMD EPYC 9R14|64|64|1|✗|✗|
|m7a.24xla rge|✗|384.00|AMD EPYC 9R14|96|96|1|✗|✗|
|m7a.32xla rge|✗|512.00|AMD EPYC 9R14|128|128|1|✗|✗|
|m7a.48xla rge|✗|768.00|AMD EPYC 9R14|192|192|1|✗|✗|
|m7a.metal -48xl|✗|768.00|AMD EPYC 9R14|192|192|1|✗|✗|
|M7g|||||||||
|m7g.mediu m|✗|4.00|AWS Graviton3 Processor|1|1|1|✗|✗|
|m7g.large|✗|8.00|AWS Graviton3 Processor|2|2|1|✗|✗|


Performance specifications 28


-----

**Instance**


**BurstableMemory**


**Processor** **vCPUs CPU**


**Threads Accelerat**


**Accelerat**

|type|Col2|(GiB)|Col4|Col5|cores|per core|ors|or memor|
|---|---|---|---|---|---|---|---|---|
|m7g.xlarge|✗|16.00|AWS Graviton3 Processor|4|4|1|✗|✗|
|m7g.2xlarge|✗|32.00|AWS Graviton3 Processor|8|8|1|✗|✗|
|m7g.4xlarge|✗|64.00|AWS Graviton3 Processor|16|16|1|✗|✗|
|m7g.8xlarge|✗|128.00|AWS Graviton3 Processor|32|32|1|✗|✗|
|m7g.12xla rge|✗|192.00|AWS Graviton3 Processor|48|48|1|✗|✗|
|m7g.16xla rge|✗|256.00|AWS Graviton3 Processor|64|64|1|✗|✗|
|m7g.metal|✗|256.00|AWS Graviton3 Processor|64|64|1|✗|✗|
|M7gd|||||||||
|m7gd.medi um|✗|4.00|AWS Graviton3 Processor|1|1|1|✗|✗|


Performance specifications 29


-----

**Instance**


**BurstableMemory**


**Processor** **vCPUs CPU**


**Threads Accelerat**


**Accelerat**

|type|Col2|(GiB)|Col4|Col5|cores|per core|ors|or memor|
|---|---|---|---|---|---|---|---|---|
|m7gd.large|✗|8.00|AWS Graviton3 Processor|2|2|1|✗|✗|
|m7gd.xlarge|✗|16.00|AWS Graviton3 Processor|4|4|1|✗|✗|
|m7gd.2xla rge|✗|32.00|AWS Graviton3 Processor|8|8|1|✗|✗|
|m7gd.4xla rge|✗|64.00|AWS Graviton3 Processor|16|16|1|✗|✗|
|m7gd.8xla rge|✗|128.00|AWS Graviton3 Processor|32|32|1|✗|✗|
|m7gd.12xl arge|✗|192.00|AWS Graviton3 Processor|48|48|1|✗|✗|
|m7gd.16xl arge|✗|256.00|AWS Graviton3 Processor|64|64|1|✗|✗|
|m7gd.metal|✗|256.00|AWS Graviton3 Processor|64|64|1|✗|✗|
|M7i|||||||||


Performance specifications 30


-----

**Instance**


**BurstableMemory**


**Processor** **vCPUs CPU**


**Threads Accelerat**


**Accelerat**

|type|Col2|(GiB)|Col4|Col5|cores|per core|ors|or memor|
|---|---|---|---|---|---|---|---|---|
|m7i.large|✗|8.00|Intel Xeon Sapphire Rapids|2|1|2|✗|✗|
|m7i.xlarge|✗|16.00|Intel Xeon Sapphire Rapids|4|2|2|✗|✗|
|m7i.2xlarge|✗|32.00|Intel Xeon Sapphire Rapids|8|4|2|✗|✗|
|m7i.4xlarge|✗|64.00|Intel Xeon Sapphire Rapids|16|8|2|✗|✗|
|m7i.8xlarge|✗|128.00|Intel Xeon Sapphire Rapids|32|16|2|✗|✗|
|m7i.12xla rge|✗|192.00|Intel Xeon Sapphire Rapids|48|24|2|✗|✗|
|m7i.16xla rge|✗|256.00|Intel Xeon Sapphire Rapids|64|32|2|✗|✗|
|m7i.24xla rge|✗|384.00|Intel Xeon Sapphire Rapids|96|48|2|✗|✗|
|m7i.48xla rge|✗|768.00|Intel Xeon Sapphire Rapids|192|96|2|✗|✗|


Performance specifications 31


-----

**Instance**


**BurstableMemory**


**Processor** **vCPUs CPU**


**Threads Accelerat**


**Accelerat**

|type|Col2|(GiB)|Col4|Col5|cores|per core|ors|or memor|
|---|---|---|---|---|---|---|---|---|
|m7i.metal -24xl|✗|384.00|Intel Xeon Sapphire Rapids|96|48|2|✗|✗|
|m7i.metal -48xl|✗|768.00|Intel Xeon Sapphire Rapids|192|96|2|✗|✗|
|M7i-flex|||||||||
|m7i-flex. large|✗|8.00|Intel Xeon Sapphire Rapids|2|1|2|✗|✗|
|m7i-flex. xlarge|✗|16.00|Intel Xeon Sapphire Rapids|4|2|2|✗|✗|
|m7i-flex. 2xlarge|✗|32.00|Intel Xeon Sapphire Rapids|8|4|2|✗|✗|
|m7i-flex. 4xlarge|✗|64.00|Intel Xeon Sapphire Rapids|16|8|2|✗|✗|
|m7i-flex. 8xlarge|✗|128.00|Intel Xeon Sapphire Rapids|32|16|2|✗|✗|
|Mac1|||||||||
|mac1.metal|✗|32.00|Intel Core i7-8700B|12|6|2|✗|✗|


Performance specifications 32


-----

|Mac2|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
|mac2.metal|✗|16.00|Apple M1 chip with 8- core CPU|8|4|2|✗|✗|
|Mac2-m1ultra|||||||||
|mac2-m1ul tra.metal|✗|128.00|Apple M1 Ultra with 20‑core CPU|20|20|1|✗|✗|
|Mac2-m2|||||||||
|mac2-m2.m etal|✗|24.00|Apple M2 with 8 ‑core CPU|8|8|1|✗|✗|
|Mac2-m2pro|||||||||
|mac2-m2pr o.metal|✗|32.00|Apple M2 Pro with 1 2‑core CPU|12|12|1|✗|✗|
|T2|||||||||
|t2.nano|✓|0.50|Intel Xeon Family|1|1|1|✗|✗|
|t2.micro|✓|1.00|Intel Xeon Family|1|1|1|✗|✗|
|t2.small|✓|2.00|Intel Xeon Family|1|1|1|✗|✗|


**Instance** **BurstableMemory Processor** **vCPUs CPU** **Threads Accelerat** **Accelerat**
**type** **(GiB)** **cores** **per** **ors** **or**

**core** **memory**

Performance specifications 33


-----

**Instance**


**BurstableMemory**


**Processor** **vCPUs CPU**


**Threads Accelerat**


**Accelerat**

|type|Col2|(GiB)|Col4|Col5|cores|per core|ors|or memor|
|---|---|---|---|---|---|---|---|---|
|t2.medium|✓|4.00|Intel Broadwell E5-2686v4|2|2|1|✗|✗|
|t2.large|✓|8.00|Intel Broadwell E5-2686v4|2|2|1|✗|✗|
|t2.xlarge|✓|16.00|Intel Broadwell E5-2686v4|4|4|1|✗|✗|
|t2.2xlarge|✓|32.00|Intel Broadwell E5-2686v4|8|8|1|✗|✗|
|T3|||||||||
|t3.nano|✓|0.50|Intel Skylake P-8175|2|1|2|✗|✗|
|t3.micro|✓|1.00|Intel Skylake P-8175|2|1|2|✗|✗|
|t3.small|✓|2.00|Intel Skylake P-8175|2|1|2|✗|✗|
|t3.medium|✓|4.00|Intel Skylake P-8175|2|1|2|✗|✗|
|t3.large|✓|8.00|Intel Skylake P-8175|2|1|2|✗|✗|
|t3.xlarge|✓|16.00|Intel Skylake P-8175|4|2|2|✗|✗|


Performance specifications 34


-----

**Instance**


**BurstableMemory**


**Processor** **vCPUs CPU**


**Threads Accelerat**


**Accelerat**

|type|Col2|(GiB)|Col4|Col5|cores|per core|ors|or memor|
|---|---|---|---|---|---|---|---|---|
|t3.2xlarge|✓|32.00|Intel Skylake P-8175|8|4|2|✗|✗|
|T3a|||||||||
|t3a.nano|✓|0.50|AMD EPYC 7571|2|1|2|✗|✗|
|t3a.micro|✓|1.00|AMD EPYC 7571|2|1|2|✗|✗|
|t3a.small|✓|2.00|AMD EPYC 7571|2|1|2|✗|✗|
|t3a.medium|✓|4.00|AMD EPYC 7571|2|1|2|✗|✗|
|t3a.large|✓|8.00|AMD EPYC 7571|2|1|2|✗|✗|
|t3a.xlarge|✓|16.00|AMD EPYC 7571|4|2|2|✗|✗|
|t3a.2xlarge|✓|32.00|AMD EPYC 7571|8|4|2|✗|✗|
|T4g|||||||||
|t4g.nano|✓|0.50|AWS Graviton2 Processor|2|2|1|✗|✗|
|t4g.micro|✓|1.00|AWS Graviton2 Processor|2|2|1|✗|✗|


Performance specifications 35


-----

**Instance**


**BurstableMemory**


**Processor** **vCPUs CPU**


**Threads Accelerat**


**Accelerat**

|type|Col2|(GiB)|Col4|Col5|cores|per core|ors|or memor|
|---|---|---|---|---|---|---|---|---|
|t4g.small|✓|2.00|AWS Graviton2 Processor|2|2|1|✗|✗|
|t4g.medium|✓|4.00|AWS Graviton2 Processor|2|2|1|✗|✗|
|t4g.large|✓|8.00|AWS Graviton2 Processor|2|2|1|✗|✗|
|t4g.xlarge|✓|16.00|AWS Graviton2 Processor|4|4|1|✗|✗|
|t4g.2xlarge|✓|32.00|AWS Graviton2 Processor|8|8|1|✗|✗|


#### Network specifications

|Instance type|Baseline / Burst bandwidth (Gbps)|EFA|ENA|ENA Express|Network cards|Max. network interface s|IP addresses per interface|IPv6|
|---|---|---|---|---|---|---|---|---|
|M5|||||||||
|1 m5.large|0.75 / 10.0|✗|✓|✗|1|3|10|✓|
|1 m5.xlarge|1.25 / 10.0|✗|✓|✗|1|4|15|✓|



Network specifications 36


-----

|Col1|bandwidth (Gbps)|Col3|Col4|Col5|Col6|interface s|per interface|Col9|
|---|---|---|---|---|---|---|---|---|
|1 m5.2xlarge|2.5 / 10.0|✗|✓|✗|1|4|15|✓|
|1 m5.4xlarge|5.0 / 10.0|✗|✓|✗|1|8|30|✓|
|m5.8xlarge|10 Gigabit|✗|✓|✗|1|8|30|✓|
|m5.12xlarge|12 Gigabit|✗|✓|✗|1|8|30|✓|
|m5.16xlarge|20 Gigabit|✗|✓|✗|1|15|50|✓|
|m5.24xlarge|25 Gigabit|✗|✓|✗|1|15|50|✓|
|m5.metal|25 Gigabit|✗|✓|✗|1|15|50|✓|
|M5a|||||||||
|1 m5a.large|0.75 / 10.0|✗|✓|✗|1|3|10|✓|
|1 m5a.xlarge|1.25 / 10.0|✗|✓|✗|1|4|15|✓|
|1 m5a.2xlarge|2.5 / 10.0|✗|✓|✗|1|4|15|✓|
|1 m5a.4xlarge|5.0 / 10.0|✗|✓|✗|1|8|30|✓|
|1 m5a.8xlarge|7.5 / 10.0|✗|✓|✗|1|8|30|✓|
|m5a.12xlarge|10 Gigabit|✗|✓|✗|1|8|30|✓|
|m5a.16xlarge|12 Gigabit|✗|✓|✗|1|15|50|✓|
|m5a.24xlarge|20 Gigabit|✗|✓|✗|1|15|50|✓|
|M5ad|||||||||
|1 m5ad.large|0.75 / 10.0|✗|✓|✗|1|3|10|✓|
|1 m5ad.xlarge|1.25 / 10.0|✗|✓|✗|1|4|15|✓|


**Instance type** **Baseline /** **EFA** **ENA** **ENA** **Network** **Max.** **IP** **IPv6**
**Burst** **Express** **cards** **network** **addresses**
**bandwidth** **interface** **per**
**(Gbps)** **s** **interface**


Network specifications 37


-----

|Col1|bandwidth (Gbps)|Col3|Col4|Col5|Col6|interface s|per interface|Col9|
|---|---|---|---|---|---|---|---|---|
|m5ad.2xlarge 1|2.5 / 10.0|✗|✓|✗|1|4|15|✓|
|m5ad.4xlarge 1|5.0 / 10.0|✗|✓|✗|1|8|30|✓|
|m5ad.8xlarge 1|7.5 / 10.0|✗|✓|✗|1|8|30|✓|
|m5ad.12xl arge|10 Gigabit|✗|✓|✗|1|8|30|✓|
|m5ad.16xl arge|12 Gigabit|✗|✓|✗|1|15|50|✓|
|m5ad.24xl arge|20 Gigabit|✗|✓|✗|1|15|50|✓|
|M5d|||||||||
|1 m5d.large|0.75 / 10.0|✗|✓|✗|1|3|10|✓|
|1 m5d.xlarge|1.25 / 10.0|✗|✓|✗|1|4|15|✓|
|1 m5d.2xlarge|2.5 / 10.0|✗|✓|✗|1|4|15|✓|
|1 m5d.4xlarge|5.0 / 10.0|✗|✓|✗|1|8|30|✓|
|m5d.8xlarge|10 Gigabit|✗|✓|✗|1|8|30|✓|
|m5d.12xlarge|12 Gigabit|✗|✓|✗|1|8|30|✓|
|m5d.16xlarge|20 Gigabit|✗|✓|✗|1|15|50|✓|
|m5d.24xlarge|25 Gigabit|✗|✓|✗|1|15|50|✓|


**Instance type** **Baseline /** **EFA** **ENA** **ENA** **Network** **Max.** **IP** **IPv6**
**Burst** **Express** **cards** **network** **addresses**
**bandwidth** **interface** **per**
**(Gbps)** **s** **interface**


Network specifications 38


-----

|Col1|bandwidth (Gbps)|Col3|Col4|Col5|Col6|interface s|per interface|Col9|
|---|---|---|---|---|---|---|---|---|
|m5d.metal|25 Gigabit|✗|✓|✗|1|15|50|✓|
|M5dn|||||||||
|1 m5dn.large|2.1 / 25.0|✗|✓|✗|1|3|10|✓|
|1 m5dn.xlarge|4.1 / 25.0|✗|✓|✗|1|4|15|✓|
|m5dn.2xlarge 1|8.125 / 25.0|✗|✓|✗|1|4|15|✓|
|m5dn.4xlarge 1|16.25 / 25.0|✗|✓|✗|1|8|30|✓|
|m5dn.8xlarge|25 Gigabit|✗|✓|✗|1|8|30|✓|
|m5dn.12xl arge|50 Gigabit|✗|✓|✗|1|8|30|✓|
|m5dn.16xl arge|75 Gigabit|✗|✓|✗|1|15|50|✓|
|m5dn.24xl arge|100 Gigabit|✓|✓|✗|1|15|50|✓|
|m5dn.metal|100 Gigabit|✓|✓|✗|1|15|50|✓|
|M5n|||||||||
|1 m5n.large|2.1 / 25.0|✗|✓|✗|1|3|10|✓|
|1 m5n.xlarge|4.1 / 25.0|✗|✓|✗|1|4|15|✓|
|1 m5n.2xlarge|8.125 / 25.0|✗|✓|✗|1|4|15|✓|
|1 m5n.4xlarge|16.25 / 25.0|✗|✓|✗|1|8|30|✓|


**Instance type** **Baseline /** **EFA** **ENA** **ENA** **Network** **Max.** **IP** **IPv6**
**Burst** **Express** **cards** **network** **addresses**
**bandwidth** **interface** **per**
**(Gbps)** **s** **interface**


Network specifications 39


-----

|Col1|bandwidth (Gbps)|Col3|Col4|Col5|Col6|interface s|per interface|Col9|
|---|---|---|---|---|---|---|---|---|
|m5n.8xlarge|25 Gigabit|✗|✓|✗|1|8|30|✓|
|m5n.12xlarge|50 Gigabit|✗|✓|✗|1|8|30|✓|
|m5n.16xlarge|75 Gigabit|✗|✓|✗|1|15|50|✓|
|m5n.24xlarge|100 Gigabit|✓|✓|✗|1|15|50|✓|
|m5n.metal|100 Gigabit|✓|✓|✗|1|15|50|✓|
|M5zn|||||||||
|1 m5zn.large|3.0 / 25.0|✗|✓|✗|1|3|10|✓|
|1 m5zn.xlarge|5.0 / 25.0|✗|✓|✗|1|4|15|✓|
|m5zn.2xlarge 1|10.0 / 25.0|✗|✓|✗|1|4|15|✓|
|m5zn.3xlarge 1|15.0 / 25.0|✗|✓|✗|1|8|30|✓|
|m5zn.6xlarge|50 Gigabit|✗|✓|✗|1|8|30|✓|
|m5zn.12xl arge|100 Gigabit|✓|✓|✗|1|15|50|✓|
|m5zn.metal|100 Gigabit|✓|✓|✗|1|15|50|✓|
|M6a|||||||||
|1 m6a.large|0.781 / 12.5|✗|✓|✗|1|3|10|✓|
|1 m6a.xlarge|1.562 / 12.5|✗|✓|✗|1|4|15|✓|
|1 m6a.2xlarge|3.125 / 12.5|✗|✓|✗|1|4|15|✓|


**Instance type** **Baseline /** **EFA** **ENA** **ENA** **Network** **Max.** **IP** **IPv6**
**Burst** **Express** **cards** **network** **addresses**
**bandwidth** **interface** **per**
**(Gbps)** **s** **interface**


Network specifications 40


-----

|Col1|bandwidth (Gbps)|Col3|Col4|Col5|Col6|interface s|per interface|Col9|
|---|---|---|---|---|---|---|---|---|
|1 m6a.4xlarge|6.25 / 12.5|✗|✓|✗|1|8|30|✓|
|m6a.8xlarge|12.5 Gigabit|✗|✓|✗|1|8|30|✓|
|m6a.12xlarge|18.75 Gigabit|✗|✓|✓|1|8|30|✓|
|m6a.16xlarge|25 Gigabit|✗|✓|✓|1|15|50|✓|
|m6a.24xlarge|37.5 Gigabit|✗|✓|✓|1|15|50|✓|
|m6a.32xlarge|50 Gigabit|✗|✓|✓|1|15|50|✓|
|m6a.48xlarge|50 Gigabit|✓|✓|✓|1|15|50|✓|
|m6a.metal|50 Gigabit|✓|✓|✓|1|15|50|✓|
|M6g|||||||||
|m6g.medium 1|0.5 / 10.0|✗|✓|✗|1|2|4|✓|
|1 m6g.large|0.75 / 10.0|✗|✓|✗|1|3|10|✓|
|1 m6g.xlarge|1.25 / 10.0|✗|✓|✗|1|4|15|✓|
|1 m6g.2xlarge|2.5 / 10.0|✗|✓|✗|1|4|15|✓|
|1 m6g.4xlarge|5.0 / 10.0|✗|✓|✗|1|8|30|✓|
|m6g.8xlarge|12 Gigabit|✗|✓|✗|1|8|30|✓|
|m6g.12xlarge|20 Gigabit|✗|✓|✗|1|8|30|✓|
|m6g.16xlarge|25 Gigabit|✗|✓|✗|1|15|50|✓|
|m6g.metal|25 Gigabit|✗|✓|✗|1|15|50|✓|


**Instance type** **Baseline /** **EFA** **ENA** **ENA** **Network** **Max.** **IP** **IPv6**
**Burst** **Express** **cards** **network** **addresses**
**bandwidth** **interface** **per**
**(Gbps)** **s** **interface**


Network specifications 41


-----

|Instance type Baseline / Burst bandwidth (Gbps) EFA ENA ENA Express Network cards Max. network interface s IP addresses per interface IPv6|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
|M6gd|||||||||
|m6gd.medi 1 um|0.5 / 10.0|✗|✓|✗|1|2|4|✓|
|1 m6gd.large|0.75 / 10.0|✗|✓|✗|1|3|10|✓|
|1 m6gd.xlarge|1.25 / 10.0|✗|✓|✗|1|4|15|✓|
|m6gd.2xlarge 1|2.5 / 10.0|✗|✓|✗|1|4|15|✓|
|m6gd.4xlarge 1|5.0 / 10.0|✗|✓|✗|1|8|30|✓|
|m6gd.8xlarge|12 Gigabit|✗|✓|✗|1|8|30|✓|
|m6gd.12xl arge|20 Gigabit|✗|✓|✗|1|8|30|✓|
|m6gd.16xl arge|25 Gigabit|✗|✓|✗|1|15|50|✓|
|m6gd.metal|25 Gigabit|✗|✓|✗|1|15|50|✓|
|M6i|||||||||
|1 m6i.large|0.781 / 12.5|✗|✓|✗|1|3|10|✓|
|1 m6i.xlarge|1.562 / 12.5|✗|✓|✗|1|4|15|✓|
|1 m6i.2xlarge|3.125 / 12.5|✗|✓|✗|1|4|15|✓|
|1 m6i.4xlarge|6.25 / 12.5|✗|✓|✗|1|8|30|✓|
|m6i.8xlarge|12.5 Gigabit|✗|✓|✓|1|8|30|✓|


Network specifications 42


-----

|Col1|bandwidth (Gbps)|Col3|Col4|Col5|Col6|interface s|per interface|Col9|
|---|---|---|---|---|---|---|---|---|
|m6i.12xlarge|18.75 Gigabit|✗|✓|✓|1|8|30|✓|
|m6i.16xlarge|25 Gigabit|✗|✓|✓|1|15|50|✓|
|m6i.24xlarge|37.5 Gigabit|✗|✓|✓|1|15|50|✓|
|m6i.32xlarge|50 Gigabit|✓|✓|✓|1|15|50|✓|
|m6i.metal|50 Gigabit|✓|✓|✓|1|15|50|✓|
|M6id|||||||||
|1 m6id.large|0.781 / 12.5|✗|✓|✗|1|3|10|✓|
|1 m6id.xlarge|1.562 / 12.5|✗|✓|✗|1|4|15|✓|
|1 m6id.2xlarge|3.125 / 12.5|✗|✓|✗|1|4|15|✓|
|1 m6id.4xlarge|6.25 / 12.5|✗|✓|✗|1|8|30|✓|
|m6id.8xlarge|12.5 Gigabit|✗|✓|✓|1|8|30|✓|
|m6id.12xlarge|18.75 Gigabit|✗|✓|✓|1|8|30|✓|
|m6id.16xlarge|25 Gigabit|✗|✓|✓|1|15|50|✓|
|m6id.24xlarge|37.5 Gigabit|✗|✓|✓|1|15|50|✓|
|m6id.32xlarge|50 Gigabit|✓|✓|✓|1|15|50|✓|
|m6id.metal|50 Gigabit|✓|✓|✓|1|15|50|✓|
|M6idn|||||||||
|1 m6idn.large|3.125 / 25.0|✗|✓|✗|1|3|10|✓|


**Instance type** **Baseline /** **EFA** **ENA** **ENA** **Network** **Max.** **IP** **IPv6**
**Burst** **Express** **cards** **network** **addresses**
**bandwidth** **interface** **per**
**(Gbps)** **s** **interface**


Network specifications 43


-----

|Col1|bandwidth (Gbps)|Col3|Col4|Col5|Col6|interface s|per interface|Col9|
|---|---|---|---|---|---|---|---|---|
|m6idn.xlarge 1|6.25 / 30.0|✗|✓|✗|1|4|15|✓|
|m6idn.2xlarge 1|12.5 / 40.0|✗|✓|✗|1|4|15|✓|
|m6idn.4xlarge 1|25.0 / 50.0|✗|✓|✗|1|8|30|✓|
|m6idn.8xlarge|50 Gigabit|✗|✓|✗|1|8|30|✓|
|m6idn.12x large|75 Gigabit|✗|✓|✗|1|8|30|✓|
|m6idn.16x large|100 Gigabit|✗|✓|✗|1|15|50|✓|
|m6idn.24x large|150 Gigabit|✗|✓|✗|1|15|50|✓|
|m6idn.32x large|200 Gigabit|✓|✓|✗|2|16|50|✓|
|m6idn.metal|200 Gigabit|✓|✓|✗|2|16|50|✓|
|M6in|||||||||
|1 m6in.large|3.125 / 25.0|✗|✓|✗|1|3|10|✓|
|1 m6in.xlarge|6.25 / 30.0|✗|✓|✗|1|4|15|✓|
|1 m6in.2xlarge|12.5 / 40.0|✗|✓|✗|1|4|15|✓|
|1 m6in.4xlarge|25.0 / 50.0|✗|✓|✗|1|8|30|✓|


**Instance type** **Baseline /** **EFA** **ENA** **ENA** **Network** **Max.** **IP** **IPv6**
**Burst** **Express** **cards** **network** **addresses**
**bandwidth** **interface** **per**
**(Gbps)** **s** **interface**


Network specifications 44


-----

|Col1|bandwidth (Gbps)|Col3|Col4|Col5|Col6|interface s|per interface|Col9|
|---|---|---|---|---|---|---|---|---|
|m6in.8xlarge|50 Gigabit|✗|✓|✗|1|8|30|✓|
|m6in.12xlarge|75 Gigabit|✗|✓|✗|1|8|30|✓|
|m6in.16xlarge|100 Gigabit|✗|✓|✗|1|15|50|✓|
|m6in.24xlarge|150 Gigabit|✗|✓|✗|1|15|50|✓|
|m6in.32xlarge|200 Gigabit|✓|✓|✗|2|16|50|✓|
|m6in.metal|200 Gigabit|✓|✓|✗|2|16|50|✓|
|M7a|||||||||
|m7a.medium 1|0.39 / 12.5|✗|✓|✗|1|2|4|✓|
|1 m7a.large|0.781 / 12.5|✗|✓|✗|1|3|10|✓|
|1 m7a.xlarge|1.562 / 12.5|✗|✓|✗|1|4|15|✓|
|1 m7a.2xlarge|3.125 / 12.5|✗|✓|✗|1|4|15|✓|
|1 m7a.4xlarge|6.25 / 12.5|✗|✓|✗|1|8|30|✓|
|m7a.8xlarge|12.5 Gigabit|✗|✓|✗|1|8|30|✓|
|m7a.12xlarge|18.75 Gigabit|✗|✓|✗|1|8|30|✓|
|m7a.16xlarge|25 Gigabit|✗|✓|✗|1|15|50|✓|
|m7a.24xlarge|37.5 Gigabit|✗|✓|✗|1|15|50|✓|
|m7a.32xlarge|50 Gigabit|✗|✓|✗|1|15|50|✓|
|m7a.48xlarge|50 Gigabit|✓|✓|✗|1|15|50|✓|


**Instance type** **Baseline /** **EFA** **ENA** **ENA** **Network** **Max.** **IP** **IPv6**
**Burst** **Express** **cards** **network** **addresses**
**bandwidth** **interface** **per**
**(Gbps)** **s** **interface**


Network specifications 45


-----

|Col1|bandwidth (Gbps)|Col3|Col4|Col5|Col6|interface s|per interface|Col9|
|---|---|---|---|---|---|---|---|---|
|m7a.metal -48xl|50 Gigabit|✓|✓|✗|1|15|50|✓|
|M7g|||||||||
|m7g.medium 1|0.52 / 12.5|✗|✓|✗|1|2|4|✓|
|1 m7g.large|0.937 / 12.5|✗|✓|✗|1|3|10|✓|
|1 m7g.xlarge|1.876 / 12.5|✗|✓|✗|1|4|15|✓|
|1 m7g.2xlarge|3.75 / 15.0|✗|✓|✗|1|4|15|✓|
|1 m7g.4xlarge|7.5 / 15.0|✗|✓|✗|1|8|30|✓|
|m7g.8xlarge|15 Gigabit|✗|✓|✗|1|8|30|✓|
|m7g.12xlarge|22.5 Gigabit|✗|✓|✓|1|8|30|✓|
|m7g.16xlarge|30 Gigabit|✓|✓|✓|1|15|50|✓|
|m7g.metal|30 Gigabit|✓|✓|✓|1|15|50|✓|
|M7gd|||||||||
|m7gd.medi 1 um|0.52 / 12.5|✗|✓|✗|1|2|4|✓|
|1 m7gd.large|0.937 / 12.5|✗|✓|✗|1|3|10|✓|
|1 m7gd.xlarge|1.876 / 12.5|✗|✓|✗|1|4|15|✓|
|m7gd.2xlarge 1|3.75 / 15.0|✗|✓|✗|1|4|15|✓|


**Instance type** **Baseline /** **EFA** **ENA** **ENA** **Network** **Max.** **IP** **IPv6**
**Burst** **Express** **cards** **network** **addresses**
**bandwidth** **interface** **per**
**(Gbps)** **s** **interface**


Network specifications 46


-----

|Col1|bandwidth (Gbps)|Col3|Col4|Col5|Col6|interface s|per interface|Col9|
|---|---|---|---|---|---|---|---|---|
|m7gd.4xlarge 1|7.5 / 15.0|✗|✓|✗|1|8|30|✓|
|m7gd.8xlarge|15 Gigabit|✗|✓|✗|1|8|30|✓|
|m7gd.12xl arge|22.5 Gigabit|✗|✓|✓|1|8|30|✓|
|m7gd.16xl arge|30 Gigabit|✓|✓|✓|1|15|50|✓|
|m7gd.metal|30 Gigabit|✓|✓|✓|1|15|50|✓|
|M7i|||||||||
|1 m7i.large|0.781 / 12.5|✗|✓|✗|1|3|10|✓|
|1 m7i.xlarge|1.562 / 12.5|✗|✓|✗|1|4|15|✓|
|1 m7i.2xlarge|3.125 / 12.5|✗|✓|✗|1|4|15|✓|
|1 m7i.4xlarge|6.25 / 12.5|✗|✓|✗|1|8|30|✓|
|m7i.8xlarge|12.5 Gigabit|✗|✓|✗|1|8|30|✓|
|m7i.12xlarge|18.75 Gigabit|✗|✓|✓|1|8|30|✓|
|m7i.16xlarge|25 Gigabit|✗|✓|✓|1|15|50|✓|
|m7i.24xlarge|37.5 Gigabit|✗|✓|✓|1|15|50|✓|
|m7i.48xlarge|50 Gigabit|✓|✓|✓|1|15|50|✓|
|m7i.metal -24xl|37.5 Gigabit|✗|✓|✓|1|15|50|✓|


**Instance type** **Baseline /** **EFA** **ENA** **ENA** **Network** **Max.** **IP** **IPv6**
**Burst** **Express** **cards** **network** **addresses**
**bandwidth** **interface** **per**
**(Gbps)** **s** **interface**


Network specifications 47


-----

|Col1|bandwidth (Gbps)|Col3|Col4|Col5|Col6|interface s|per interface|Col9|
|---|---|---|---|---|---|---|---|---|
|m7i.metal -48xl|50 Gigabit|✓|✓|✓|1|15|50|✓|
|M7i-flex|||||||||
|m7i-flex.large 1|0.39 / 12.5|✗|✓|✗|1|3|10|✓|
|m7i-flex. 1 xlarge|0.781 / 12.5|✗|✓|✗|1|4|15|✓|
|m7i-flex. 1 2xlarge|1.562 / 12.5|✗|✓|✗|1|4|15|✓|
|m7i-flex. 1 4xlarge|3.125 / 12.5|✗|✓|✗|1|8|30|✓|
|m7i-flex. 1 8xlarge|6.25 / 12.5|✗|✓|✗|1|8|30|✓|
|Mac1|||||||||
|mac1.metal|25 Gigabit|✗|✓|✗|1|8|30|✓|
|Mac2|||||||||
|mac2.metal|10 Gigabit|✗|✓|✗|1|8|30|✓|
|Mac2-m1ultra|||||||||
|mac2-m1ul tra.metal|10 Gigabit|✗|✓|✗|1|8|30|✓|
|Mac2-m2|||||||||


**Instance type** **Baseline /** **EFA** **ENA** **ENA** **Network** **Max.** **IP** **IPv6**
**Burst** **Express** **cards** **network** **addresses**
**bandwidth** **interface** **per**
**(Gbps)** **s** **interface**


Network specifications 48


-----

|Col1|bandwidth (Gbps)|Col3|Col4|Col5|Col6|interface s|per interface|Col9|
|---|---|---|---|---|---|---|---|---|
|mac2-m2.m etal|10 Gigabit|✗|✓|✗|1|8|30|✓|
|Mac2-m2pro|||||||||
|mac2-m2pr o.metal|10 Gigabit|✗|✓|✗|1|8|30|✓|
|T2|||||||||
|t2.nano|Low to Moderate|✗|✗|✗|1|2|2|✓|
|t2.micro|Low to Moderate|✗|✗|✗|1|2|2|✓|
|t2.small|Low to Moderate|✗|✗|✗|1|3|4|✓|
|t2.medium|Low to Moderate|✗|✗|✗|1|3|6|✓|
|t2.large|Low to Moderate|✗|✗|✗|1|3|12|✓|
|t2.xlarge|Moderate|✗|✗|✗|1|3|15|✓|
|t2.2xlarge|Moderate|✗|✗|✗|1|3|15|✓|
|T3|||||||||
|1 t3.nano|0.032 / 5.0|✗|✓|✗|1|2|2|✓|
|1 t3.micro|0.064 / 5.0|✗|✓|✗|1|2|2|✓|


**Instance type** **Baseline /** **EFA** **ENA** **ENA** **Network** **Max.** **IP** **IPv6**
**Burst** **Express** **cards** **network** **addresses**
**bandwidth** **interface** **per**
**(Gbps)** **s** **interface**


Network specifications 49


-----

|Col1|bandwidth (Gbps)|Col3|Col4|Col5|Col6|interface s|per interface|Col9|
|---|---|---|---|---|---|---|---|---|
|1 t3.small|0.128 / 5.0|✗|✓|✗|1|3|4|✓|
|1 t3.medium|0.256 / 5.0|✗|✓|✗|1|3|6|✓|
|1 t3.large|0.512 / 5.0|✗|✓|✗|1|3|12|✓|
|1 t3.xlarge|1.024 / 5.0|✗|✓|✗|1|4|15|✓|
|1 t3.2xlarge|2.048 / 5.0|✗|✓|✗|1|4|15|✓|
|T3a|||||||||
|1 t3a.nano|0.032 / 5.0|✗|✓|✗|1|2|2|✓|
|1 t3a.micro|0.064 / 5.0|✗|✓|✗|1|2|2|✓|
|1 t3a.small|0.128 / 5.0|✗|✓|✗|1|2|4|✓|
|1 t3a.medium|0.256 / 5.0|✗|✓|✗|1|3|6|✓|
|1 t3a.large|0.512 / 5.0|✗|✓|✗|1|3|12|✓|
|1 t3a.xlarge|1.024 / 5.0|✗|✓|✗|1|4|15|✓|
|1 t3a.2xlarge|2.048 / 5.0|✗|✓|✗|1|4|15|✓|
|T4g|||||||||
|1 t4g.nano|0.032 / 5.0|✗|✓|✗|1|2|2|✓|
|1 t4g.micro|0.064 / 5.0|✗|✓|✗|1|2|2|✓|
|1 t4g.small|0.128 / 5.0|✗|✓|✗|1|3|4|✓|
|1 t4g.medium|0.256 / 5.0|✗|✓|✗|1|3|6|✓|
|1 t4g.large|0.512 / 5.0|✗|✓|✗|1|3|12|✓|


**Instance type** **Baseline /** **EFA** **ENA** **ENA** **Network** **Max.** **IP** **IPv6**
**Burst** **Express** **cards** **network** **addresses**
**bandwidth** **interface** **per**
**(Gbps)** **s** **interface**


Network specifications 50


-----

|Col1|bandwidth (Gbps)|Col3|Col4|Col5|Col6|interface s|per interface|Col9|
|---|---|---|---|---|---|---|---|---|
|1 t4g.xlarge|1.024 / 5.0|✗|✓|✗|1|4|15|✓|
|1 t4g.2xlarge|2.048 / 5.0|✗|✓|✗|1|4|15|✓|


**Instance type** **Baseline /** **EFA** **ENA** **ENA** **Network** **Max.** **IP** **IPv6**
**Burst** **Express** **cards** **network** **addresses**
**bandwidth** **interface** **per**
**(Gbps)** **s** **interface**


**Note**

1
These instances have a baseline bandwidth and can use a network I/O credit mechanism
to burst beyond their baseline bandwidth on a best effort basis. Other instances types
[can sustain their maximum performance indefinitely. For more information, see instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-network-bandwidth.html)
[network bandwidth.](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-network-bandwidth.html)

For 32xlarge and metal instance types that support 200 Gbps, at least 2 ENIs, each
attached to a different network card, are required on the instance to achieve 200 Gbps
throughput. Each ENI attached to a network card can achieve a max of 170 Gbps.

#### Amazon EBS specifications

The following table indicates which instance types are Amazon EBS optimized by default and
which optionally support it. It also describes their EBS-optimized performance, including dedicated
bandwidth to Amazon EBS, the typical maximum aggregate throughput that can be achieved on
that dedicated connection with a streaming read workload and 128 KiB I/O size, and the maximum
IOPS the instance type can support when using a 16 KiB I/O size. Instance types not listed do not
support Amazon EBS optimization.

**Important**

An instance's EBS performance is bounded by the instance's performance limits, or
the aggregated performance of its attached volumes, whichever is smaller. To achieve
maximum EBS performance, an instance must have attached volumes that provide a
combined performance equal to or greater than the maximum instance performance. For

example, to achieve 80,000 IOPS for r6i.16xlarge, the instance must have at least 5

Amazon EBS specifications 51


-----

```
   gp3 volumes provisioned with 16,000 IOPS each (5 volumes x 16,000 IOPS = 80,000

```
IOPS).
We recommand that you choose an EBS–optimized instance type that provides more
dedicated Amazon EBS throughput than your application needs; otherwise, the connection
between Amazon EBS and Amazon EC2 can become a performance bottleneck.

|Instance type|Baseline / Maximum bandwidth (Mbps)|Baseline / Maximum throughput (MB/s, 128 KiB I/O)|Baseline / Maximum IOPS (16 KiB I/O)|NVMe|EBS optimization 2|
|---|---|---|---|---|---|
|M5||||||
|1 m5.large|650.00 / 4750.00|81.25 / 593.75|3600.00 / 18750.00|✓|default|
|1 m5.xlarge|1150.00 / 4750.00|143.75 / 593.75|6000.00 / 18750.00|✓|default|
|1 m5.2xlarge|2300.00 / 4750.00|287.50 / 593.75|12000.00 / 18750.00|✓|default|
|m5.4xlarge|4750.00|593.75|18750.00|✓|default|
|m5.8xlarge|6800.00|850.00|30000.00|✓|default|
|m5.12xlarge|9500.00|1187.50|40000.00|✓|default|
|m5.16xlarge|13600.00|1700.00|60000.00|✓|default|
|m5.24xlarge|19000.00|2375.00|80000.00|✓|default|
|m5.metal|19000.00|2375.00|80000.00|✓|default|
|M5a||||||



Amazon EBS specifications 52


-----

**Instance**


**Baseline /**


**Baseline /**


**Baseline /**


**NVMe** **EBS**

|type|Maximum bandwidth (Mbps)|Maximum throughput (MB/s, 128 KiB I/O)|Maximum IOPS (16 KiB I/O)|Col5|optimization 2|
|---|---|---|---|---|---|
|1 m5a.large|650.00 / 2880.00|81.25 / 360.00|3600.00 / 16000.00|✓|default|
|1 m5a.xlarge|1085.00 / 2880.00|135.62 / 360.00|6000.00 / 16000.00|✓|default|
|m5a.2xlarge 1|1580.00 / 2880.00|197.50 / 360.00|8333.00 / 16000.00|✓|default|
|m5a.4xlarge|2880.00|360.00|16000.00|✓|default|
|m5a.8xlarge|4750.00|593.75|20000.00|✓|default|
|m5a.12xlarge|6780.00|847.50|30000.00|✓|default|
|m5a.16xlarge|9500.00|1187.50|40000.00|✓|default|
|m5a.24xlarge|13750.00|1718.75|60000.00|✓|default|
|M5ad||||||
|1 m5ad.large|650.00 / 2880.00|81.25 / 360.00|3600.00 / 16000.00|✓|default|
|m5ad.xlarge 1|1085.00 / 2880.00|135.62 / 360.00|6000.00 / 16000.00|✓|default|
|m5ad.2xlarge 1|1580.00 / 2880.00|197.50 / 360.00|8333.00 / 16000.00|✓|default|
|m5ad.4xlarge|2880.00|360.00|16000.00|✓|default|
|m5ad.8xlarge|4750.00|593.75|20000.00|✓|default|


Amazon EBS specifications 53


-----

**Instance**


**Baseline /**


**Baseline /**


**Baseline /**


**NVMe** **EBS**

|type|Maximum bandwidth (Mbps)|Maximum throughput (MB/s, 128 KiB I/O)|Maximum IOPS (16 KiB I/O)|Col5|optimization 2|
|---|---|---|---|---|---|
|m5ad.12xl arge|6780.00|847.50|30000.00|✓|default|
|m5ad.16xl arge|9500.00|1187.50|40000.00|✓|default|
|m5ad.24xl arge|13750.00|1718.75|60000.00|✓|default|
|M5d||||||
|1 m5d.large|650.00 / 4750.00|81.25 / 593.75|3600.00 / 18750.00|✓|default|
|1 m5d.xlarge|1150.00 / 4750.00|143.75 / 593.75|6000.00 / 18750.00|✓|default|
|m5d.2xlarge 1|2300.00 / 4750.00|287.50 / 593.75|12000.00 / 18750.00|✓|default|
|m5d.4xlarge|4750.00|593.75|18750.00|✓|default|
|m5d.8xlarge|6800.00|850.00|30000.00|✓|default|
|m5d.12xla rge|9500.00|1187.50|40000.00|✓|default|
|m5d.16xla rge|13600.00|1700.00|60000.00|✓|default|
|m5d.24xla rge|19000.00|2375.00|80000.00|✓|default|
|m5d.metal|19000.00|2375.00|80000.00|✓|default|


Amazon EBS specifications 54


-----

**Instance**


**Baseline /**


**Baseline /**


**Baseline /**


**NVMe** **EBS**

|type Maximum bandwidth (Mbps) Maximum throughput (MB/s, 128 KiB I/O) Maximum IOPS (16 KiB I/O) optimization 2|Col2|Col3|Col4|Col5|Col6|
|---|---|---|---|---|---|
|M5dn||||||
|1 m5dn.large|650.00 / 4750.00|81.25 / 593.75|3600.00 / 18750.00|✓|default|
|m5dn.xlarge 1|1150.00 / 4750.00|143.75 / 593.75|6000.00 / 18750.00|✓|default|
|m5dn.2xla 1 rge|2300.00 / 4750.00|287.50 / 593.75|12000.00 / 18750.00|✓|default|
|m5dn.4xla rge|4750.00|593.75|18750.00|✓|default|
|m5dn.8xla rge|6800.00|850.00|30000.00|✓|default|
|m5dn.12xl arge|9500.00|1187.50|40000.00|✓|default|
|m5dn.16xl arge|13600.00|1700.00|60000.00|✓|default|
|m5dn.24xl arge|19000.00|2375.00|80000.00|✓|default|
|m5dn.metal|19000.00|2375.00|80000.00|✓|default|
|M5n||||||
|1 m5n.large|650.00 / 4750.00|81.25 / 593.75|3600.00 / 18750.00|✓|default|


Amazon EBS specifications 55


-----

**Instance**


**Baseline /**


**Baseline /**


**Baseline /**


**NVMe** **EBS**

|type|Maximum bandwidth (Mbps)|Maximum throughput (MB/s, 128 KiB I/O)|Maximum IOPS (16 KiB I/O)|Col5|optimization 2|
|---|---|---|---|---|---|
|1 m5n.xlarge|1150.00 / 4750.00|143.75 / 593.75|6000.00 / 18750.00|✓|default|
|m5n.2xlarge 1|2300.00 / 4750.00|287.50 / 593.75|12000.00 / 18750.00|✓|default|
|m5n.4xlarge|4750.00|593.75|18750.00|✓|default|
|m5n.8xlarge|6800.00|850.00|30000.00|✓|default|
|m5n.12xla rge|9500.00|1187.50|40000.00|✓|default|
|m5n.16xla rge|13600.00|1700.00|60000.00|✓|default|
|m5n.24xla rge|19000.00|2375.00|80000.00|✓|default|
|m5n.metal|19000.00|2375.00|80000.00|✓|default|
|M5zn||||||
|1 m5zn.large|800.00 / 3170.00|100.00 / 396.25|3333.00 / 13333.00|✓|default|
|m5zn.xlarge 1|1564.00 / 3170.00|195.50 / 396.25|6667.00 / 13333.00|✓|default|
|m5zn.2xlarge|3170.00|396.25|13333.00|✓|default|
|m5zn.3xlarge|4750.00|593.75|20000.00|✓|default|
|m5zn.6xlarge|9500.00|1187.50|40000.00|✓|default|


Amazon EBS specifications 56


-----

**Instance**


**Baseline /**


**Baseline /**


**Baseline /**


**NVMe** **EBS**

|type|Maximum bandwidth (Mbps)|Maximum throughput (MB/s, 128 KiB I/O)|Maximum IOPS (16 KiB I/O)|Col5|optimization 2|
|---|---|---|---|---|---|
|m5zn.12xl arge|19000.00|2375.00|80000.00|✓|default|
|m5zn.metal|19000.00|2375.00|80000.00|✓|default|
|M6a||||||
|1 m6a.large|650.00 / 10000.00|81.25 / 1250.00|3600.00 / 40000.00|✓|default|
|1 m6a.xlarge|1250.00 / 10000.00|156.25 / 1250.00|6000.00 / 40000.00|✓|default|
|m6a.2xlarge 1|2500.00 / 10000.00|312.50 / 1250.00|12000.00 / 40000.00|✓|default|
|m6a.4xlarge 1|5000.00 / 10000.00|625.00 / 1250.00|20000.00 / 40000.00|✓|default|
|m6a.8xlarge|10000.00|1250.00|40000.00|✓|default|
|m6a.12xlarge|15000.00|1875.00|60000.00|✓|default|
|m6a.16xlarge|20000.00|2500.00|80000.00|✓|default|
|m6a.24xlarge|30000.00|3750.00|120000.00|✓|default|
|m6a.32xlarge|40000.00|5000.00|160000.00|✓|default|
|m6a.48xlarge|40000.00|5000.00|240000.00|✓|default|
|m6a.metal|40000.00|5000.00|240000.00|✓|default|
|M6g||||||


Amazon EBS specifications 57


-----

**Instance**


**Baseline /**


**Baseline /**


**Baseline /**


**NVMe** **EBS**

|type|Maximum bandwidth (Mbps)|Maximum throughput (MB/s, 128 KiB I/O)|Maximum IOPS (16 KiB I/O)|Col5|optimization 2|
|---|---|---|---|---|---|
|m6g.medium 1|315.00 / 4750.00|39.38 / 593.75|2500.00 / 20000.00|✓|default|
|1 m6g.large|630.00 / 4750.00|78.75 / 593.75|3600.00 / 20000.00|✓|default|
|1 m6g.xlarge|1188.00 / 4750.00|148.50 / 593.75|6000.00 / 20000.00|✓|default|
|m6g.2xlarge 1|2375.00 / 4750.00|296.88 / 593.75|12000.00 / 20000.00|✓|default|
|m6g.4xlarge|4750.00|593.75|20000.00|✓|default|
|m6g.8xlarge|9500.00|1187.50|40000.00|✓|default|
|m6g.12xla rge|14250.00|1781.25|50000.00|✓|default|
|m6g.16xla rge|19000.00|2375.00|80000.00|✓|default|
|m6g.metal|19000.00|2375.00|80000.00|✓|default|
|M6gd||||||
|m6gd.medi 1 um|315.00 / 4750.00|39.38 / 593.75|2500.00 / 20000.00|✓|default|
|1 m6gd.large|630.00 / 4750.00|78.75 / 593.75|3600.00 / 20000.00|✓|default|
|m6gd.xlarge 1|1188.00 / 4750.00|148.50 / 593.75|6000.00 / 20000.00|✓|default|


Amazon EBS specifications 58


-----

**Instance**


**Baseline /**


**Baseline /**


**Baseline /**


**NVMe** **EBS**

|type|Maximum bandwidth (Mbps)|Maximum throughput (MB/s, 128 KiB I/O)|Maximum IOPS (16 KiB I/O)|Col5|optimization 2|
|---|---|---|---|---|---|
|m6gd.2xla 1 rge|2375.00 / 4750.00|296.88 / 593.75|12000.00 / 20000.00|✓|default|
|m6gd.4xla rge|4750.00|593.75|20000.00|✓|default|
|m6gd.8xla rge|9500.00|1187.50|40000.00|✓|default|
|m6gd.12xl arge|14250.00|1781.25|50000.00|✓|default|
|m6gd.16xl arge|19000.00|2375.00|80000.00|✓|default|
|m6gd.metal|19000.00|2375.00|80000.00|✓|default|
|M6i||||||
|1 m6i.large|650.00 / 10000.00|81.25 / 1250.00|3600.00 / 40000.00|✓|default|
|1 m6i.xlarge|1250.00 / 10000.00|156.25 / 1250.00|6000.00 / 40000.00|✓|default|
|1 m6i.2xlarge|2500.00 / 10000.00|312.50 / 1250.00|12000.00 / 40000.00|✓|default|
|1 m6i.4xlarge|5000.00 / 10000.00|625.00 / 1250.00|20000.00 / 40000.00|✓|default|
|m6i.8xlarge|10000.00|1250.00|40000.00|✓|default|
|m6i.12xlarge|15000.00|1875.00|60000.00|✓|default|


Amazon EBS specifications 59


-----

**Instance**


**Baseline /**


**Baseline /**


**Baseline /**


**NVMe** **EBS**

|type|Maximum bandwidth (Mbps)|Maximum throughput (MB/s, 128 KiB I/O)|Maximum IOPS (16 KiB I/O)|Col5|optimization 2|
|---|---|---|---|---|---|
|m6i.16xlarge|20000.00|2500.00|80000.00|✓|default|
|m6i.24xlarge|30000.00|3750.00|120000.00|✓|default|
|m6i.32xlarge|40000.00|5000.00|160000.00|✓|default|
|m6i.metal|40000.00|5000.00|160000.00|✓|default|
|M6id||||||
|1 m6id.large|650.00 / 10000.00|81.25 / 1250.00|3600.00 / 40000.00|✓|default|
|1 m6id.xlarge|1250.00 / 10000.00|156.25 / 1250.00|6000.00 / 40000.00|✓|default|
|m6id.2xlarge 1|2500.00 / 10000.00|312.50 / 1250.00|12000.00 / 40000.00|✓|default|
|m6id.4xlarge 1|5000.00 / 10000.00|625.00 / 1250.00|20000.00 / 40000.00|✓|default|
|m6id.8xlarge|10000.00|1250.00|40000.00|✓|default|
|m6id.12xl arge|15000.00|1875.00|60000.00|✓|default|
|m6id.16xl arge|20000.00|2500.00|80000.00|✓|default|
|m6id.24xl arge|30000.00|3750.00|120000.00|✓|default|


Amazon EBS specifications 60


-----

**Instance**


**Baseline /**


**Baseline /**


**Baseline /**


**NVMe** **EBS**

|type|Maximum bandwidth (Mbps)|Maximum throughput (MB/s, 128 KiB I/O)|Maximum IOPS (16 KiB I/O)|Col5|optimization 2|
|---|---|---|---|---|---|
|m6id.32xl arge|40000.00|5000.00|160000.00|✓|default|
|m6id.metal|40000.00|5000.00|160000.00|✓|default|
|M6idn||||||
|1 m6idn.large|1562.00 / 25000.00|195.31 / 3125.00|6250.00 / 100000.00|✓|default|
|m6idn.xlarge 1|3125.00 / 25000.00|390.62 / 3125.00|12500.00 / 100000.00|✓|default|
|m6idn.2xl 1 arge|6250.00 / 25000.00|781.25 / 3125.00|25000.00 / 100000.00|✓|default|
|m6idn.4xl 1 arge|12500.00 / 25000.00|1562.50 / 3125.00|50000.00 / 100000.00|✓|default|
|m6idn.8xl arge|25000.00|3125.00|100000.00|✓|default|
|m6idn.12x large|37500.00|4687.50|150000.00|✓|default|
|m6idn.16x large|50000.00|6250.00|200000.00|✓|default|
|m6idn.24x large|75000.00|9375.00|300000.00|✓|default|
|m6idn.32x large|100000.00|12500.00|400000.00|✓|default|


Amazon EBS specifications 61


-----

**Instance**


**Baseline /**


**Baseline /**


**Baseline /**


**NVMe** **EBS**

|type|Maximum bandwidth (Mbps)|Maximum throughput (MB/s, 128 KiB I/O)|Maximum IOPS (16 KiB I/O)|Col5|optimization 2|
|---|---|---|---|---|---|
|m6idn.metal|100000.00|12500.00|400000.00|✓|default|
|M6in||||||
|1 m6in.large|1562.00 / 25000.00|195.31 / 3125.00|6250.00 / 100000.00|✓|default|
|1 m6in.xlarge|3125.00 / 25000.00|390.62 / 3125.00|12500.00 / 100000.00|✓|default|
|m6in.2xlarge 1|6250.00 / 25000.00|781.25 / 3125.00|25000.00 / 100000.00|✓|default|
|m6in.4xlarge 1|12500.00 / 25000.00|1562.50 / 3125.00|50000.00 / 100000.00|✓|default|
|m6in.8xlarge|25000.00|3125.00|100000.00|✓|default|
|m6in.12xl arge|37500.00|4687.50|150000.00|✓|default|
|m6in.16xl arge|50000.00|6250.00|200000.00|✓|default|
|m6in.24xl arge|75000.00|9375.00|300000.00|✓|default|
|m6in.32xl arge|100000.00|12500.00|400000.00|✓|default|
|m6in.metal|100000.00|12500.00|400000.00|✓|default|
|M7a||||||


Amazon EBS specifications 62


-----

**Instance**


**Baseline /**


**Baseline /**


**Baseline /**


**NVMe** **EBS**

|type|Maximum bandwidth (Mbps)|Maximum throughput (MB/s, 128 KiB I/O)|Maximum IOPS (16 KiB I/O)|Col5|optimization 2|
|---|---|---|---|---|---|
|m7a.medium 1|325.00 / 10000.00|40.62 / 1250.00|2500.00 / 40000.00|✓|default|
|1 m7a.large|650.00 / 10000.00|81.25 / 1250.00|3600.00 / 40000.00|✓|default|
|1 m7a.xlarge|1250.00 / 10000.00|156.25 / 1250.00|6000.00 / 40000.00|✓|default|
|m7a.2xlarge 1|2500.00 / 10000.00|312.50 / 1250.00|12000.00 / 40000.00|✓|default|
|m7a.4xlarge 1|5000.00 / 10000.00|625.00 / 1250.00|20000.00 / 40000.00|✓|default|
|m7a.8xlarge|10000.00|1250.00|40000.00|✓|default|
|m7a.12xlarge|15000.00|1875.00|60000.00|✓|default|
|m7a.16xlarge|20000.00|2500.00|80000.00|✓|default|
|m7a.24xlarge|30000.00|3750.00|120000.00|✓|default|
|m7a.32xlarge|40000.00|5000.00|160000.00|✓|default|
|m7a.48xlarge|40000.00|5000.00|240000.00|✓|default|
|m7a.metal -48xl|40000.00|5000.00|240000.00|✓|default|
|M7g||||||
|m7g.medium 1|315.00 / 10000.00|39.38 / 1250.00|2500.00 / 40000.00|✓|default|


Amazon EBS specifications 63


-----

**Instance**


**Baseline /**


**Baseline /**


**Baseline /**


**NVMe** **EBS**

|type|Maximum bandwidth (Mbps)|Maximum throughput (MB/s, 128 KiB I/O)|Maximum IOPS (16 KiB I/O)|Col5|optimization 2|
|---|---|---|---|---|---|
|1 m7g.large|630.00 / 10000.00|78.75 / 1250.00|3600.00 / 40000.00|✓|default|
|1 m7g.xlarge|1250.00 / 10000.00|156.25 / 1250.00|6000.00 / 40000.00|✓|default|
|m7g.2xlarge 1|2500.00 / 10000.00|312.50 / 1250.00|12000.00 / 40000.00|✓|default|
|m7g.4xlarge 1|5000.00 / 10000.00|625.00 / 1250.00|20000.00 / 40000.00|✓|default|
|m7g.8xlarge|10000.00|1250.00|40000.00|✓|default|
|m7g.12xla rge|15000.00|1875.00|60000.00|✓|default|
|m7g.16xla rge|20000.00|2500.00|80000.00|✓|default|
|m7g.metal|20000.00|2500.00|80000.00|✓|default|
|M7gd||||||
|m7gd.medi 1 um|315.00 / 10000.00|39.38 / 1250.00|2500.00 / 40000.00|✓|default|
|1 m7gd.large|630.00 / 10000.00|78.75 / 1250.00|3600.00 / 40000.00|✓|default|
|m7gd.xlarge 1|1250.00 / 10000.00|156.25 / 1250.00|6000.00 / 40000.00|✓|default|


Amazon EBS specifications 64


-----

**Instance**


**Baseline /**


**Baseline /**


**Baseline /**


**NVMe** **EBS**

|type|Maximum bandwidth (Mbps)|Maximum throughput (MB/s, 128 KiB I/O)|Maximum IOPS (16 KiB I/O)|Col5|optimization 2|
|---|---|---|---|---|---|
|m7gd.2xla 1 rge|2500.00 / 10000.00|312.50 / 1250.00|12000.00 / 40000.00|✓|default|
|m7gd.4xla 1 rge|5000.00 / 10000.00|625.00 / 1250.00|20000.00 / 40000.00|✓|default|
|m7gd.8xla rge|10000.00|1250.00|40000.00|✓|default|
|m7gd.12xl arge|15000.00|1875.00|60000.00|✓|default|
|m7gd.16xl arge|20000.00|2500.00|80000.00|✓|default|
|m7gd.metal|20000.00|2500.00|80000.00|✓|default|
|M7i||||||
|1 m7i.large|650.00 / 10000.00|81.25 / 1250.00|3600.00 / 40000.00|✓|default|
|1 m7i.xlarge|1250.00 / 10000.00|156.25 / 1250.00|6000.00 / 40000.00|✓|default|
|1 m7i.2xlarge|2500.00 / 10000.00|312.50 / 1250.00|12000.00 / 40000.00|✓|default|
|1 m7i.4xlarge|5000.00 / 10000.00|625.00 / 1250.00|20000.00 / 40000.00|✓|default|
|m7i.8xlarge|10000.00|1250.00|40000.00|✓|default|
|m7i.12xlarge|15000.00|1875.00|60000.00|✓|default|


Amazon EBS specifications 65


-----

**Instance**


**Baseline /**


**Baseline /**


**Baseline /**


**NVMe** **EBS**

|type|Maximum bandwidth (Mbps)|Maximum throughput (MB/s, 128 KiB I/O)|Maximum IOPS (16 KiB I/O)|Col5|optimization 2|
|---|---|---|---|---|---|
|m7i.16xlarge|20000.00|2500.00|80000.00|✓|default|
|m7i.24xlarge|30000.00|3750.00|120000.00|✓|default|
|m7i.48xlarge|40000.00|5000.00|240000.00|✓|default|
|m7i.metal -24xl|30000.00|3750.00|120000.00|✓|default|
|m7i.metal -48xl|40000.00|5000.00|240000.00|✓|default|
|M7i-flex||||||
|m7i-flex. 1 large|312.00 / 10000.00|39.06 / 1250.00|2500.00 / 40000.00|✓|default|
|m7i-flex. 1 xlarge|625.00 / 10000.00|78.12 / 1250.00|3600.00 / 40000.00|✓|default|
|m7i-flex. 1 2xlarge|1250.00 / 10000.00|156.25 / 1250.00|6000.00 / 40000.00|✓|default|
|m7i-flex. 1 4xlarge|2500.00 / 10000.00|312.50 / 1250.00|12000.00 / 40000.00|✓|default|
|m7i-flex. 1 8xlarge|5000.00 / 10000.00|625.00 / 1250.00|20000.00 / 40000.00|✓|default|
|Mac1||||||
|mac1.metal|14000.00|1750.00|80000.00|✓|default|
|Mac2||||||


Amazon EBS specifications 66


-----

**Instance**


**Baseline /**


**Baseline /**


**Baseline /**


**NVMe** **EBS**

|type|Maximum bandwidth (Mbps)|Maximum throughput (MB/s, 128 KiB I/O)|Maximum IOPS (16 KiB I/O)|Col5|optimization 2|
|---|---|---|---|---|---|
|mac2.metal|10000.00|1250.00|55000.00|✓|default|
|Mac2-m1ultra||||||
|mac2-m1ul tra.metal|10000.00|1250.00|55000.00|✓|default|
|Mac2-m2||||||
|mac2-m2.m etal|8000.00|1000.00|55000.00|✓|default|
|Mac2-m2pro||||||
|mac2-m2pr o.metal|8000.00|1000.00|55000.00|✓|default|
|T2||||||
|T3||||||
|1 t3.nano|43.00 / 2085.00|5.38 / 260.62|250.00 / 11800.00|✓|default|
|1 t3.micro|87.00 / 2085.00|10.88 / 260.62|500.00 / 11800.00|✓|default|
|1 t3.small|174.00 / 2085.00|21.75 / 260.62|1000.00 / 11800.00|✓|default|
|1 t3.medium|347.00 / 2085.00|43.38 / 260.62|2000.00 / 11800.00|✓|default|


Amazon EBS specifications 67


-----

**Instance**


**Baseline /**


**Baseline /**


**Baseline /**


**NVMe** **EBS**

|type|Maximum bandwidth (Mbps)|Maximum throughput (MB/s, 128 KiB I/O)|Maximum IOPS (16 KiB I/O)|Col5|optimization 2|
|---|---|---|---|---|---|
|1 t3.large|695.00 / 2780.00|86.88 / 347.50|4000.00 / 15700.00|✓|default|
|1 t3.xlarge|695.00 / 2780.00|86.88 / 347.50|4000.00 / 15700.00|✓|default|
|1 t3.2xlarge|695.00 / 2780.00|86.88 / 347.50|4000.00 / 15700.00|✓|default|
|T3a||||||
|1 t3a.nano|45.00 / 2085.00|5.62 / 260.62|250.00 / 11800.00|✓|default|
|1 t3a.micro|90.00 / 2085.00|11.25 / 260.62|500.00 / 11800.00|✓|default|
|1 t3a.small|175.00 / 2085.00|21.88 / 260.62|1000.00 / 11800.00|✓|default|
|1 t3a.medium|350.00 / 2085.00|43.75 / 260.62|2000.00 / 11800.00|✓|default|
|1 t3a.large|695.00 / 2780.00|86.88 / 347.50|4000.00 / 15700.00|✓|default|
|1 t3a.xlarge|695.00 / 2780.00|86.88 / 347.50|4000.00 / 15700.00|✓|default|
|1 t3a.2xlarge|695.00 / 2780.00|86.88 / 347.50|4000.00 / 15700.00|✓|default|
|T4g||||||


Amazon EBS specifications 68


-----

**Instance**

|type|Maximum bandwidth (Mbps)|Maximum throughput (MB/s, 128 KiB I/O)|Maximum IOPS (16 KiB I/O)|Col5|optimization 2|
|---|---|---|---|---|---|
|1 t4g.nano|43.00 / 2085.00|5.38 / 260.62|250.00 / 11800.00|✓|default|
|1 t4g.micro|87.00 / 2085.00|10.88 / 260.62|500.00 / 11800.00|✓|default|
|1 t4g.small|174.00 / 2085.00|21.75 / 260.62|1000.00 / 11800.00|✓|default|
|t4g.medium 1|347.00 / 2085.00|43.38 / 260.62|2000.00 / 11800.00|✓|default|
|1 t4g.large|695.00 / 2780.00|86.88 / 347.50|4000.00 / 15700.00|✓|default|
|1 t4g.xlarge|695.00 / 2780.00|86.88 / 347.50|4000.00 / 15700.00|✓|default|
|1 t4g.2xlarge|695.00 / 2780.00|86.88 / 347.50|4000.00 / 15700.00|✓|default|



**Note**


**Baseline /**
**Maximum**
**bandwidth**
**(Mbps)**


**Baseline /**
**Maximum**
**throughput**
**(MB/s, 128**
**KiB I/O)**


**Baseline /**
**Maximum**
**IOPS (16 KiB**
**I/O)**


**NVMe** **EBS**
**optimization**


1
These instances can support maximum performance for 30 minutes at least once every 24
hours, after which they revert to their baseline performance. Other instances can sustain
the maximum performance indefinitely. If your workload requires sustained maximum
performance for longer than 30 minutes, use one of these instances.
2
```
   default indicates that instances are enabled for EBS optimization by default.
   supported indicates that instances can optionally be enabled for EBS optimization For

```
[more information, see Amazon EBS–optimized instances.](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-optimized.html)

Amazon EBS specifications 69


-----

#### Instance store specifications

The following table shows the instance store volume configuration for supported instance types,
along with the aggregated IOPS performance with 4,096 byte block size at queue depth saturation.

|Instance type|Instance store volumes|Instance store type|100% random read IOPS / Write IOPS|Needs initializ 1 ation|TRIM support 2|
|---|---|---|---|---|---|
|M5ad||||||
|m5ad.large|1 x 75 GB|NVMe SSD|30,000 / 15,000||✓|
|m5ad.xlarge|1 x 150 GB|NVMe SSD|59,000 / 29,000||✓|
|m5ad.2xlarge|1 x 300 GB|NVMe SSD|117,000 / 57,000||✓|
|m5ad.4xlarge|2 x 300 GB|NVMe SSD|234,000 / 114,000||✓|
|m5ad.8xlarge|2 x 600 GB|NVMe SSD|466,666 / 233,334||✓|
|m5ad.12xlarge|2 x 900 GB|NVMe SSD|700,000 / 340,000||✓|
|m5ad.16xlarge|4 x 600 GB|NVMe SSD|933,332 / 466,668||✓|
|m5ad.24xlarge|4 x 900 GB|NVMe SSD|1,400,000 / 680,000||✓|
|M5d||||||
|m5d.large|1 x 75 GB|NVMe SSD|30,000 / 15,000||✓|



Instance store specifications 70


-----

|Instance type|Instance store volumes|Instance store type|100% random read IOPS / Write IOPS|Needs initializ ation 1|TRIM support 2|
|---|---|---|---|---|---|
|m5d.xlarge|1 x 150 GB|NVMe SSD|59,000 / 29,000||✓|
|m5d.2xlarge|1 x 300 GB|NVMe SSD|117,000 / 57,000||✓|
|m5d.4xlarge|2 x 300 GB|NVMe SSD|234,000 / 114,000||✓|
|m5d.8xlarge|2 x 600 GB|NVMe SSD|466,666 / 233,334||✓|
|m5d.12xlarge|2 x 900 GB|NVMe SSD|700,000 / 340,000||✓|
|m5d.16xlarge|4 x 600 GB|NVMe SSD|933,332 / 466,668||✓|
|m5d.24xlarge|4 x 900 GB|NVMe SSD|1,400,000 / 680,000||✓|
|m5d.metal|4 x 900 GB|NVMe SSD|1,400,000 / 680,000||✓|
|M5dn||||||
|m5dn.large|1 x 75 GB|NVMe SSD|29,000 / 14,500||✓|
|m5dn.xlarge|1 x 150 GB|NVMe SSD|58,000 / 29,000||✓|
|m5dn.2xlarge|1 x 300 GB|NVMe SSD|116,000 / 58,000||✓|


Instance store specifications 71


-----

|Instance type|Instance store volumes|Instance store type|100% random read IOPS / Write IOPS|Needs initializ ation 1|TRIM support 2|
|---|---|---|---|---|---|
|m5dn.4xlarge|2 x 300 GB|NVMe SSD|232,000 / 116,000||✓|
|m5dn.8xlarge|2 x 600 GB|NVMe SSD|464,000 / 232,000||✓|
|m5dn.12xlarge|2 x 900 GB|NVMe SSD|700,000 / 350,000||✓|
|m5dn.16xlarge|4 x 600 GB|NVMe SSD|930,000 / 465,000||✓|
|m5dn.24xlarge|4 x 900 GB|NVMe SSD|1,400,000 / 700,000||✓|
|m5dn.metal|4 x 900 GB|NVMe SSD|1,400,000 / 700,000||✓|
|M6gd||||||
|m6gd.medium|1 x 59 GB|NVMe SSD|13,438 / 5,625||✓|
|m6gd.large|1 x 118 GB|NVMe SSD|26,875 / 11,250||✓|
|m6gd.xlarge|1 x 237 GB|NVMe SSD|53,750 / 22,500||✓|
|m6gd.2xlarge|1 x 474 GB|NVMe SSD|107,500 / 45,000||✓|
|m6gd.4xlarge|1 x 950 GB|NVMe SSD|215,000 / 90,000||✓|


Instance store specifications 72


-----

|Instance type|Instance store volumes|Instance store type|100% random read IOPS / Write IOPS|Needs initializ ation 1|TRIM support 2|
|---|---|---|---|---|---|
|m6gd.8xlarge|1 x 1900 GB|NVMe SSD|430,000 / 180,000||✓|
|m6gd.12xlarge|2 x 1425 GB|NVMe SSD|645,000 / 270,000||✓|
|m6gd.16xlarge|2 x 1900 GB|NVMe SSD|860,000 / 360,000||✓|
|m6gd.metal|2 x 1900 GB|NVMe SSD|860,000 / 360,000||✓|
|M6id||||||
|m6id.large|1 x 118 GB|NVMe SSD|33,542 / 16,771||✓|
|m6id.xlarge|1 x 237 GB|NVMe SSD|67,083 / 33,542||✓|
|m6id.2xlarge|1 x 474 GB|NVMe SSD|134,167 / 67,084||✓|
|m6id.4xlarge|1 x 950 GB|NVMe SSD|268,333 / 134,167||✓|
|m6id.8xlarge|1 x 1900 GB|NVMe SSD|536,666 / 268,334||✓|
|m6id.12xlarge|2 x 1425 GB|NVMe SSD|804,998 / 402,500||✓|
|m6id.16xlarge|2 x 1900 GB|NVMe SSD|1,073,332 / 536,668||✓|


Instance store specifications 73


-----

|Instance type|Instance store volumes|Instance store type|100% random read IOPS / Write IOPS|Needs initializ ation 1|TRIM support 2|
|---|---|---|---|---|---|
|m6id.24xlarge|4 x 1425 GB|NVMe SSD|1,609,996 / 805,000||✓|
|m6id.32xlarge|4 x 1900 GB|NVMe SSD|2,146,664 / 1,073,336||✓|
|m6id.metal|4 x 1900 GB|NVMe SSD|2,146,664 / 1,073,336||✓|
|M6idn||||||
|m6idn.large|1 x 118 GB|NVMe SSD|33,542 / 16,771||✓|
|m6idn.xlarge|1 x 237 GB|NVMe SSD|67,083 / 33,542||✓|
|m6idn.2xlarge|1 x 474 GB|NVMe SSD|134,167 / 67,084||✓|
|m6idn.4xlarge|1 x 950 GB|NVMe SSD|268,333 / 134,167||✓|
|m6idn.8xlarge|1 x 1900 GB|NVMe SSD|536,666 / 268,334||✓|
|m6idn.12xlarge|2 x 1425 GB|NVMe SSD|804,998 / 402,500||✓|
|m6idn.16xlarge|2 x 1900 GB|NVMe SSD|1,073,332 / 536,668||✓|
|m6idn.24xlarge|4 x 1425 GB|NVMe SSD|1,609,996 / 805,000||✓|


Instance store specifications 74


-----

|Instance type|Instance store volumes|Instance store type|100% random read IOPS / Write IOPS|Needs initializ ation 1|TRIM support 2|
|---|---|---|---|---|---|
|m6idn.32xlarge|4 x 1900 GB|NVMe SSD|2,146,664 / 1,073,336||✓|
|m6idn.metal|4 x 1900 GB|NVMe SSD|2,146,664 / 1,073,336||✓|
|M7gd||||||
|m7gd.medium|1 x 59 GB|NVMe SSD|16,771 / 8,385||✓|
|m7gd.large|1 x 118 GB|NVMe SSD|33,542 / 16,771||✓|
|m7gd.xlarge|1 x 237 GB|NVMe SSD|67,083 / 33,542||✓|
|m7gd.2xlarge|1 x 474 GB|NVMe SSD|134,167 / 67,084||✓|
|m7gd.4xlarge|1 x 950 GB|NVMe SSD|268,333 / 134,167||✓|
|m7gd.8xlarge|1 x 1900 GB|NVMe SSD|536,666 / 268,334||✓|
|m7gd.12xlarge|2 x 1425 GB|NVMe SSD|804,998 / 402,500||✓|
|m7gd.16xlarge|2 x 1900 GB|NVMe SSD|1,073,332 / 536,668||✓|
|m7gd.metal|2 x 1900 GB|NVMe SSD|1,073,332 / 536,668||✓|


Instance store specifications 75


-----

1
Volumes attached to certain instances suffer a first-write penalty unless initialized. For more
[information, see Optimize disk performance for instance store volumes.](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/disk-performance.html)

2
[For more information, see Instance store volume TRIM support.](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ssd-instance-store.html#InstanceStoreTrimSupport)

#### Security specifications

|Instance type|EBS encryptio n|Instance store encryptio n|Encryptio n in transit|AMD SEV-SNP|NitroTPM|Nitro Enclaves|
|---|---|---|---|---|---|---|
|M5|||||||
|m5.large|✓|Instance store not supported|✗|✗|✓|✗|
|m5.xlarge|✓|Instance store not supported|✗|✗|✓|✓|
|m5.2xlarge|✓|Instance store not supported|✗|✗|✓|✓|
|m5.4xlarge|✓|Instance store not supported|✗|✗|✓|✓|
|m5.8xlarge|✓|Instance store not supported|✗|✗|✓|✓|
|m5.12xlarge|✓|Instance store not supported|✗|✗|✓|✓|



Security specifications 76


-----

|Instance type|EBS encryptio n|Instance store encryptio n|Encryptio n in transit|AMD SEV-SNP|NitroTPM|Nitro Enclaves|
|---|---|---|---|---|---|---|
|m5.16xlarge|✓|Instance store not supported|✗|✗|✓|✓|
|m5.24xlarge|✓|Instance store not supported|✗|✗|✓|✓|
|m5.metal|✓|Instance store not supported|✗|✗|✗|✗|
|M5a|||||||
|m5a.large|✓|Instance store not supported|✗|✗|✓|✗|
|m5a.xlarge|✓|Instance store not supported|✗|✗|✓|✓|
|m5a.2xlarge|✓|Instance store not supported|✗|✗|✓|✓|
|m5a.4xlarge|✓|Instance store not supported|✗|✗|✓|✓|
|m5a.8xlarge|✓|Instance store not supported|✗|✗|✓|✓|


Security specifications 77


-----

|Instance type|EBS encryptio n|Instance store encryptio n|Encryptio n in transit|AMD SEV-SNP|NitroTPM|Nitro Enclaves|
|---|---|---|---|---|---|---|
|m5a.12xlarge|✓|Instance store not supported|✗|✗|✓|✓|
|m5a.16xlarge|✓|Instance store not supported|✗|✗|✓|✓|
|m5a.24xlarge|✓|Instance store not supported|✗|✗|✓|✓|
|M5ad|||||||
|m5ad.large|✓|✓|✗|✗|✓|✗|
|m5ad.xlarge|✓|✓|✗|✗|✓|✓|
|m5ad.2xlarge|✓|✓|✗|✗|✓|✓|
|m5ad.4xlarge|✓|✓|✗|✗|✓|✓|
|m5ad.8xlarge|✓|✓|✗|✗|✓|✓|
|m5ad.12xlarge|✓|✓|✗|✗|✓|✓|
|m5ad.16xlarge|✓|✓|✗|✗|✓|✓|
|m5ad.24xlarge|✓|✓|✗|✗|✓|✓|
|M5d|||||||
|m5d.large|✓|✓|✗|✗|✓|✗|
|m5d.xlarge|✓|✓|✗|✗|✓|✓|


Security specifications 78


-----

|Instance type|EBS encryptio n|Instance store encryptio n|Encryptio n in transit|AMD SEV-SNP|NitroTPM|Nitro Enclaves|
|---|---|---|---|---|---|---|
|m5d.2xlarge|✓|✓|✗|✗|✓|✓|
|m5d.4xlarge|✓|✓|✗|✗|✓|✓|
|m5d.8xlarge|✓|✓|✗|✗|✓|✓|
|m5d.12xlarge|✓|✓|✗|✗|✓|✓|
|m5d.16xlarge|✓|✓|✗|✗|✓|✓|
|m5d.24xlarge|✓|✓|✗|✗|✓|✓|
|m5d.metal|✓|✓|✗|✗|✗|✗|
|M5dn|||||||
|m5dn.large|✓|✓|✓|✗|✓|✗|
|m5dn.xlarge|✓|✓|✓|✗|✓|✓|
|m5dn.2xlarge|✓|✓|✓|✗|✓|✓|
|m5dn.4xlarge|✓|✓|✓|✗|✓|✓|
|m5dn.8xlarge|✓|✓|✓|✗|✓|✓|
|m5dn.12xlarge|✓|✓|✓|✗|✓|✓|
|m5dn.16xlarge|✓|✓|✓|✗|✓|✓|
|m5dn.24xlarge|✓|✓|✓|✗|✓|✓|
|m5dn.metal|✓|✓|✓|✗|✗|✗|
|M5n|||||||


Security specifications 79


-----

|Instance type|EBS encryptio n|Instance store encryptio n|Encryptio n in transit|AMD SEV-SNP|NitroTPM|Nitro Enclaves|
|---|---|---|---|---|---|---|
|m5n.large|✓|Instance store not supported|✓|✗|✓|✗|
|m5n.xlarge|✓|Instance store not supported|✓|✗|✓|✓|
|m5n.2xlarge|✓|Instance store not supported|✓|✗|✓|✓|
|m5n.4xlarge|✓|Instance store not supported|✓|✗|✓|✓|
|m5n.8xlarge|✓|Instance store not supported|✓|✗|✓|✓|
|m5n.12xlarge|✓|Instance store not supported|✓|✗|✓|✓|
|m5n.16xlarge|✓|Instance store not supported|✓|✗|✓|✓|
|m5n.24xlarge|✓|Instance store not supported|✓|✗|✓|✓|


Security specifications 80


-----

|Instance type|EBS encryptio n|Instance store encryptio n|Encryptio n in transit|AMD SEV-SNP|NitroTPM|Nitro Enclaves|
|---|---|---|---|---|---|---|
|m5n.metal|✓|Instance store not supported|✓|✗|✗|✗|
|M5zn|||||||
|m5zn.large|✓|Instance store not supported|✓|✗|✓|✗|
|m5zn.xlarge|✓|Instance store not supported|✓|✗|✓|✓|
|m5zn.2xlarge|✓|Instance store not supported|✓|✗|✓|✓|
|m5zn.3xlarge|✓|Instance store not supported|✓|✗|✓|✓|
|m5zn.6xlarge|✓|Instance store not supported|✓|✗|✓|✓|
|m5zn.12xlarge|✓|Instance store not supported|✓|✗|✓|✓|
|m5zn.metal|✓|Instance store not supported|✓|✗|✗|✗|


Security specifications 81


-----

|Instance type EBS encryptio n Instance store encryptio n Encryptio n in transit AMD SEV-SNP NitroTPM Nitro Enclaves|Col2|Col3|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
|M6a|||||||
|m6a.large|✓|Instance store not supported|✓|✓|✓|✗|
|m6a.xlarge|✓|Instance store not supported|✓|✓|✓|✓|
|m6a.2xlarge|✓|Instance store not supported|✓|✓|✓|✓|
|m6a.4xlarge|✓|Instance store not supported|✓|✓|✓|✓|
|m6a.8xlarge|✓|Instance store not supported|✓|✓|✓|✓|
|m6a.12xlarge|✓|Instance store not supported|✓|✗|✓|✓|
|m6a.16xlarge|✓|Instance store not supported|✓|✗|✓|✓|
|m6a.24xlarge|✓|Instance store not supported|✓|✗|✓|✓|


Security specifications 82


-----

|Instance type|EBS encryptio n|Instance store encryptio n|Encryptio n in transit|AMD SEV-SNP|NitroTPM|Nitro Enclaves|
|---|---|---|---|---|---|---|
|m6a.32xlarge|✓|Instance store not supported|✓|✗|✓|✓|
|m6a.48xlarge|✓|Instance store not supported|✓|✗|✓|✓|
|m6a.metal|✓|Instance store not supported|✓|✗|✗|✗|
|M6g|||||||
|m6g.medium|✓|Instance store not supported|✗|✗|✗|✗|
|m6g.large|✓|Instance store not supported|✗|✗|✗|✓|
|m6g.xlarge|✓|Instance store not supported|✗|✗|✗|✓|
|m6g.2xlarge|✓|Instance store not supported|✗|✗|✗|✓|
|m6g.4xlarge|✓|Instance store not supported|✗|✗|✗|✓|


Security specifications 83


-----

|Instance type|EBS encryptio n|Instance store encryptio n|Encryptio n in transit|AMD SEV-SNP|NitroTPM|Nitro Enclaves|
|---|---|---|---|---|---|---|
|m6g.8xlarge|✓|Instance store not supported|✗|✗|✗|✓|
|m6g.12xlarge|✓|Instance store not supported|✗|✗|✗|✓|
|m6g.16xlarge|✓|Instance store not supported|✗|✗|✗|✓|
|m6g.metal|✓|Instance store not supported|✗|✗|✗|✗|
|M6gd|||||||
|m6gd.medium|✓|✓|✗|✗|✗|✗|
|m6gd.large|✓|✓|✗|✗|✗|✓|
|m6gd.xlarge|✓|✓|✗|✗|✗|✓|
|m6gd.2xlarge|✓|✓|✗|✗|✗|✓|
|m6gd.4xlarge|✓|✓|✗|✗|✗|✓|
|m6gd.8xlarge|✓|✓|✗|✗|✗|✓|
|m6gd.12xlarge|✓|✓|✗|✗|✗|✓|
|m6gd.16xlarge|✓|✓|✗|✗|✗|✓|
|m6gd.metal|✓|✓|✗|✗|✗|✗|


Security specifications 84


-----

|Instance type EBS encryptio n Instance store encryptio n Encryptio n in transit AMD SEV-SNP NitroTPM Nitro Enclaves|Col2|Col3|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
|M6i|||||||
|m6i.large|✓|Instance store not supported|✓|✗|✓|✗|
|m6i.xlarge|✓|Instance store not supported|✓|✗|✓|✓|
|m6i.2xlarge|✓|Instance store not supported|✓|✗|✓|✓|
|m6i.4xlarge|✓|Instance store not supported|✓|✗|✓|✓|
|m6i.8xlarge|✓|Instance store not supported|✓|✗|✓|✓|
|m6i.12xlarge|✓|Instance store not supported|✓|✗|✓|✓|
|m6i.16xlarge|✓|Instance store not supported|✓|✗|✓|✓|
|m6i.24xlarge|✓|Instance store not supported|✓|✗|✓|✓|


Security specifications 85


-----

|Instance type|EBS encryptio n|Instance store encryptio n|Encryptio n in transit|AMD SEV-SNP|NitroTPM|Nitro Enclaves|
|---|---|---|---|---|---|---|
|m6i.32xlarge|✓|Instance store not supported|✓|✗|✓|✓|
|m6i.metal|✓|Instance store not supported|✓|✗|✗|✗|
|M6id|||||||
|m6id.large|✓|✓|✓|✗|✓|✗|
|m6id.xlarge|✓|✓|✓|✗|✓|✓|
|m6id.2xlarge|✓|✓|✓|✗|✓|✓|
|m6id.4xlarge|✓|✓|✓|✗|✓|✓|
|m6id.8xlarge|✓|✓|✓|✗|✓|✓|
|m6id.12xlarge|✓|✓|✓|✗|✓|✓|
|m6id.16xlarge|✓|✓|✓|✗|✓|✓|
|m6id.24xlarge|✓|✓|✓|✗|✓|✓|
|m6id.32xlarge|✓|✓|✓|✗|✓|✓|
|m6id.metal|✓|✓|✓|✗|✗|✗|
|M6idn|||||||
|m6idn.large|✓|✓|✓|✗|✓|✗|
|m6idn.xlarge|✓|✓|✓|✗|✓|✓|


Security specifications 86


-----

|Instance type|EBS encryptio n|Instance store encryptio n|Encryptio n in transit|AMD SEV-SNP|NitroTPM|Nitro Enclaves|
|---|---|---|---|---|---|---|
|m6idn.2xlarge|✓|✓|✓|✗|✓|✓|
|m6idn.4xlarge|✓|✓|✓|✗|✓|✓|
|m6idn.8xlarge|✓|✓|✓|✗|✓|✓|
|m6idn.12xlarge|✓|✓|✓|✗|✓|✓|
|m6idn.16xlarge|✓|✓|✓|✗|✓|✓|
|m6idn.24xlarge|✓|✓|✓|✗|✓|✓|
|m6idn.32xlarge|✓|✓|✓|✗|✓|✓|
|m6idn.metal|✓|✓|✓|✗|✗|✗|
|M6in|||||||
|m6in.large|✓|Instance store not supported|✓|✗|✓|✗|
|m6in.xlarge|✓|Instance store not supported|✓|✗|✓|✓|
|m6in.2xlarge|✓|Instance store not supported|✓|✗|✓|✓|
|m6in.4xlarge|✓|Instance store not supported|✓|✗|✓|✓|


Security specifications 87


-----

|Instance type|EBS encryptio n|Instance store encryptio n|Encryptio n in transit|AMD SEV-SNP|NitroTPM|Nitro Enclaves|
|---|---|---|---|---|---|---|
|m6in.8xlarge|✓|Instance store not supported|✓|✗|✓|✓|
|m6in.12xlarge|✓|Instance store not supported|✓|✗|✓|✓|
|m6in.16xlarge|✓|Instance store not supported|✓|✗|✓|✓|
|m6in.24xlarge|✓|Instance store not supported|✓|✗|✓|✓|
|m6in.32xlarge|✓|Instance store not supported|✓|✗|✓|✓|
|m6in.metal|✓|Instance store not supported|✓|✗|✗|✗|
|M7a|||||||
|m7a.medium|✓|Instance store not supported|✓|✗|✓|✗|
|m7a.large|✓|Instance store not supported|✓|✗|✓|✗|


Security specifications 88


-----

|Instance type|EBS encryptio n|Instance store encryptio n|Encryptio n in transit|AMD SEV-SNP|NitroTPM|Nitro Enclaves|
|---|---|---|---|---|---|---|
|m7a.xlarge|✓|Instance store not supported|✓|✗|✓|✗|
|m7a.2xlarge|✓|Instance store not supported|✓|✗|✓|✗|
|m7a.4xlarge|✓|Instance store not supported|✓|✗|✓|✗|
|m7a.8xlarge|✓|Instance store not supported|✓|✗|✓|✗|
|m7a.12xlarge|✓|Instance store not supported|✓|✗|✓|✗|
|m7a.16xlarge|✓|Instance store not supported|✓|✗|✓|✗|
|m7a.24xlarge|✓|Instance store not supported|✓|✗|✓|✗|
|m7a.32xlarge|✓|Instance store not supported|✓|✗|✓|✗|


Security specifications 89


-----

|Instance type|EBS encryptio n|Instance store encryptio n|Encryptio n in transit|AMD SEV-SNP|NitroTPM|Nitro Enclaves|
|---|---|---|---|---|---|---|
|m7a.48xlarge|✓|Instance store not supported|✓|✗|✓|✗|
|m7a.metal-48xl|✓|Instance store not supported|✓|✗|✗|✗|
|M7g|||||||
|m7g.medium|✓|Instance store not supported|✓|✗|✗|✗|
|m7g.large|✓|Instance store not supported|✓|✗|✗|✗|
|m7g.xlarge|✓|Instance store not supported|✓|✗|✗|✗|
|m7g.2xlarge|✓|Instance store not supported|✓|✗|✗|✗|
|m7g.4xlarge|✓|Instance store not supported|✓|✗|✗|✗|
|m7g.8xlarge|✓|Instance store not supported|✓|✗|✗|✗|


Security specifications 90


-----

|Instance type|EBS encryptio n|Instance store encryptio n|Encryptio n in transit|AMD SEV-SNP|NitroTPM|Nitro Enclaves|
|---|---|---|---|---|---|---|
|m7g.12xlarge|✓|Instance store not supported|✓|✗|✗|✗|
|m7g.16xlarge|✓|Instance store not supported|✓|✗|✗|✗|
|m7g.metal|✓|Instance store not supported|✓|✗|✗|✗|
|M7gd|||||||
|m7gd.medium|✓|✓|✓|✗|✗|✗|
|m7gd.large|✓|✓|✓|✗|✗|✗|
|m7gd.xlarge|✓|✓|✓|✗|✗|✗|
|m7gd.2xlarge|✓|✓|✓|✗|✗|✗|
|m7gd.4xlarge|✓|✓|✓|✗|✗|✗|
|m7gd.8xlarge|✓|✓|✓|✗|✗|✗|
|m7gd.12xlarge|✓|✓|✓|✗|✗|✗|
|m7gd.16xlarge|✓|✓|✓|✗|✗|✗|
|m7gd.metal|✓|✓|✓|✗|✗|✗|
|M7i|||||||


Security specifications 91


-----

|Instance type|EBS encryptio n|Instance store encryptio n|Encryptio n in transit|AMD SEV-SNP|NitroTPM|Nitro Enclaves|
|---|---|---|---|---|---|---|
|m7i.large|✓|Instance store not supported|✓|✗|✓|✗|
|m7i.xlarge|✓|Instance store not supported|✓|✗|✓|✗|
|m7i.2xlarge|✓|Instance store not supported|✓|✗|✓|✗|
|m7i.4xlarge|✓|Instance store not supported|✓|✗|✓|✗|
|m7i.8xlarge|✓|Instance store not supported|✓|✗|✓|✗|
|m7i.12xlarge|✓|Instance store not supported|✓|✗|✓|✗|
|m7i.16xlarge|✓|Instance store not supported|✓|✗|✓|✗|
|m7i.24xlarge|✓|Instance store not supported|✓|✗|✓|✗|


Security specifications 92


-----

|Instance type|EBS encryptio n|Instance store encryptio n|Encryptio n in transit|AMD SEV-SNP|NitroTPM|Nitro Enclaves|
|---|---|---|---|---|---|---|
|m7i.48xlarge|✓|Instance store not supported|✓|✗|✓|✗|
|m7i.metal-24xl|✓|Instance store not supported|✓|✗|✗|✗|
|m7i.metal-48xl|✓|Instance store not supported|✓|✗|✗|✗|
|M7i-flex|||||||
|m7i-flex.large|✓|Instance store not supported|✓|✗|✓|✗|
|m7i-flex.xlarge|✓|Instance store not supported|✓|✗|✓|✗|
|m7i-flex.2xlarge|✓|Instance store not supported|✓|✗|✓|✗|
|m7i-flex.4xlarge|✓|Instance store not supported|✓|✗|✓|✗|
|m7i-flex.8xlarge|✓|Instance store not supported|✓|✗|✓|✗|


Security specifications 93


-----

|Instance type EBS encryptio n Instance store encryptio n Encryptio n in transit AMD SEV-SNP NitroTPM Nitro Enclaves|Col2|Col3|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
|Mac1|||||||
|mac1.metal|✓|Instance store not supported|✗|✗|✗|✗|
|Mac2|||||||
|mac2.metal|✓|Instance store not supported|✗|✗|✗|✗|
|Mac2-m1ultra|||||||
|mac2-m1ul tra.metal|✓|Instance store not supported|✗|✗|✗|✗|
|Mac2-m2|||||||
|mac2-m2.metal|✓|Instance store not supported|✗|✗|✗|✗|
|Mac2-m2pro|||||||
|mac2-m2pr o.metal|✓|Instance store not supported|✗|✗|✗|✗|
|T2|||||||


Security specifications 94


-----

|Instance type|EBS encryptio n|Instance store encryptio n|Encryptio n in transit|AMD SEV-SNP|NitroTPM|Nitro Enclaves|
|---|---|---|---|---|---|---|
|t2.nano|✓|Instance store not supported|✗|✗|✗|✗|
|t2.micro|✓|Instance store not supported|✗|✗|✗|✗|
|t2.small|✓|Instance store not supported|✗|✗|✗|✗|
|t2.medium|✓|Instance store not supported|✗|✗|✗|✗|
|t2.large|✓|Instance store not supported|✗|✗|✗|✗|
|t2.xlarge|✓|Instance store not supported|✗|✗|✗|✗|
|t2.2xlarge|✓|Instance store not supported|✗|✗|✗|✗|
|T3|||||||
|t3.nano|✓|Instance store not supported|✗|✗|✓|✗|


Security specifications 95


-----

|Instance type|EBS encryptio n|Instance store encryptio n|Encryptio n in transit|AMD SEV-SNP|NitroTPM|Nitro Enclaves|
|---|---|---|---|---|---|---|
|t3.micro|✓|Instance store not supported|✗|✗|✓|✗|
|t3.small|✓|Instance store not supported|✗|✗|✓|✗|
|t3.medium|✓|Instance store not supported|✗|✗|✓|✗|
|t3.large|✓|Instance store not supported|✗|✗|✓|✗|
|t3.xlarge|✓|Instance store not supported|✗|✗|✓|✗|
|t3.2xlarge|✓|Instance store not supported|✗|✗|✓|✗|
|T3a|||||||
|t3a.nano|✓|Instance store not supported|✗|✗|✓|✗|
|t3a.micro|✓|Instance store not supported|✗|✗|✓|✗|


Security specifications 96


-----

|Instance type|EBS encryptio n|Instance store encryptio n|Encryptio n in transit|AMD SEV-SNP|NitroTPM|Nitro Enclaves|
|---|---|---|---|---|---|---|
|t3a.small|✓|Instance store not supported|✗|✗|✓|✗|
|t3a.medium|✓|Instance store not supported|✗|✗|✓|✗|
|t3a.large|✓|Instance store not supported|✗|✗|✓|✗|
|t3a.xlarge|✓|Instance store not supported|✗|✗|✓|✗|
|t3a.2xlarge|✓|Instance store not supported|✗|✗|✓|✗|
|T4g|||||||
|t4g.nano|✓|Instance store not supported|✗|✗|✗|✗|
|t4g.micro|✓|Instance store not supported|✗|✗|✗|✗|
|t4g.small|✓|Instance store not supported|✗|✗|✗|✗|


Security specifications 97


-----

|Instance type|EBS encryptio n|Instance store encryptio n|Encryptio n in transit|AMD SEV-SNP|NitroTPM|Nitro Enclaves|
|---|---|---|---|---|---|---|
|t4g.medium|✓|Instance store not supported|✗|✗|✗|✗|
|t4g.large|✓|Instance store not supported|✗|✗|✗|✗|
|t4g.xlarge|✓|Instance store not supported|✗|✗|✗|✗|
|t4g.2xlarge|✓|Instance store not supported|✗|✗|✗|✗|


### Specifications for Amazon EC2 compute optimized instances

Compute optimized instances are designed for compute intensive applications that benefit
from high performance processors. These instances are ideal for batch processing workloads,
media transcoding, high performance web servers, high performance computing (HPC), scientific
modeling, dedicated gaming servers, ad server engines, and machine learning inference.

For information on previous generation instance types of this category, such as C4 instances, see
Specifications for Amazon EC2 previous generation instances.

**Contents**

-  Available sizes

-  Platform summary

-  Performance specifications

-  Network specifications

Compute optimized 98


-----

-  Amazon EBS specifications

-  Instance store specifications

-  Security specifications

**Pricing**

[For pricing information, see Amazon EC2 On-Demand Pricing.](https://aws.amazon.com/ec2/pricing/on-demand/)

#### Available sizes

|Instance type|Available sizes|
|---|---|
|C5|c5.large | c5.xlarge | c5.2xlarge | c5.4xlarge | c5.9xlarge | c5.12xlarge | c5.18xlarge | c5.24xlarge | c5.metal|
|C5a|c5a.large | c5a.xlarge | c5a.2xlarge | c5a.4xlarge | c5a.8xlar ge | c5a.12xlarge | c5a.16xlarge | c5a.24xlarge|
|C5ad|c5ad.large | c5ad.xlarge | c5ad.2xlarge | c5ad.4xlarge | c5ad.8xlarge | c5ad.12xlarge | c5ad.16xlarge | c5ad.24xlarge|
|C5d|c5d.large | c5d.xlarge | c5d.2xlarge | c5d.4xlarge | c5d.9xlar ge | c5d.12xlarge | c5d.18xlarge | c5d.24xlarge | c5d.metal|
|C5n|c5n.large | c5n.xlarge | c5n.2xlarge | c5n.4xlarge | c5n.9xlar ge | c5n.18xlarge | c5n.metal|
|C6a|c6a.large | c6a.xlarge | c6a.2xlarge | c6a.4xlarge | c6a.8xlar ge | c6a.12xlarge | c6a.16xlarge | c6a.24xlarge | c6a.32xlarge | c6a.48xlarge | c6a.metal|
|C6g|c6g.medium | c6g.large | c6g.xlarge | c6g.2xlarge | c6g.4xlarge | c6g.8xlarge | c6g.12xlarge | c6g.16xlarge | c6g.metal|
|C6gd|c6gd.medium | c6gd.large | c6gd.xlarge | c6gd.2xlarge | c6gd.4xlarge | c6gd.8xlarge | c6gd.12xlarge | c6gd.16xlarge | c6gd.metal|



Available sizes 99


-----

|Instance type|Available sizes|
|---|---|
|C6gn|c6gn.medium | c6gn.large | c6gn.xlarge | c6gn.2xlarge | c6gn.4xlarge | c6gn.8xlarge | c6gn.12xlarge | c6gn.16xlarge|
|C6i|c6i.large | c6i.xlarge | c6i.2xlarge | c6i.4xlarge | c6i.8xlar ge | c6i.12xlarge | c6i.16xlarge | c6i.24xlarge | c6i.32xlarge | c6i.metal|
|C6id|c6id.large | c6id.xlarge | c6id.2xlarge | c6id.4xlarge | c6id.8xlarge | c6id.12xlarge | c6id.16xlarge | c6id.24xlarge | c6id.32xlarge | c6id.metal|
|C6in|c6in.large | c6in.xlarge | c6in.2xlarge | c6in.4xlarge | c6in.8xlarge | c6in.12xlarge | c6in.16xlarge | c6in.24xlarge | c6in.32xlarge | c6in.metal|
|C7a|c7a.medium | c7a.large | c7a.xlarge | c7a.2xlarge | c7a.4xlar ge | c7a.8xlarge | c7a.12xlarge | c7a.16xlarge | c7a.24xlarge | c7a.32xlarge | c7a.48xlarge | c7a.metal-48xl|
|C7g|c7g.medium | c7g.large | c7g.xlarge | c7g.2xlarge | c7g.4xlarge | c7g.8xlarge | c7g.12xlarge | c7g.16xlarge | c7g.metal|
|C7gd|c7gd.medium | c7gd.large | c7gd.xlarge | c7gd.2xlarge | c7gd.4xlarge | c7gd.8xlarge | c7gd.12xlarge | c7gd.16xlarge | c7gd.metal|
|C7gn|c7gn.medium | c7gn.large | c7gn.xlarge | c7gn.2xlarge | c7gn.4xlarge | c7gn.8xlarge | c7gn.12xlarge | c7gn.16xlarge | c7gn.metal|
|C7i|c7i.large | c7i.xlarge | c7i.2xlarge | c7i.4xlarge | c7i.8xlar ge | c7i.12xlarge | c7i.16xlarge | c7i.24xlarge | c7i.48xlarge | c7i.metal-24xl | c7i.metal-48xl|
|C7i-flex|c7i-flex.large | c7i-flex.xlarge | c7i-flex.2xlarge | c7i-flex. 4xlarge | c7i-flex.8xlarge|


Available sizes 100


-----

#### Platform summary

|Instance type|Hypervi r|soP rocessor type (architec ture)|Metal instances available|Dedicate Hosts support|dS pot support|Hibernati on support|Support operatin systems|
|---|---|---|---|---|---|---|---|
|C5|Nitro v2|Intel (x86_64)|✓|✓|✓|✓|Window | Linux|
|C5a|Nitro v2|AMD (x86_64)|✗|✗|✓|✗|Window | Linux|
|C5ad|Nitro v2|AMD (x86_64)|✗|✗|✓|✗|Window | Linux|
|C5d|Nitro v2|Intel (x86_64)|✓|✓|✓|✓|Window | Linux|
|C5n|Nitro v3|Intel (x86_64)|✓|✓|✓|✗|Window | Linux|
|C6a|Nitro v4|AMD (x86_64)|✓|✓|✓|✗|Window | Linux|
|C6g|Nitro v2|AWS Graviton (arm64)|✓|✓|✓|✓|Linux|
|C6gd|Nitro v2|AWS Graviton (arm64)|✓|✓|✓|✓|Linux|
|C6gn|Nitro v4|AWS Graviton (arm64)|✗|✓|✓|✓|Linux|
|C6i|Nitro v4|Intel (x86_64)|✓|✓|✓|✓|Window | Linux|



Platform summary 101


-----

**Instance**


**Hyperviso Processor**


**Metal**


**Dedicated Spot**


**Hibernati**


**Supported**

|type|r|type (architec ture)|instances available|Hosts support|support|on support|operatin systems|
|---|---|---|---|---|---|---|---|
|C6id|Nitro v4|Intel (x86_64)|✓|✓|✓|✓|Window | Linux|
|C6in|Nitro v4|Intel (x86_64)|✓|✓|✓|✗|Window | Linux|
|C7a|Nitro v4|AMD (x86_64)|✓|✓|✓|✓|Window | Linux|
|C7g|Nitro v4|AWS Graviton (arm64)|✓|✓|✓|✓|Linux|
|C7gd|Nitro v4|AWS Graviton (arm64)|✓|✓|✓|✓|Linux|
|C7gn|Nitro v5|AWS Graviton (arm64)|✓|✓|✓|✗|Linux|
|C7i|Nitro v4|Intel (x86_64)|✓|✓|✓|✓|Window | Linux|
|C7i- flex|Nitro v4|Intel (x86_64)|✗|✗|✓|✓|Window | Linux|


Platform summary 102


-----

#### Performance specifications

|Instance type|Burstabl|eMemor (GiB)|y Processor|vCPUs|CPU cores|Thread per core|s Accelerat ors|Acceler or memor|
|---|---|---|---|---|---|---|---|---|
|C5|||||||||
|c5.large|✗|4.00|Intel Xeon Platinum 8124M|2|1|2|✗|✗|
|c5.xlarge|✗|8.00|Intel Xeon Platinum 8124M|4|2|2|✗|✗|
|c5.2xlarge|✗|16.00|Intel Xeon Platinum 8124M|8|4|2|✗|✗|
|c5.4xlarge|✗|32.00|Intel Xeon Platinum 8124M|16|8|2|✗|✗|
|c5.9xlarge|✗|72.00|Intel Xeon Platinum 8124M|36|18|2|✗|✗|
|c5.12xlarge|✗|96.00|2nd Gen Intel Xeon Platinum 8275CL|48|24|2|✗|✗|
|c5.18xlarge|✗|144.00|Intel Xeon Platinum 8124M|72|36|2|✗|✗|
|c5.24xlarge|✗|192.00|2nd Gen Intel Xeon|96|48|2|✗|✗|



Performance specifications 103


-----

**Instance**


**BurstableMemory**


**Processor** **vCPUs CPU**


**Threads Accelerat**


**Accelerat**

|type|Col2|(GiB)|Col4|Col5|cores|per core|ors|or memor|
|---|---|---|---|---|---|---|---|---|
||||Platinum 8275CL||||||
|c5.metal|✗|192.00|2nd Gen Intel Xeon Platinum 8275CL|96|48|2|✗|✗|
|C5a|||||||||
|c5a.large|✗|4.00|2nd Gen AMD EPYC 7R32|2|1|2|✗|✗|
|c5a.xlarge|✗|8.00|2nd Gen AMD EPYC 7R32|4|2|2|✗|✗|
|c5a.2xlarge|✗|16.00|2nd Gen AMD EPYC 7R32|8|4|2|✗|✗|
|c5a.4xlarge|✗|32.00|2nd Gen AMD EPYC 7R32|16|8|2|✗|✗|
|c5a.8xlarge|✗|64.00|2nd Gen AMD EPYC 7R32|32|16|2|✗|✗|
|c5a.12xlarge|✗|96.00|2nd Gen AMD EPYC 7R32|48|24|2|✗|✗|
|c5a.16xlarge|✗|128.00|2nd Gen AMD EPYC 7R32|64|32|2|✗|✗|
|c5a.24xlarge|✗|192.00|2nd Gen AMD EPYC 7R32|96|48|2|✗|✗|
|C5ad|||||||||


Performance specifications 104


-----

**Instance**


**BurstableMemory**


**Processor** **vCPUs CPU**


**Threads Accelerat**


**Accelerat**

|type|Col2|(GiB)|Col4|Col5|cores|per core|ors|or memor|
|---|---|---|---|---|---|---|---|---|
|c5ad.large|✗|4.00|2nd Gen AMD EPYC 7R32|2|1|2|✗|✗|
|c5ad.xlarge|✗|8.00|2nd Gen AMD EPYC 7R32|4|2|2|✗|✗|
|c5ad.2xlarge|✗|16.00|2nd Gen AMD EPYC 7R32|8|4|2|✗|✗|
|c5ad.4xlarge|✗|32.00|2nd Gen AMD EPYC 7R32|16|8|2|✗|✗|
|c5ad.8xlarge|✗|64.00|2nd Gen AMD EPYC 7R32|32|16|2|✗|✗|
|c5ad.12xl arge|✗|96.00|2nd Gen AMD EPYC 7R32|48|24|2|✗|✗|
|c5ad.16xl arge|✗|128.00|2nd Gen AMD EPYC 7R32|64|32|2|✗|✗|
|c5ad.24xl arge|✗|192.00|2nd Gen AMD EPYC 7R32|96|48|2|✗|✗|
|C5d|||||||||
|c5d.large|✗|4.00|Intel Xeon Platinum 8124M|2|1|2|✗|✗|
|c5d.xlarge|✗|8.00|Intel Xeon Platinum 8124M|4|2|2|✗|✗|


Performance specifications 105


-----

**Instance**


**BurstableMemory**


**Processor** **vCPUs CPU**


**Threads Accelerat**


**Accelerat**

|type|Col2|(GiB)|Col4|Col5|cores|per core|ors|or memor|
|---|---|---|---|---|---|---|---|---|
|c5d.2xlarge|✗|16.00|Intel Xeon Platinum 8124M|8|4|2|✗|✗|
|c5d.4xlarge|✗|32.00|Intel Xeon Platinum 8124M|16|8|2|✗|✗|
|c5d.9xlarge|✗|72.00|Intel Xeon Platinum 8124M|36|18|2|✗|✗|
|c5d.12xlarge|✗|96.00|2nd Gen Intel Xeon Platinum 8275CL|48|24|2|✗|✗|
|c5d.18xlarge|✗|144.00|Intel Xeon Platinum 8124M|72|36|2|✗|✗|
|c5d.24xlarge|✗|192.00|2nd Gen Intel Xeon Platinum 8275CL|96|48|2|✗|✗|
|c5d.metal|✗|192.00|2nd Gen Intel Xeon Platinum 8275CL|96|48|2|✗|✗|
|C5n|||||||||


Performance specifications 106


-----

**Instance**


**BurstableMemory**


**Processor** **vCPUs CPU**


**Threads Accelerat**


**Accelerat**

|type|Col2|(GiB)|Col4|Col5|cores|per core|ors|or memor|
|---|---|---|---|---|---|---|---|---|
|c5n.large|✗|5.25|Intel Xeon Platinum 8124M|2|1|2|✗|✗|
|c5n.xlarge|✗|10.50|Intel Xeon Platinum 8124M|4|2|2|✗|✗|
|c5n.2xlarge|✗|21.00|Intel Xeon Platinum 8124M|8|4|2|✗|✗|
|c5n.4xlarge|✗|42.00|Intel Xeon Platinum 8124M|16|8|2|✗|✗|
|c5n.9xlarge|✗|96.00|Intel Xeon Platinum 8124M|36|18|2|✗|✗|
|c5n.18xlarge|✗|192.00|Intel Xeon Platinum 8124M|72|36|2|✗|✗|
|c5n.metal|✗|192.00|Intel Xeon Platinum 8124M|72|36|2|✗|✗|
|C6a|||||||||
|c6a.large|✗|4.00|AMD EPYC 7R13|2|1|2|✗|✗|
|c6a.xlarge|✗|8.00|AMD EPYC 7R13|4|2|2|✗|✗|


Performance specifications 107


-----

**Instance**


**BurstableMemory**


**Processor** **vCPUs CPU**


**Threads Accelerat**


**Accelerat**

|type|Col2|(GiB)|Col4|Col5|cores|per core|ors|or memor|
|---|---|---|---|---|---|---|---|---|
|c6a.2xlarge|✗|16.00|AMD EPYC 7R13|8|4|2|✗|✗|
|c6a.4xlarge|✗|32.00|AMD EPYC 7R13|16|8|2|✗|✗|
|c6a.8xlarge|✗|64.00|AMD EPYC 7R13|32|16|2|✗|✗|
|c6a.12xlarge|✗|96.00|AMD EPYC 7R13|48|24|2|✗|✗|
|c6a.16xlarge|✗|128.00|AMD EPYC 7R13|64|32|2|✗|✗|
|c6a.24xlarge|✗|192.00|AMD EPYC 7R13|96|48|2|✗|✗|
|c6a.32xlarge|✗|256.00|AMD EPYC 7R13|128|64|2|✗|✗|
|c6a.48xlarge|✗|384.00|AMD EPYC 7R13|192|96|2|✗|✗|
|c6a.metal|✗|384.00|AMD EPYC 7R13|192|96|2|✗|✗|
|C6g|||||||||
|c6g.medium|✗|2.00|AWS Graviton2 Processor|1|1|1|✗|✗|


Performance specifications 108


-----

**Instance**


**BurstableMemory**


**Processor** **vCPUs CPU**


**Threads Accelerat**


**Accelerat**

|type|Col2|(GiB)|Col4|Col5|cores|per core|ors|or memor|
|---|---|---|---|---|---|---|---|---|
|c6g.large|✗|4.00|AWS Graviton2 Processor|2|2|1|✗|✗|
|c6g.xlarge|✗|8.00|AWS Graviton2 Processor|4|4|1|✗|✗|
|c6g.2xlarge|✗|16.00|AWS Graviton2 Processor|8|8|1|✗|✗|
|c6g.4xlarge|✗|32.00|AWS Graviton2 Processor|16|16|1|✗|✗|
|c6g.8xlarge|✗|64.00|AWS Graviton2 Processor|32|32|1|✗|✗|
|c6g.12xlarge|✗|96.00|AWS Graviton2 Processor|48|48|1|✗|✗|
|c6g.16xlarge|✗|128.00|AWS Graviton2 Processor|64|64|1|✗|✗|
|c6g.metal|✗|128.00|AWS Graviton2 Processor|64|64|1|✗|✗|
|C6gd|||||||||


Performance specifications 109


-----

**Instance**


**BurstableMemory**


**Processor** **vCPUs CPU**


**Threads Accelerat**


**Accelerat**

|type|Col2|(GiB)|Col4|Col5|cores|per core|ors|or memor|
|---|---|---|---|---|---|---|---|---|
|c6gd.medi um|✗|2.00|AWS Graviton2 Processor|1|1|1|✗|✗|
|c6gd.large|✗|4.00|AWS Graviton2 Processor|2|2|1|✗|✗|
|c6gd.xlarge|✗|8.00|AWS Graviton2 Processor|4|4|1|✗|✗|
|c6gd.2xlarge|✗|16.00|AWS Graviton2 Processor|8|8|1|✗|✗|
|c6gd.4xlarge|✗|32.00|AWS Graviton2 Processor|16|16|1|✗|✗|
|c6gd.8xlarge|✗|64.00|AWS Graviton2 Processor|32|32|1|✗|✗|
|c6gd.12xl arge|✗|96.00|AWS Graviton2 Processor|48|48|1|✗|✗|
|c6gd.16xl arge|✗|128.00|AWS Graviton2 Processor|64|64|1|✗|✗|
|c6gd.metal|✗|128.00|AWS Graviton2 Processor|64|64|1|✗|✗|


Performance specifications 110


-----

|C6gn|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
|c6gn.medi um|✗|2.00|AWS Graviton2 Processor|1|1|1|✗|✗|
|c6gn.large|✗|4.00|AWS Graviton2 Processor|2|2|1|✗|✗|
|c6gn.xlarge|✗|8.00|AWS Graviton2 Processor|4|4|1|✗|✗|
|c6gn.2xlarge|✗|16.00|AWS Graviton2 Processor|8|8|1|✗|✗|
|c6gn.4xlarge|✗|32.00|AWS Graviton2 Processor|16|16|1|✗|✗|
|c6gn.8xlarge|✗|64.00|AWS Graviton2 Processor|32|32|1|✗|✗|
|c6gn.12xl arge|✗|96.00|AWS Graviton2 Processor|48|48|1|✗|✗|
|c6gn.16xl arge|✗|128.00|AWS Graviton2 Processor|64|64|1|✗|✗|
|C6i|||||||||


**Instance** **BurstableMemory Processor** **vCPUs CPU** **Threads Accelerat** **Accelerat**
**type** **(GiB)** **cores** **per** **ors** **or**

**core** **memory**

Performance specifications 111


-----

**Instance**


**BurstableMemory**


**Processor** **vCPUs CPU**


**Threads Accelerat**


**Accelerat**

|type|Col2|(GiB)|Col4|Col5|cores|per core|ors|or memor|
|---|---|---|---|---|---|---|---|---|
|c6i.large|✗|4.00|Intel Xeon Ice Lake|2|1|2|✗|✗|
|c6i.xlarge|✗|8.00|Intel Xeon Ice Lake|4|2|2|✗|✗|
|c6i.2xlarge|✗|16.00|Intel Xeon Ice Lake|8|4|2|✗|✗|
|c6i.4xlarge|✗|32.00|Intel Xeon Ice Lake|16|8|2|✗|✗|
|c6i.8xlarge|✗|64.00|Intel Xeon Ice Lake|32|16|2|✗|✗|
|c6i.12xlarge|✗|96.00|Intel Xeon Ice Lake|48|24|2|✗|✗|
|c6i.16xlarge|✗|128.00|Intel Xeon Ice Lake|64|32|2|✗|✗|
|c6i.24xlarge|✗|192.00|Intel Xeon Ice Lake|96|48|2|✗|✗|
|c6i.32xlarge|✗|256.00|Intel Xeon Ice Lake|128|64|2|✗|✗|
|c6i.metal|✗|256.00|Intel Xeon Ice Lake|128|64|2|✗|✗|
|C6id|||||||||
|c6id.large|✗|4.00|Intel Xeon Ice Lake|2|1|2|✗|✗|


Performance specifications 112


-----

**Instance**


**BurstableMemory**


**Processor** **vCPUs CPU**


**Threads Accelerat**


**Accelerat**

|type|Col2|(GiB)|Col4|Col5|cores|per core|ors|or memor|
|---|---|---|---|---|---|---|---|---|
|c6id.xlarge|✗|8.00|Intel Xeon Ice Lake|4|2|2|✗|✗|
|c6id.2xlarge|✗|16.00|Intel Xeon Ice Lake|8|4|2|✗|✗|
|c6id.4xlarge|✗|32.00|Intel Xeon Ice Lake|16|8|2|✗|✗|
|c6id.8xlarge|✗|64.00|Intel Xeon Ice Lake|32|16|2|✗|✗|
|c6id.12xl arge|✗|96.00|Intel Xeon Ice Lake|48|24|2|✗|✗|
|c6id.16xl arge|✗|128.00|Intel Xeon Ice Lake|64|32|2|✗|✗|
|c6id.24xl arge|✗|192.00|Intel Xeon Ice Lake|96|48|2|✗|✗|
|c6id.32xl arge|✗|256.00|Intel Xeon Ice Lake|128|64|2|✗|✗|
|c6id.metal|✗|256.00|Intel Xeon Ice Lake|128|64|2|✗|✗|
|C6in|||||||||
|c6in.large|✗|4.00|Intel Xeon Ice Lake|2|1|2|✗|✗|
|c6in.xlarge|✗|8.00|Intel Xeon Ice Lake|4|2|2|✗|✗|


Performance specifications 113


-----

**Instance**


**BurstableMemory**


**Processor** **vCPUs CPU**


**Threads Accelerat**


**Accelerat**

|type|Col2|(GiB)|Col4|Col5|cores|per core|ors|or memor|
|---|---|---|---|---|---|---|---|---|
|c6in.2xlarge|✗|16.00|Intel Xeon Ice Lake|8|4|2|✗|✗|
|c6in.4xlarge|✗|32.00|Intel Xeon Ice Lake|16|8|2|✗|✗|
|c6in.8xlarge|✗|64.00|Intel Xeon Ice Lake|32|16|2|✗|✗|
|c6in.12xl arge|✗|96.00|Intel Xeon Ice Lake|48|24|2|✗|✗|
|c6in.16xl arge|✗|128.00|Intel Xeon Ice Lake|64|32|2|✗|✗|
|c6in.24xl arge|✗|192.00|Intel Xeon Ice Lake|96|48|2|✗|✗|
|c6in.32xl arge|✗|256.00|Intel Xeon Ice Lake|128|64|2|✗|✗|
|c6in.metal|✗|256.00|Intel Xeon Ice Lake|128|64|2|✗|✗|
|C7a|||||||||
|c7a.medium|✗|2.00|AMD EPYC 9R14|1|1|1|✗|✗|
|c7a.large|✗|4.00|AMD EPYC 9R14|2|2|1|✗|✗|
|c7a.xlarge|✗|8.00|AMD EPYC 9R14|4|4|1|✗|✗|


Performance specifications 114


-----

**Instance**


**BurstableMemory**


**Processor** **vCPUs CPU**


**Threads Accelerat**


**Accelerat**

|type|Col2|(GiB)|Col4|Col5|cores|per core|ors|or memor|
|---|---|---|---|---|---|---|---|---|
|c7a.2xlarge|✗|16.00|AMD EPYC 9R14|8|8|1|✗|✗|
|c7a.4xlarge|✗|32.00|AMD EPYC 9R14|16|16|1|✗|✗|
|c7a.8xlarge|✗|64.00|AMD EPYC 9R14|32|32|1|✗|✗|
|c7a.12xlarge|✗|96.00|AMD EPYC 9R14|48|48|1|✗|✗|
|c7a.16xlarge|✗|128.00|AMD EPYC 9R14|64|64|1|✗|✗|
|c7a.24xlarge|✗|192.00|AMD EPYC 9R14|96|96|1|✗|✗|
|c7a.32xlarge|✗|256.00|AMD EPYC 9R14|128|128|1|✗|✗|
|c7a.48xlarge|✗|384.00|AMD EPYC 9R14|192|192|1|✗|✗|
|c7a.metal -48xl|✗|384.00|AMD EPYC 9R14|192|192|1|✗|✗|
|C7g|||||||||
|c7g.medium|✗|2.00|AWS Graviton3 Processor|1|1|1|✗|✗|


Performance specifications 115


-----

**Instance**


**BurstableMemory**


**Processor** **vCPUs CPU**


**Threads Accelerat**


**Accelerat**

|type|Col2|(GiB)|Col4|Col5|cores|per core|ors|or memor|
|---|---|---|---|---|---|---|---|---|
|c7g.large|✗|4.00|AWS Graviton3 Processor|2|2|1|✗|✗|
|c7g.xlarge|✗|8.00|AWS Graviton3 Processor|4|4|1|✗|✗|
|c7g.2xlarge|✗|16.00|AWS Graviton3 Processor|8|8|1|✗|✗|
|c7g.4xlarge|✗|32.00|AWS Graviton3 Processor|16|16|1|✗|✗|
|c7g.8xlarge|✗|64.00|AWS Graviton3 Processor|32|32|1|✗|✗|
|c7g.12xlarge|✗|96.00|AWS Graviton3 Processor|48|48|1|✗|✗|
|c7g.16xlarge|✗|128.00|AWS Graviton3 Processor|64|64|1|✗|✗|
|c7g.metal|✗|128.00|AWS Graviton3 Processor|64|64|1|✗|✗|
|C7gd|||||||||


Performance specifications 116


-----

**Instance**


**BurstableMemory**


**Processor** **vCPUs CPU**


**Threads Accelerat**


**Accelerat**

|type|Col2|(GiB)|Col4|Col5|cores|per core|ors|or memor|
|---|---|---|---|---|---|---|---|---|
|c7gd.medi um|✗|2.00|AWS Graviton3 Processor|1|1|1|✗|✗|
|c7gd.large|✗|4.00|AWS Graviton3 Processor|2|2|1|✗|✗|
|c7gd.xlarge|✗|8.00|AWS Graviton3 Processor|4|4|1|✗|✗|
|c7gd.2xlarge|✗|16.00|AWS Graviton3 Processor|8|8|1|✗|✗|
|c7gd.4xlarge|✗|32.00|AWS Graviton3 Processor|16|16|1|✗|✗|
|c7gd.8xlarge|✗|64.00|AWS Graviton3 Processor|32|32|1|✗|✗|
|c7gd.12xl arge|✗|96.00|AWS Graviton3 Processor|48|48|1|✗|✗|
|c7gd.16xl arge|✗|128.00|AWS Graviton3 Processor|64|64|1|✗|✗|
|c7gd.metal|✗|128.00|AWS Graviton3 Processor|64|64|1|✗|✗|


Performance specifications 117


-----

|C7gn|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
|c7gn.medi um|✗|2.00|AWS Graviton3E Processor|1|1|1|✗|✗|
|c7gn.large|✗|4.00|AWS Graviton3E Processor|2|2|1|✗|✗|
|c7gn.xlarge|✗|8.00|AWS Graviton3E Processor|4|4|1|✗|✗|
|c7gn.2xlarge|✗|16.00|AWS Graviton3E Processor|8|8|1|✗|✗|
|c7gn.4xlarge|✗|32.00|AWS Graviton3E Processor|16|16|1|✗|✗|
|c7gn.8xlarge|✗|64.00|AWS Graviton3E Processor|32|32|1|✗|✗|
|c7gn.12xl arge|✗|96.00|AWS Graviton3E Processor|48|48|1|✗|✗|
|c7gn.16xl arge|✗|128.00|AWS Graviton3E Processor|64|64|1|✗|✗|


**Instance** **BurstableMemory Processor** **vCPUs CPU** **Threads Accelerat** **Accelerat**
**type** **(GiB)** **cores** **per** **ors** **or**

**core** **memory**

Performance specifications 118


-----

**Instance**


**BurstableMemory**


**Processor** **vCPUs CPU**


**Threads Accelerat**


**Accelerat**

|type|Col2|(GiB)|Col4|Col5|cores|per core|ors|or memor|
|---|---|---|---|---|---|---|---|---|
|c7gn.metal|✗|128.00|AWS Graviton3E Processor|64|64|1|✗|✗|
|C7i|||||||||
|c7i.large|✗|4.00|Intel Xeon Sapphire Rapids|2|1|2|✗|✗|
|c7i.xlarge|✗|8.00|Intel Xeon Sapphire Rapids|4|2|2|✗|✗|
|c7i.2xlarge|✗|16.00|Intel Xeon Sapphire Rapids|8|4|2|✗|✗|
|c7i.4xlarge|✗|32.00|Intel Xeon Sapphire Rapids|16|8|2|✗|✗|
|c7i.8xlarge|✗|64.00|Intel Xeon Sapphire Rapids|32|16|2|✗|✗|
|c7i.12xlarge|✗|96.00|Intel Xeon Sapphire Rapids|48|24|2|✗|✗|
|c7i.16xlarge|✗|128.00|Intel Xeon Sapphire Rapids|64|32|2|✗|✗|


Performance specifications 119


-----

**Instance**


**BurstableMemory**


**Processor** **vCPUs CPU**


**Threads Accelerat**


**Accelerat**

|type|Col2|(GiB)|Col4|Col5|cores|per core|ors|or memor|
|---|---|---|---|---|---|---|---|---|
|c7i.24xlarge|✗|192.00|Intel Xeon Sapphire Rapids|96|48|2|✗|✗|
|c7i.48xlarge|✗|384.00|Intel Xeon Sapphire Rapids|192|96|2|✗|✗|
|c7i.metal -24xl|✗|192.00|Intel Xeon Sapphire Rapids|96|48|2|✗|✗|
|c7i.metal -48xl|✗|384.00|Intel Xeon Sapphire Rapids|192|96|2|✗|✗|
|C7i-flex|||||||||
|c7i-flex. large|✗|4.00|Intel Xeon Sapphire Rapids|2|1|2|✗|✗|
|c7i-flex. xlarge|✗|8.00|Intel Xeon Sapphire Rapids|4|2|2|✗|✗|
|c7i-flex. 2xlarge|✗|16.00|Intel Xeon Sapphire Rapids|8|4|2|✗|✗|
|c7i-flex. 4xlarge|✗|32.00|Intel Xeon Sapphire Rapids|16|8|2|✗|✗|


Performance specifications 120


-----

|c7i-flex. 8xlarge|✗|64.00|Intel Xeon Sapphire Rapids|32|16|2|✗|✗|
|---|---|---|---|---|---|---|---|---|


**Instance** **BurstableMemory Processor** **vCPUs CPU** **Threads Accelerat** **Accelerat**
**type** **(GiB)** **cores** **per** **ors** **or**

**core** **memory**

#### Network specifications

|Instance type|Baseline / Burst bandwidth (Gbps)|EFA|ENA|ENA Express|Network cards|Max. network interface s|IP addresses per interface|IPv6|
|---|---|---|---|---|---|---|---|---|
|C5|||||||||
|1 c5.large|0.75 / 10.0|✗|✓|✗|1|3|10|✓|
|1 c5.xlarge|1.25 / 10.0|✗|✓|✗|1|4|15|✓|
|1 c5.2xlarge|2.5 / 10.0|✗|✓|✗|1|4|15|✓|
|1 c5.4xlarge|5.0 / 10.0|✗|✓|✗|1|8|30|✓|
|c5.9xlarge|12 Gigabit|✗|✓|✗|1|8|30|✓|
|c5.12xlarge|12 Gigabit|✗|✓|✗|1|8|30|✓|
|c5.18xlarge|25 Gigabit|✗|✓|✗|1|15|50|✓|
|c5.24xlarge|25 Gigabit|✗|✓|✗|1|15|50|✓|
|c5.metal|25 Gigabit|✗|✓|✗|1|15|50|✓|
|C5a|||||||||
|1 c5a.large|0.75 / 10.0|✗|✓|✗|1|3|10|✓|



Network specifications 121


-----

|Col1|bandwidth (Gbps)|Col3|Col4|Col5|Col6|interface s|per interface|Col9|
|---|---|---|---|---|---|---|---|---|
|1 c5a.xlarge|1.25 / 10.0|✗|✓|✗|1|4|15|✓|
|1 c5a.2xlarge|2.5 / 10.0|✗|✓|✗|1|4|15|✓|
|1 c5a.4xlarge|5.0 / 10.0|✗|✓|✗|1|8|30|✓|
|c5a.8xlarge|10 Gigabit|✗|✓|✗|1|8|30|✓|
|c5a.12xlarge|12 Gigabit|✗|✓|✗|1|8|30|✓|
|c5a.16xlarge|20 Gigabit|✗|✓|✗|1|15|50|✓|
|c5a.24xlarge|20 Gigabit|✗|✓|✗|1|15|50|✓|
|C5ad|||||||||
|1 c5ad.large|0.75 / 10.0|✗|✓|✗|1|3|10|✓|
|1 c5ad.xlarge|1.25 / 10.0|✗|✓|✗|1|4|15|✓|
|1 c5ad.2xlarge|2.5 / 10.0|✗|✓|✗|1|4|15|✓|
|1 c5ad.4xlarge|5.0 / 10.0|✗|✓|✗|1|8|30|✓|
|c5ad.8xlarge|10 Gigabit|✗|✓|✗|1|8|30|✓|
|c5ad.12xlarge|12 Gigabit|✗|✓|✗|1|8|30|✓|
|c5ad.16xlarge|20 Gigabit|✗|✓|✗|1|15|50|✓|
|c5ad.24xlarge|20 Gigabit|✗|✓|✗|1|15|50|✓|
|C5d|||||||||
|1 c5d.large|0.75 / 10.0|✗|✓|✗|1|3|10|✓|
|1 c5d.xlarge|1.25 / 10.0|✗|✓|✗|1|4|15|✓|


**Instance type** **Baseline /** **EFA** **ENA** **ENA** **Network** **Max.** **IP** **IPv6**
**Burst** **Express** **cards** **network** **addresses**
**bandwidth** **interface** **per**
**(Gbps)** **s** **interface**


Network specifications 122


-----

|Col1|bandwidth (Gbps)|Col3|Col4|Col5|Col6|interface s|per interface|Col9|
|---|---|---|---|---|---|---|---|---|
|1 c5d.2xlarge|2.5 / 10.0|✗|✓|✗|1|4|15|✓|
|1 c5d.4xlarge|5.0 / 10.0|✗|✓|✗|1|8|30|✓|
|c5d.9xlarge|12 Gigabit|✗|✓|✗|1|8|30|✓|
|c5d.12xlarge|12 Gigabit|✗|✓|✗|1|8|30|✓|
|c5d.18xlarge|25 Gigabit|✗|✓|✗|1|15|50|✓|
|c5d.24xlarge|25 Gigabit|✗|✓|✗|1|15|50|✓|
|c5d.metal|25 Gigabit|✗|✓|✗|1|15|50|✓|
|C5n|||||||||
|1 c5n.large|3.0 / 25.0|✗|✓|✗|1|3|10|✓|
|1 c5n.xlarge|5.0 / 25.0|✗|✓|✗|1|4|15|✓|
|1 c5n.2xlarge|10.0 / 25.0|✗|✓|✗|1|4|15|✓|
|1 c5n.4xlarge|15.0 / 25.0|✗|✓|✗|1|8|30|✓|
|c5n.9xlarge|50 Gigabit|✓|✓|✗|1|8|30|✓|
|c5n.18xlarge|100 Gigabit|✓|✓|✗|1|15|50|✓|
|c5n.metal|100 Gigabit|✓|✓|✗|1|15|50|✓|
|C6a|||||||||
|1 c6a.large|0.781 / 12.5|✗|✓|✗|1|3|10|✓|
|1 c6a.xlarge|1.562 / 12.5|✗|✓|✗|1|4|15|✓|
|1 c6a.2xlarge|3.125 / 12.5|✗|✓|✗|1|4|15|✓|


**Instance type** **Baseline /** **EFA** **ENA** **ENA** **Network** **Max.** **IP** **IPv6**
**Burst** **Express** **cards** **network** **addresses**
**bandwidth** **interface** **per**
**(Gbps)** **s** **interface**


Network specifications 123


-----

|Col1|bandwidth (Gbps)|Col3|Col4|Col5|Col6|interface s|per interface|Col9|
|---|---|---|---|---|---|---|---|---|
|1 c6a.4xlarge|6.25 / 12.5|✗|✓|✗|1|8|30|✓|
|c6a.8xlarge|12.5 Gigabit|✗|✓|✗|1|8|30|✓|
|c6a.12xlarge|18.75 Gigabit|✗|✓|✓|1|8|30|✓|
|c6a.16xlarge|25 Gigabit|✗|✓|✓|1|15|50|✓|
|c6a.24xlarge|37.5 Gigabit|✗|✓|✓|1|15|50|✓|
|c6a.32xlarge|50 Gigabit|✗|✓|✓|1|15|50|✓|
|c6a.48xlarge|50 Gigabit|✓|✓|✓|1|15|50|✓|
|c6a.metal|50 Gigabit|✓|✓|✓|1|15|50|✓|
|C6g|||||||||
|1 c6g.medium|0.5 / 10.0|✗|✓|✗|1|2|4|✓|
|1 c6g.large|0.75 / 10.0|✗|✓|✗|1|3|10|✓|
|1 c6g.xlarge|1.25 / 10.0|✗|✓|✗|1|4|15|✓|
|1 c6g.2xlarge|2.5 / 10.0|✗|✓|✗|1|4|15|✓|
|1 c6g.4xlarge|5.0 / 10.0|✗|✓|✗|1|8|30|✓|
|c6g.8xlarge|12 Gigabit|✗|✓|✗|1|8|30|✓|
|c6g.12xlarge|20 Gigabit|✗|✓|✗|1|8|30|✓|
|c6g.16xlarge|25 Gigabit|✗|✓|✗|1|15|50|✓|
|c6g.metal|25 Gigabit|✗|✓|✗|1|15|50|✓|
|C6gd|||||||||


**Instance type** **Baseline /** **EFA** **ENA** **ENA** **Network** **Max.** **IP** **IPv6**
**Burst** **Express** **cards** **network** **addresses**
**bandwidth** **interface** **per**
**(Gbps)** **s** **interface**


Network specifications 124


-----

|Col1|bandwidth (Gbps)|Col3|Col4|Col5|Col6|interface s|per interface|Col9|
|---|---|---|---|---|---|---|---|---|
|c6gd.medium 1|0.5 / 10.0|✗|✓|✗|1|2|4|✓|
|1 c6gd.large|0.75 / 10.0|✗|✓|✗|1|3|10|✓|
|1 c6gd.xlarge|1.25 / 10.0|✗|✓|✗|1|4|15|✓|
|1 c6gd.2xlarge|2.5 / 10.0|✗|✓|✗|1|4|15|✓|
|1 c6gd.4xlarge|5.0 / 10.0|✗|✓|✗|1|8|30|✓|
|c6gd.8xlarge|12 Gigabit|✗|✓|✗|1|8|30|✓|
|c6gd.12xlarge|20 Gigabit|✗|✓|✗|1|8|30|✓|
|c6gd.16xlarge|25 Gigabit|✗|✓|✗|1|15|50|✓|
|c6gd.metal|25 Gigabit|✗|✓|✗|1|15|50|✓|
|C6gn|||||||||
|c6gn.medium 1|1.6 / 16.0|✗|✓|✗|1|2|4|✓|
|1 c6gn.large|3.0 / 25.0|✗|✓|✗|1|3|10|✓|
|1 c6gn.xlarge|6.3 / 25.0|✗|✓|✗|1|4|15|✓|
|1 c6gn.2xlarge|12.5 / 25.0|✗|✓|✗|1|4|15|✓|
|c6gn.4xlarge|25 Gigabit|✗|✓|✗|1|8|30|✓|
|c6gn.8xlarge|50 Gigabit|✗|✓|✗|1|8|30|✓|
|c6gn.12xlarge|75 Gigabit|✗|✓|✗|1|8|30|✓|


**Instance type** **Baseline /** **EFA** **ENA** **ENA** **Network** **Max.** **IP** **IPv6**
**Burst** **Express** **cards** **network** **addresses**
**bandwidth** **interface** **per**
**(Gbps)** **s** **interface**


Network specifications 125


-----

|Col1|bandwidth (Gbps)|Col3|Col4|Col5|Col6|interface s|per interface|Col9|
|---|---|---|---|---|---|---|---|---|
|c6gn.16xlarge|100 Gigabit|✓|✓|✓|1|15|50|✓|
|C6i|||||||||
|1 c6i.large|0.781 / 12.5|✗|✓|✗|1|3|10|✓|
|1 c6i.xlarge|1.562 / 12.5|✗|✓|✗|1|4|15|✓|
|1 c6i.2xlarge|3.125 / 12.5|✗|✓|✗|1|4|15|✓|
|1 c6i.4xlarge|6.25 / 12.5|✗|✓|✗|1|8|30|✓|
|c6i.8xlarge|12.5 Gigabit|✗|✓|✓|1|8|30|✓|
|c6i.12xlarge|18.75 Gigabit|✗|✓|✓|1|8|30|✓|
|c6i.16xlarge|25 Gigabit|✗|✓|✓|1|15|50|✓|
|c6i.24xlarge|37.5 Gigabit|✗|✓|✓|1|15|50|✓|
|c6i.32xlarge|50 Gigabit|✓|✓|✓|1|15|50|✓|
|c6i.metal|50 Gigabit|✓|✓|✓|1|15|50|✓|
|C6id|||||||||
|1 c6id.large|0.781 / 12.5|✗|✓|✗|1|3|10|✓|
|1 c6id.xlarge|1.562 / 12.5|✗|✓|✗|1|4|15|✓|
|1 c6id.2xlarge|3.125 / 12.5|✗|✓|✗|1|4|15|✓|
|1 c6id.4xlarge|6.25 / 12.5|✗|✓|✗|1|8|30|✓|
|c6id.8xlarge|12.5 Gigabit|✗|✓|✓|1|8|30|✓|
|c6id.12xlarge|18.75 Gigabit|✗|✓|✓|1|8|30|✓|


**Instance type** **Baseline /** **EFA** **ENA** **ENA** **Network** **Max.** **IP** **IPv6**
**Burst** **Express** **cards** **network** **addresses**
**bandwidth** **interface** **per**
**(Gbps)** **s** **interface**


Network specifications 126


-----

|Col1|bandwidth (Gbps)|Col3|Col4|Col5|Col6|interface s|per interface|Col9|
|---|---|---|---|---|---|---|---|---|
|c6id.16xlarge|25 Gigabit|✗|✓|✓|1|15|50|✓|
|c6id.24xlarge|37.5 Gigabit|✗|✓|✓|1|15|50|✓|
|c6id.32xlarge|50 Gigabit|✓|✓|✓|1|15|50|✓|
|c6id.metal|50 Gigabit|✓|✓|✓|1|15|50|✓|
|C6in|||||||||
|1 c6in.large|3.125 / 25.0|✗|✓|✗|1|3|10|✓|
|1 c6in.xlarge|6.25 / 30.0|✗|✓|✗|1|4|15|✓|
|1 c6in.2xlarge|12.5 / 40.0|✗|✓|✗|1|4|15|✓|
|1 c6in.4xlarge|25.0 / 50.0|✗|✓|✗|1|8|30|✓|
|c6in.8xlarge|50 Gigabit|✗|✓|✗|1|8|30|✓|
|c6in.12xlarge|75 Gigabit|✗|✓|✗|1|8|30|✓|
|c6in.16xlarge|100 Gigabit|✗|✓|✗|1|15|50|✓|
|c6in.24xlarge|150 Gigabit|✗|✓|✗|1|15|50|✓|
|c6in.32xlarge|200 Gigabit|✓|✓|✗|2|16|50|✓|
|c6in.metal|200 Gigabit|✓|✓|✗|2|16|50|✓|
|C7a|||||||||
|1 c7a.medium|0.39 / 12.5|✗|✓|✗|1|2|4|✓|
|1 c7a.large|0.781 / 12.5|✗|✓|✗|1|3|10|✓|
|1 c7a.xlarge|1.562 / 12.5|✗|✓|✗|1|4|15|✓|


**Instance type** **Baseline /** **EFA** **ENA** **ENA** **Network** **Max.** **IP** **IPv6**
**Burst** **Express** **cards** **network** **addresses**
**bandwidth** **interface** **per**
**(Gbps)** **s** **interface**


Network specifications 127


-----

|Col1|bandwidth (Gbps)|Col3|Col4|Col5|Col6|interface s|per interface|Col9|
|---|---|---|---|---|---|---|---|---|
|1 c7a.2xlarge|3.125 / 12.5|✗|✓|✗|1|4|15|✓|
|1 c7a.4xlarge|6.25 / 12.5|✗|✓|✗|1|8|30|✓|
|c7a.8xlarge|12.5 Gigabit|✗|✓|✗|1|8|30|✓|
|c7a.12xlarge|18.75 Gigabit|✗|✓|✗|1|8|30|✓|
|c7a.16xlarge|25 Gigabit|✗|✓|✗|1|15|50|✓|
|c7a.24xlarge|37.5 Gigabit|✗|✓|✗|1|15|50|✓|
|c7a.32xlarge|50 Gigabit|✗|✓|✗|1|15|50|✓|
|c7a.48xlarge|50 Gigabit|✓|✓|✗|1|15|50|✓|
|c7a.metal -48xl|50 Gigabit|✓|✓|✗|1|15|50|✓|
|C7g|||||||||
|1 c7g.medium|0.52 / 12.5|✗|✓|✗|1|2|4|✓|
|1 c7g.large|0.937 / 12.5|✗|✓|✗|1|3|10|✓|
|1 c7g.xlarge|1.876 / 12.5|✗|✓|✗|1|4|15|✓|
|1 c7g.2xlarge|3.75 / 15.0|✗|✓|✗|1|4|15|✓|
|1 c7g.4xlarge|7.5 / 15.0|✗|✓|✗|1|8|30|✓|
|c7g.8xlarge|15 Gigabit|✗|✓|✗|1|8|30|✓|
|c7g.12xlarge|22.5 Gigabit|✗|✓|✓|1|8|30|✓|
|c7g.16xlarge|30 Gigabit|✓|✓|✓|1|15|50|✓|


**Instance type** **Baseline /** **EFA** **ENA** **ENA** **Network** **Max.** **IP** **IPv6**
**Burst** **Express** **cards** **network** **addresses**
**bandwidth** **interface** **per**
**(Gbps)** **s** **interface**


Network specifications 128


-----

|Col1|bandwidth (Gbps)|Col3|Col4|Col5|Col6|interface s|per interface|Col9|
|---|---|---|---|---|---|---|---|---|
|c7g.metal|30 Gigabit|✓|✓|✓|1|15|50|✓|
|C7gd|||||||||
|c7gd.medium 1|0.52 / 12.5|✗|✓|✗|1|2|4|✓|
|1 c7gd.large|0.937 / 12.5|✗|✓|✗|1|3|10|✓|
|1 c7gd.xlarge|1.876 / 12.5|✗|✓|✗|1|4|15|✓|
|1 c7gd.2xlarge|3.75 / 15.0|✗|✓|✗|1|4|15|✓|
|1 c7gd.4xlarge|7.5 / 15.0|✗|✓|✗|1|8|30|✓|
|c7gd.8xlarge|15 Gigabit|✗|✓|✗|1|8|30|✓|
|c7gd.12xlarge|22.5 Gigabit|✗|✓|✓|1|8|30|✓|
|c7gd.16xlarge|30 Gigabit|✓|✓|✓|1|15|50|✓|
|c7gd.metal|30 Gigabit|✓|✓|✓|1|15|50|✓|
|C7gn|||||||||
|c7gn.medium 1|3.125 / 25.0|✗|✓|✗|1|2|4|✓|
|1 c7gn.large|6.25 / 30.0|✗|✓|✗|1|3|10|✓|
|1 c7gn.xlarge|12.5 / 40.0|✗|✓|✗|1|4|15|✓|
|1 c7gn.2xlarge|25.0 / 50.0|✗|✓|✗|1|4|15|✓|
|c7gn.4xlarge|50 Gigabit|✗|✓|✗|1|8|30|✓|


**Instance type** **Baseline /** **EFA** **ENA** **ENA** **Network** **Max.** **IP** **IPv6**
**Burst** **Express** **cards** **network** **addresses**
**bandwidth** **interface** **per**
**(Gbps)** **s** **interface**


Network specifications 129


-----

|Col1|bandwidth (Gbps)|Col3|Col4|Col5|Col6|interface s|per interface|Col9|
|---|---|---|---|---|---|---|---|---|
|c7gn.8xlarge|100 Gigabit|✗|✓|✗|1|8|30|✓|
|c7gn.12xlarge|150 Gigabit|✗|✓|✗|1|8|30|✓|
|c7gn.16xlarge|200 Gigabit|✓|✓|✗|1|15|50|✓|
|c7gn.metal|200 Gigabit|✓|✓|✗|1|15|50|✓|
|C7i|||||||||
|1 c7i.large|0.781 / 12.5|✗|✓|✗|1|3|10|✓|
|1 c7i.xlarge|1.562 / 12.5|✗|✓|✗|1|4|15|✓|
|1 c7i.2xlarge|3.125 / 12.5|✗|✓|✗|1|4|15|✓|
|1 c7i.4xlarge|6.25 / 12.5|✗|✓|✗|1|8|30|✓|
|c7i.8xlarge|12.5 Gigabit|✗|✓|✗|1|8|30|✓|
|c7i.12xlarge|18.75 Gigabit|✗|✓|✓|1|8|30|✓|
|c7i.16xlarge|25 Gigabit|✗|✓|✓|1|15|50|✓|
|c7i.24xlarge|37.5 Gigabit|✗|✓|✓|1|15|50|✓|
|c7i.48xlarge|50 Gigabit|✓|✓|✓|1|15|50|✓|
|c7i.metal-24xl|37.5 Gigabit|✗|✓|✓|1|15|50|✓|
|c7i.metal-48xl|50 Gigabit|✓|✓|✓|1|15|50|✓|
|C7i-flex|||||||||
|1 c7i-flex.large|0.39 / 12.5|✗|✓|✗|1|3|10|✓|


**Instance type** **Baseline /** **EFA** **ENA** **ENA** **Network** **Max.** **IP** **IPv6**
**Burst** **Express** **cards** **network** **addresses**
**bandwidth** **interface** **per**
**(Gbps)** **s** **interface**


Network specifications 130


-----

|Col1|bandwidth (Gbps)|Col3|Col4|Col5|Col6|interface s|per interface|Col9|
|---|---|---|---|---|---|---|---|---|
|c7i-flex.xlarge 1|0.781 / 12.5|✗|✓|✗|1|4|15|✓|
|c7i-flex. 1 2xlarge|1.562 / 12.5|✗|✓|✗|1|4|15|✓|
|c7i-flex. 1 4xlarge|3.125 / 12.5|✗|✓|✗|1|8|30|✓|
|c7i-flex. 1 8xlarge|6.25 / 12.5|✗|✓|✗|1|8|30|✓|


**Instance type** **Baseline /** **EFA** **ENA** **ENA** **Network** **Max.** **IP** **IPv6**
**Burst** **Express** **cards** **network** **addresses**
**bandwidth** **interface** **per**
**(Gbps)** **s** **interface**


**Note**

1
These instances have a baseline bandwidth and can use a network I/O credit mechanism
to burst beyond their baseline bandwidth on a best effort basis. Other instances types
[can sustain their maximum performance indefinitely. For more information, see instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-network-bandwidth.html)
[network bandwidth.](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-network-bandwidth.html)

For 32xlarge and metal instance types that support 200 Gbps, at least 2 ENIs, each
attached to a different network card, are required on the instance to achieve 200 Gbps
throughput. Each ENI attached to a network card can achieve a max of 170 Gbps.

#### Amazon EBS specifications

The following table indicates which instance types are Amazon EBS optimized by default and
which optionally support it. It also describes their EBS-optimized performance, including dedicated
bandwidth to Amazon EBS, the typical maximum aggregate throughput that can be achieved on
that dedicated connection with a streaming read workload and 128 KiB I/O size, and the maximum
IOPS the instance type can support when using a 16 KiB I/O size. Instance types not listed do not
support Amazon EBS optimization.

Amazon EBS specifications 131


-----

**Important**

An instance's EBS performance is bounded by the instance's performance limits, or
the aggregated performance of its attached volumes, whichever is smaller. To achieve
maximum EBS performance, an instance must have attached volumes that provide a
combined performance equal to or greater than the maximum instance performance. For

example, to achieve 80,000 IOPS for r6i.16xlarge, the instance must have at least 5
```
   gp3 volumes provisioned with 16,000 IOPS each (5 volumes x 16,000 IOPS = 80,000

```
IOPS).
We recommand that you choose an EBS–optimized instance type that provides more
dedicated Amazon EBS throughput than your application needs; otherwise, the connection
between Amazon EBS and Amazon EC2 can become a performance bottleneck.

|Instance type|Baseline / Maximum bandwidth (Mbps)|Baseline / Maximum throughput (MB/s, 128 KiB I/O)|Baseline / Maximum IOPS (16 KiB I/O)|NVMe|EBS optimization 2|
|---|---|---|---|---|---|
|C5||||||
|1 c5.large|650.00 / 4750.00|81.25 / 593.75|4000.00 / 20000.00|✓|default|
|1 c5.xlarge|1150.00 / 4750.00|143.75 / 593.75|6000.00 / 20000.00|✓|default|
|1 c5.2xlarge|2300.00 / 4750.00|287.50 / 593.75|10000.00 / 20000.00|✓|default|
|c5.4xlarge|4750.00|593.75|20000.00|✓|default|
|c5.9xlarge|9500.00|1187.50|40000.00|✓|default|
|c5.12xlarge|9500.00|1187.50|40000.00|✓|default|
|c5.18xlarge|19000.00|2375.00|80000.00|✓|default|



Amazon EBS specifications 132


-----

**Instance**


**Baseline /**


**Baseline /**


**Baseline /**


**NVMe** **EBS**

|type|Maximum bandwidth (Mbps)|Maximum throughput (MB/s, 128 KiB I/O)|Maximum IOPS (16 KiB I/O)|Col5|optimization 2|
|---|---|---|---|---|---|
|c5.24xlarge|19000.00|2375.00|80000.00|✓|default|
|c5.metal|19000.00|2375.00|80000.00|✓|default|
|C5a||||||
|1 c5a.large|200.00 / 3170.00|25.00 / 396.25|800.00 / 13300.00|✓|default|
|1 c5a.xlarge|400.00 / 3170.00|50.00 / 396.25|1600.00 / 13300.00|✓|default|
|1 c5a.2xlarge|800.00 / 3170.00|100.00 / 396.25|3200.00 / 13300.00|✓|default|
|1 c5a.4xlarge|1580.00 / 3170.00|197.50 / 396.25|6600.00 / 13300.00|✓|default|
|c5a.8xlarge|3170.00|396.25|13300.00|✓|default|
|c5a.12xlarge|4750.00|593.75|20000.00|✓|default|
|c5a.16xlarge|6300.00|787.50|26700.00|✓|default|
|c5a.24xlarge|9500.00|1187.50|40000.00|✓|default|
|C5ad||||||
|1 c5ad.large|200.00 / 3170.00|25.00 / 396.25|800.00 / 13300.00|✓|default|
|1 c5ad.xlarge|400.00 / 3170.00|50.00 / 396.25|1600.00 / 13300.00|✓|default|


Amazon EBS specifications 133


-----

**Instance**


**Baseline /**


**Baseline /**


**Baseline /**


**NVMe** **EBS**

|type|Maximum bandwidth (Mbps)|Maximum throughput (MB/s, 128 KiB I/O)|Maximum IOPS (16 KiB I/O)|Col5|optimization 2|
|---|---|---|---|---|---|
|c5ad.2xlarge 1|800.00 / 3170.00|100.00 / 396.25|3200.00 / 13300.00|✓|default|
|c5ad.4xlarge 1|1580.00 / 3170.00|197.50 / 396.25|6600.00 / 13300.00|✓|default|
|c5ad.8xlarge|3170.00|396.25|13300.00|✓|default|
|c5ad.12xl arge|4750.00|593.75|20000.00|✓|default|
|c5ad.16xl arge|6300.00|787.50|26700.00|✓|default|
|c5ad.24xl arge|9500.00|1187.50|40000.00|✓|default|
|C5d||||||
|1 c5d.large|650.00 / 4750.00|81.25 / 593.75|4000.00 / 20000.00|✓|default|
|1 c5d.xlarge|1150.00 / 4750.00|143.75 / 593.75|6000.00 / 20000.00|✓|default|
|1 c5d.2xlarge|2300.00 / 4750.00|287.50 / 593.75|10000.00 / 20000.00|✓|default|
|c5d.4xlarge|4750.00|593.75|20000.00|✓|default|
|c5d.9xlarge|9500.00|1187.50|40000.00|✓|default|
|c5d.12xlarge|9500.00|1187.50|40000.00|✓|default|


Amazon EBS specifications 134


-----

**Instance**


**Baseline /**


**Baseline /**


**Baseline /**


**NVMe** **EBS**

|type|Maximum bandwidth (Mbps)|Maximum throughput (MB/s, 128 KiB I/O)|Maximum IOPS (16 KiB I/O)|Col5|optimization 2|
|---|---|---|---|---|---|
|c5d.18xlarge|19000.00|2375.00|80000.00|✓|default|
|c5d.24xlarge|19000.00|2375.00|80000.00|✓|default|
|c5d.metal|19000.00|2375.00|80000.00|✓|default|
|C5n||||||
|1 c5n.large|650.00 / 4750.00|81.25 / 593.75|4000.00 / 20000.00|✓|default|
|1 c5n.xlarge|1150.00 / 4750.00|143.75 / 593.75|6000.00 / 20000.00|✓|default|
|1 c5n.2xlarge|2300.00 / 4750.00|287.50 / 593.75|10000.00 / 20000.00|✓|default|
|c5n.4xlarge|4750.00|593.75|20000.00|✓|default|
|c5n.9xlarge|9500.00|1187.50|40000.00|✓|default|
|c5n.18xlarge|19000.00|2375.00|80000.00|✓|default|
|c5n.metal|19000.00|2375.00|80000.00|✓|default|
|C6a||||||
|1 c6a.large|650.00 / 10000.00|81.25 / 1250.00|3600.00 / 40000.00|✓|default|
|1 c6a.xlarge|1250.00 / 10000.00|156.25 / 1250.00|6000.00 / 40000.00|✓|default|


Amazon EBS specifications 135


-----

**Instance**


**Baseline /**


**Baseline /**


**Baseline /**


**NVMe** **EBS**

|type|Maximum bandwidth (Mbps)|Maximum throughput (MB/s, 128 KiB I/O)|Maximum IOPS (16 KiB I/O)|Col5|optimization 2|
|---|---|---|---|---|---|
|1 c6a.2xlarge|2500.00 / 10000.00|312.50 / 1250.00|12000.00 / 40000.00|✓|default|
|1 c6a.4xlarge|5000.00 / 10000.00|625.00 / 1250.00|20000.00 / 40000.00|✓|default|
|c6a.8xlarge|10000.00|1250.00|40000.00|✓|default|
|c6a.12xlarge|15000.00|1875.00|60000.00|✓|default|
|c6a.16xlarge|20000.00|2500.00|80000.00|✓|default|
|c6a.24xlarge|30000.00|3750.00|120000.00|✓|default|
|c6a.32xlarge|40000.00|5000.00|160000.00|✓|default|
|c6a.48xlarge|40000.00|5000.00|240000.00|✓|default|
|c6a.metal|40000.00|5000.00|240000.00|✓|default|
|C6g||||||
|c6g.medium 1|315.00 / 4750.00|39.38 / 593.75|2500.00 / 20000.00|✓|default|
|1 c6g.large|630.00 / 4750.00|78.75 / 593.75|3600.00 / 20000.00|✓|default|
|1 c6g.xlarge|1188.00 / 4750.00|148.50 / 593.75|6000.00 / 20000.00|✓|default|
|1 c6g.2xlarge|2375.00 / 4750.00|296.88 / 593.75|12000.00 / 20000.00|✓|default|


Amazon EBS specifications 136


-----

**Instance**


**Baseline /**


**Baseline /**


**Baseline /**


**NVMe** **EBS**

|type|Maximum bandwidth (Mbps)|Maximum throughput (MB/s, 128 KiB I/O)|Maximum IOPS (16 KiB I/O)|Col5|optimization 2|
|---|---|---|---|---|---|
|c6g.4xlarge|4750.00|593.75|20000.00|✓|default|
|c6g.8xlarge|9500.00|1187.50|40000.00|✓|default|
|c6g.12xlarge|14250.00|1781.25|50000.00|✓|default|
|c6g.16xlarge|19000.00|2375.00|80000.00|✓|default|
|c6g.metal|19000.00|2375.00|80000.00|✓|default|
|C6gd||||||
|c6gd.medium 1|315.00 / 4750.00|39.38 / 593.75|2500.00 / 20000.00|✓|default|
|1 c6gd.large|630.00 / 4750.00|78.75 / 593.75|3600.00 / 20000.00|✓|default|
|1 c6gd.xlarge|1188.00 / 4750.00|148.50 / 593.75|6000.00 / 20000.00|✓|default|
|c6gd.2xlarge 1|2375.00 / 4750.00|296.88 / 593.75|12000.00 / 20000.00|✓|default|
|c6gd.4xlarge|4750.00|593.75|20000.00|✓|default|
|c6gd.8xlarge|9500.00|1187.50|40000.00|✓|default|
|c6gd.12xl arge|14250.00|1781.25|50000.00|✓|default|
|c6gd.16xl arge|19000.00|2375.00|80000.00|✓|default|


Amazon EBS specifications 137


-----

**Instance**


**Baseline /**


**Baseline /**


**Baseline /**


**NVMe** **EBS**

|type|Maximum bandwidth (Mbps)|Maximum throughput (MB/s, 128 KiB I/O)|Maximum IOPS (16 KiB I/O)|Col5|optimization 2|
|---|---|---|---|---|---|
|c6gd.metal|19000.00|2375.00|80000.00|✓|default|
|C6gn||||||
|c6gn.medium 1|760.00 / 9500.00|95.00 / 1187.50|2500.00 / 40000.00|✓|default|
|1 c6gn.large|1235.00 / 9500.00|154.38 / 1187.50|5000.00 / 40000.00|✓|default|
|1 c6gn.xlarge|2375.00 / 9500.00|296.88 / 1187.50|10000.00 / 40000.00|✓|default|
|c6gn.2xlarge 1|4750.00 / 9500.00|593.75 / 1187.50|20000.00 / 40000.00|✓|default|
|c6gn.4xlarge|9500.00|1187.50|40000.00|✓|default|
|c6gn.8xlarge|19000.00|2375.00|80000.00|✓|default|
|c6gn.12xl arge|28500.00|3562.50|120000.00|✓|default|
|c6gn.16xl arge|38000.00|4750.00|160000.00|✓|default|
|C6i||||||
|1 c6i.large|650.00 / 10000.00|81.25 / 1250.00|3600.00 / 40000.00|✓|default|
|1 c6i.xlarge|1250.00 / 10000.00|156.25 / 1250.00|6000.00 / 40000.00|✓|default|


Amazon EBS specifications 138


-----

**Instance**


**Baseline /**


**Baseline /**


**Baseline /**


**NVMe** **EBS**

|type|Maximum bandwidth (Mbps)|Maximum throughput (MB/s, 128 KiB I/O)|Maximum IOPS (16 KiB I/O)|Col5|optimization 2|
|---|---|---|---|---|---|
|1 c6i.2xlarge|2500.00 / 10000.00|312.50 / 1250.00|12000.00 / 40000.00|✓|default|
|1 c6i.4xlarge|5000.00 / 10000.00|625.00 / 1250.00|20000.00 / 40000.00|✓|default|
|c6i.8xlarge|10000.00|1250.00|40000.00|✓|default|
|c6i.12xlarge|15000.00|1875.00|60000.00|✓|default|
|c6i.16xlarge|20000.00|2500.00|80000.00|✓|default|
|c6i.24xlarge|30000.00|3750.00|120000.00|✓|default|
|c6i.32xlarge|40000.00|5000.00|160000.00|✓|default|
|c6i.metal|40000.00|5000.00|160000.00|✓|default|
|C6id||||||
|1 c6id.large|650.00 / 10000.00|81.25 / 1250.00|3600.00 / 40000.00|✓|default|
|1 c6id.xlarge|1250.00 / 10000.00|156.25 / 1250.00|6000.00 / 40000.00|✓|default|
|1 c6id.2xlarge|2500.00 / 10000.00|312.50 / 1250.00|12000.00 / 40000.00|✓|default|
|1 c6id.4xlarge|5000.00 / 10000.00|625.00 / 1250.00|20000.00 / 40000.00|✓|default|
|c6id.8xlarge|10000.00|1250.00|40000.00|✓|default|


Amazon EBS specifications 139


-----

**Instance**


**Baseline /**


**Baseline /**


**Baseline /**


**NVMe** **EBS**

|type|Maximum bandwidth (Mbps)|Maximum throughput (MB/s, 128 KiB I/O)|Maximum IOPS (16 KiB I/O)|Col5|optimization 2|
|---|---|---|---|---|---|
|c6id.12xlarge|15000.00|1875.00|60000.00|✓|default|
|c6id.16xlarge|20000.00|2500.00|80000.00|✓|default|
|c6id.24xlarge|30000.00|3750.00|120000.00|✓|default|
|c6id.32xlarge|40000.00|5000.00|160000.00|✓|default|
|c6id.metal|40000.00|5000.00|160000.00|✓|default|
|C6in||||||
|1 c6in.large|1562.00 / 25000.00|195.31 / 3125.00|6250.00 / 100000.00|✓|default|
|1 c6in.xlarge|3125.00 / 25000.00|390.62 / 3125.00|12500.00 / 100000.00|✓|default|
|1 c6in.2xlarge|6250.00 / 25000.00|781.25 / 3125.00|25000.00 / 100000.00|✓|default|
|1 c6in.4xlarge|12500.00 / 25000.00|1562.50 / 3125.00|50000.00 / 100000.00|✓|default|
|c6in.8xlarge|25000.00|3125.00|100000.00|✓|default|
|c6in.12xlarge|37500.00|4687.50|150000.00|✓|default|
|c6in.16xlarge|50000.00|6250.00|200000.00|✓|default|
|c6in.24xlarge|75000.00|9375.00|300000.00|✓|default|
|c6in.32xlarge|100000.00|12500.00|400000.00|✓|default|
|c6in.metal|100000.00|12500.00|400000.00|✓|default|


Amazon EBS specifications 140


-----

**Instance**


**Baseline /**


**Baseline /**


**Baseline /**


**NVMe** **EBS**

|type Maximum bandwidth (Mbps) Maximum throughput (MB/s, 128 KiB I/O) Maximum IOPS (16 KiB I/O) optimization 2|Col2|Col3|Col4|Col5|Col6|
|---|---|---|---|---|---|
|C7a||||||
|c7a.medium 1|325.00 / 10000.00|40.62 / 1250.00|2500.00 / 40000.00|✓|default|
|1 c7a.large|650.00 / 10000.00|81.25 / 1250.00|3600.00 / 40000.00|✓|default|
|1 c7a.xlarge|1250.00 / 10000.00|156.25 / 1250.00|6000.00 / 40000.00|✓|default|
|1 c7a.2xlarge|2500.00 / 10000.00|312.50 / 1250.00|12000.00 / 40000.00|✓|default|
|1 c7a.4xlarge|5000.00 / 10000.00|625.00 / 1250.00|20000.00 / 40000.00|✓|default|
|c7a.8xlarge|10000.00|1250.00|40000.00|✓|default|
|c7a.12xlarge|15000.00|1875.00|60000.00|✓|default|
|c7a.16xlarge|20000.00|2500.00|80000.00|✓|default|
|c7a.24xlarge|30000.00|3750.00|120000.00|✓|default|
|c7a.32xlarge|40000.00|5000.00|160000.00|✓|default|
|c7a.48xlarge|40000.00|5000.00|240000.00|✓|default|
|c7a.metal -48xl|40000.00|5000.00|240000.00|✓|default|
|C7g||||||


Amazon EBS specifications 141


-----

**Instance**


**Baseline /**


**Baseline /**


**Baseline /**


**NVMe** **EBS**

|type|Maximum bandwidth (Mbps)|Maximum throughput (MB/s, 128 KiB I/O)|Maximum IOPS (16 KiB I/O)|Col5|optimization 2|
|---|---|---|---|---|---|
|c7g.medium 1|315.00 / 10000.00|39.38 / 1250.00|2500.00 / 40000.00|✓|default|
|1 c7g.large|630.00 / 10000.00|78.75 / 1250.00|3600.00 / 40000.00|✓|default|
|1 c7g.xlarge|1250.00 / 10000.00|156.25 / 1250.00|6000.00 / 40000.00|✓|default|
|1 c7g.2xlarge|2500.00 / 10000.00|312.50 / 1250.00|12000.00 / 40000.00|✓|default|
|1 c7g.4xlarge|5000.00 / 10000.00|625.00 / 1250.00|20000.00 / 40000.00|✓|default|
|c7g.8xlarge|10000.00|1250.00|40000.00|✓|default|
|c7g.12xlarge|15000.00|1875.00|60000.00|✓|default|
|c7g.16xlarge|20000.00|2500.00|80000.00|✓|default|
|c7g.metal|20000.00|2500.00|80000.00|✓|default|
|C7gd||||||
|c7gd.medium 1|315.00 / 10000.00|39.38 / 1250.00|2500.00 / 40000.00|✓|default|
|1 c7gd.large|630.00 / 10000.00|78.75 / 1250.00|3600.00 / 40000.00|✓|default|
|1 c7gd.xlarge|1250.00 / 10000.00|156.25 / 1250.00|6000.00 / 40000.00|✓|default|


Amazon EBS specifications 142


-----

**Instance**


**Baseline /**


**Baseline /**


**Baseline /**


**NVMe** **EBS**

|type|Maximum bandwidth (Mbps)|Maximum throughput (MB/s, 128 KiB I/O)|Maximum IOPS (16 KiB I/O)|Col5|optimization 2|
|---|---|---|---|---|---|
|c7gd.2xlarge 1|2500.00 / 10000.00|312.50 / 1250.00|12000.00 / 40000.00|✓|default|
|c7gd.4xlarge 1|5000.00 / 10000.00|625.00 / 1250.00|20000.00 / 40000.00|✓|default|
|c7gd.8xlarge|10000.00|1250.00|40000.00|✓|default|
|c7gd.12xl arge|15000.00|1875.00|60000.00|✓|default|
|c7gd.16xl arge|20000.00|2500.00|80000.00|✓|default|
|c7gd.metal|20000.00|2500.00|80000.00|✓|default|
|C7gn||||||
|c7gn.medium 1|521.00 / 10000.00|65.12 / 1250.00|2083.00 / 40000.00|✓|default|
|1 c7gn.large|1042.00 / 10000.00|130.25 / 1250.00|4167.00 / 40000.00|✓|default|
|1 c7gn.xlarge|2083.00 / 10000.00|260.38 / 1250.00|8333.00 / 40000.00|✓|default|
|c7gn.2xlarge 1|4167.00 / 10000.00|520.88 / 1250.00|16667.00 / 40000.00|✓|default|
|c7gn.4xlarge 1|8333.00 / 10000.00|1041.62 / 1250.00|33333.00 / 40000.00|✓|default|


Amazon EBS specifications 143


-----

**Instance**


**Baseline /**


**Baseline /**


**Baseline /**


**NVMe** **EBS**

|type|Maximum bandwidth (Mbps)|Maximum throughput (MB/s, 128 KiB I/O)|Maximum IOPS (16 KiB I/O)|Col5|optimization 2|
|---|---|---|---|---|---|
|c7gn.8xlarge 1|16667.00 / 20000.00|2083.38 / 2500.00|66667.00 / 80000.00|✓|default|
|c7gn.12xl 1 arge|25000.00 / 30000.00|3125.00 / 3750.00|100000.00 / 120000.00|✓|default|
|c7gn.16xl 1 arge|33333.00 / 40000.00|4166.62 / 5000.00|133333.00 / 160000.00|✓|default|
|1 c7gn.metal|33333.00 / 40000.00|4166.62 / 5000.00|133333.00 / 160000.00|✓|default|
|C7i||||||
|1 c7i.large|650.00 / 10000.00|81.25 / 1250.00|3600.00 / 40000.00|✓|default|
|1 c7i.xlarge|1250.00 / 10000.00|156.25 / 1250.00|6000.00 / 40000.00|✓|default|
|1 c7i.2xlarge|2500.00 / 10000.00|312.50 / 1250.00|12000.00 / 40000.00|✓|default|
|1 c7i.4xlarge|5000.00 / 10000.00|625.00 / 1250.00|20000.00 / 40000.00|✓|default|
|c7i.8xlarge|10000.00|1250.00|40000.00|✓|default|
|c7i.12xlarge|15000.00|1875.00|60000.00|✓|default|
|c7i.16xlarge|20000.00|2500.00|80000.00|✓|default|
|c7i.24xlarge|30000.00|3750.00|120000.00|✓|default|


Amazon EBS specifications 144


-----

**Instance**

|type|Maximum bandwidth (Mbps)|Maximum throughput (MB/s, 128 KiB I/O)|Maximum IOPS (16 KiB I/O)|Col5|optimization 2|
|---|---|---|---|---|---|
|c7i.48xlarge|40000.00|5000.00|240000.00|✓|default|
|c7i.metal -24xl|30000.00|3750.00|120000.00|✓|default|
|c7i.metal -48xl|40000.00|5000.00|240000.00|✓|default|
|C7i-flex||||||
|c7i-flex.large 1|312.00 / 10000.00|39.06 / 1250.00|2500.00 / 40000.00|✓|default|
|c7i-flex. 1 xlarge|625.00 / 10000.00|78.12 / 1250.00|3600.00 / 40000.00|✓|default|
|c7i-flex. 1 2xlarge|1250.00 / 10000.00|156.25 / 1250.00|6000.00 / 40000.00|✓|default|
|c7i-flex. 1 4xlarge|2500.00 / 10000.00|312.50 / 1250.00|12000.00 / 40000.00|✓|default|
|c7i-flex. 1 8xlarge|5000.00 / 10000.00|625.00 / 1250.00|20000.00 / 40000.00|✓|default|



**Note**


**Baseline /**
**Maximum**
**bandwidth**
**(Mbps)**


**Baseline /**
**Maximum**
**throughput**
**(MB/s, 128**
**KiB I/O)**


**Baseline /**
**Maximum**
**IOPS (16 KiB**
**I/O)**


**NVMe** **EBS**
**optimization**


1
These instances can support maximum performance for 30 minutes at least once every 24
hours, after which they revert to their baseline performance. Other instances can sustain
the maximum performance indefinitely. If your workload requires sustained maximum
performance for longer than 30 minutes, use one of these instances.

Amazon EBS specifications 145


-----

2
```
   default indicates that instances are enabled for EBS optimization by default.
   supported indicates that instances can optionally be enabled for EBS optimization For

```
[more information, see Amazon EBS–optimized instances.](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-optimized.html)

#### Instance store specifications

The following table shows the instance store volume configuration for supported instance types,
along with the aggregated IOPS performance with 4,096 byte block size at queue depth saturation.

|Instance type|Instance store volumes|Instance store type|100% random read IOPS / Write IOPS|Needs initializ 1 ation|TRIM support 2|
|---|---|---|---|---|---|
|C5ad||||||
|c5ad.large|1 x 75 GB|NVMe SSD|16,283 / 7,105||✓|
|c5ad.xlarge|1 x 150 GB|NVMe SSD|32,566 / 14,211||✓|
|c5ad.2xlarge|1 x 300 GB|NVMe SSD|65,132 / 28,421||✓|
|c5ad.4xlarge|2 x 300 GB|NVMe SSD|130,262 / 56,842||✓|
|c5ad.8xlarge|2 x 600 GB|NVMe SSD|260,526 / 113,684||✓|
|c5ad.12xlarge|2 x 900 GB|NVMe SSD|412,500 / 180,000||✓|
|c5ad.16xlarge|2 x 1200 GB|NVMe SSD|521,052 / 227,368||✓|
|c5ad.24xlarge|2 x 1900 GB|NVMe SSD|825,000 / 360,000||✓|



Instance store specifications 146


-----

|Instance type Instance store volumes Instance store type 100% random read IOPS / Write IOPS Needs initializ ation 1 TRIM support 2|Col2|Col3|Col4|Col5|Col6|
|---|---|---|---|---|---|
|C5d||||||
|c5d.large|1 x 50 GB|NVMe SSD|20,000 / 9,000||✓|
|c5d.xlarge|1 x 100 GB|NVMe SSD|40,000 / 18,000||✓|
|c5d.2xlarge|1 x 200 GB|NVMe SSD|80,000 / 37,000||✓|
|c5d.4xlarge|1 x 400 GB|NVMe SSD|175,000 / 75,000||✓|
|c5d.9xlarge|1 x 900 GB|NVMe SSD|350,000 / 170,000||✓|
|c5d.12xlarge|2 x 900 GB|NVMe SSD|700,000 / 340,000||✓|
|c5d.18xlarge|2 x 900 GB|NVMe SSD|700,000 / 340,000||✓|
|c5d.24xlarge|4 x 900 GB|NVMe SSD|1,400,000 / 680,000||✓|
|c5d.metal|4 x 900 GB|NVMe SSD|1,400,000 / 680,000||✓|
|C6gd||||||
|c6gd.medium|1 x 59 GB|NVMe SSD|13,438 / 5,625||✓|
|c6gd.large|1 x 118 GB|NVMe SSD|26,875 / 11,250||✓|


Instance store specifications 147


-----

|Instance type|Instance store volumes|Instance store type|100% random read IOPS / Write IOPS|Needs initializ ation 1|TRIM support 2|
|---|---|---|---|---|---|
|c6gd.xlarge|1 x 237 GB|NVMe SSD|53,750 / 22,500||✓|
|c6gd.2xlarge|1 x 474 GB|NVMe SSD|107,500 / 45,000||✓|
|c6gd.4xlarge|1 x 950 GB|NVMe SSD|215,000 / 90,000||✓|
|c6gd.8xlarge|1 x 1900 GB|NVMe SSD|430,000 / 180,000||✓|
|c6gd.12xlarge|2 x 1425 GB|NVMe SSD|645,000 / 270,000||✓|
|c6gd.16xlarge|2 x 1900 GB|NVMe SSD|860,000 / 360,000||✓|
|c6gd.metal|2 x 1900 GB|NVMe SSD|860,000 / 360,000||✓|
|C6id||||||
|c6id.large|1 x 118 GB|NVMe SSD|33,542 / 16,771||✓|
|c6id.xlarge|1 x 237 GB|NVMe SSD|67,083 / 33,542||✓|
|c6id.2xlarge|1 x 474 GB|NVMe SSD|134,167 / 67,084||✓|
|c6id.4xlarge|1 x 950 GB|NVMe SSD|268,333 / 134,167||✓|


Instance store specifications 148


-----

|Instance type|Instance store volumes|Instance store type|100% random read IOPS / Write IOPS|Needs initializ ation 1|TRIM support 2|
|---|---|---|---|---|---|
|c6id.8xlarge|1 x 1900 GB|NVMe SSD|536,666 / 268,334||✓|
|c6id.12xlarge|2 x 1425 GB|NVMe SSD|804,998 / 402,500||✓|
|c6id.16xlarge|2 x 1900 GB|NVMe SSD|1,073,332 / 536,668||✓|
|c6id.24xlarge|4 x 1425 GB|NVMe SSD|1,609,996 / 805,000||✓|
|c6id.32xlarge|4 x 1900 GB|NVMe SSD|2,146,664 / 1,073,336||✓|
|c6id.metal|4 x 1900 GB|NVMe SSD|2,146,664 / 1,073,336||✓|
|C7gd||||||
|c7gd.medium|1 x 59 GB|NVMe SSD|16,771 / 8,385||✓|
|c7gd.large|1 x 118 GB|NVMe SSD|33,542 / 16,771||✓|
|c7gd.xlarge|1 x 237 GB|NVMe SSD|67,083 / 33,542||✓|
|c7gd.2xlarge|1 x 474 GB|NVMe SSD|134,167 / 67,084||✓|
|c7gd.4xlarge|1 x 950 GB|NVMe SSD|268,333 / 134,167||✓|


Instance store specifications 149


-----

|Instance type|Instance store volumes|Instance store type|100% random read IOPS / Write IOPS|Needs initializ ation 1|TRIM support 2|
|---|---|---|---|---|---|
|c7gd.8xlarge|1 x 1900 GB|NVMe SSD|536,666 / 268,334||✓|
|c7gd.12xlarge|2 x 1425 GB|NVMe SSD|804,998 / 402,500||✓|
|c7gd.16xlarge|2 x 1900 GB|NVMe SSD|1,073,332 / 536,668||✓|
|c7gd.metal|2 x 1900 GB|NVMe SSD|1,073,332 / 536,668||✓|


1
Volumes attached to certain instances suffer a first-write penalty unless initialized. For more
[information, see Optimize disk performance for instance store volumes.](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/disk-performance.html)

2
[For more information, see Instance store volume TRIM support.](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ssd-instance-store.html#InstanceStoreTrimSupport)

#### Security specifications

|Instance type|EBS encryptio n|Instance store encryptio n|Encryptio n in transit|AMD SEV-SNP|NitroTPM|Nitro Enclaves|
|---|---|---|---|---|---|---|
|C5|||||||
|c5.large|✓|Instance store not supported|✗|✗|✓|✗|
|c5.xlarge|✓|Instance store not supported|✗|✗|✓|✓|



Security specifications 150


-----

|Instance type|EBS encryptio n|Instance store encryptio n|Encryptio n in transit|AMD SEV-SNP|NitroTPM|Nitro Enclaves|
|---|---|---|---|---|---|---|
|c5.2xlarge|✓|Instance store not supported|✗|✗|✓|✓|
|c5.4xlarge|✓|Instance store not supported|✗|✗|✓|✓|
|c5.9xlarge|✓|Instance store not supported|✗|✗|✓|✓|
|c5.12xlarge|✓|Instance store not supported|✗|✗|✓|✓|
|c5.18xlarge|✓|Instance store not supported|✗|✗|✓|✓|
|c5.24xlarge|✓|Instance store not supported|✗|✗|✓|✓|
|c5.metal|✓|Instance store not supported|✗|✗|✗|✗|
|C5a|||||||
|c5a.large|✓|Instance store not supported|✓|✗|✓|✗|


Security specifications 151


-----

|Instance type|EBS encryptio n|Instance store encryptio n|Encryptio n in transit|AMD SEV-SNP|NitroTPM|Nitro Enclaves|
|---|---|---|---|---|---|---|
|c5a.xlarge|✓|Instance store not supported|✓|✗|✓|✓|
|c5a.2xlarge|✓|Instance store not supported|✓|✗|✓|✓|
|c5a.4xlarge|✓|Instance store not supported|✓|✗|✓|✓|
|c5a.8xlarge|✓|Instance store not supported|✓|✗|✓|✓|
|c5a.12xlarge|✓|Instance store not supported|✓|✗|✓|✓|
|c5a.16xlarge|✓|Instance store not supported|✓|✗|✓|✓|
|c5a.24xlarge|✓|Instance store not supported|✓|✗|✓|✓|
|C5ad|||||||
|c5ad.large|✓|✓|✓|✗|✓|✗|
|c5ad.xlarge|✓|✓|✓|✗|✓|✓|


Security specifications 152


-----

|Instance type|EBS encryptio n|Instance store encryptio n|Encryptio n in transit|AMD SEV-SNP|NitroTPM|Nitro Enclaves|
|---|---|---|---|---|---|---|
|c5ad.2xlarge|✓|✓|✓|✗|✓|✓|
|c5ad.4xlarge|✓|✓|✓|✗|✓|✓|
|c5ad.8xlarge|✓|✓|✓|✗|✓|✓|
|c5ad.12xlarge|✓|✓|✓|✗|✓|✓|
|c5ad.16xlarge|✓|✓|✓|✗|✓|✓|
|c5ad.24xlarge|✓|✓|✓|✗|✓|✓|
|C5d|||||||
|c5d.large|✓|✓|✗|✗|✓|✗|
|c5d.xlarge|✓|✓|✗|✗|✓|✓|
|c5d.2xlarge|✓|✓|✗|✗|✓|✓|
|c5d.4xlarge|✓|✓|✗|✗|✓|✓|
|c5d.9xlarge|✓|✓|✗|✗|✓|✓|
|c5d.12xlarge|✓|✓|✗|✗|✓|✓|
|c5d.18xlarge|✓|✓|✗|✗|✓|✓|
|c5d.24xlarge|✓|✓|✗|✗|✓|✓|
|c5d.metal|✓|✓|✗|✗|✗|✗|
|C5n|||||||


Security specifications 153


-----

|Instance type|EBS encryptio n|Instance store encryptio n|Encryptio n in transit|AMD SEV-SNP|NitroTPM|Nitro Enclaves|
|---|---|---|---|---|---|---|
|c5n.large|✓|Instance store not supported|✓|✗|✓|✗|
|c5n.xlarge|✓|Instance store not supported|✓|✗|✓|✓|
|c5n.2xlarge|✓|Instance store not supported|✓|✗|✓|✓|
|c5n.4xlarge|✓|Instance store not supported|✓|✗|✓|✓|
|c5n.9xlarge|✓|Instance store not supported|✓|✗|✓|✓|
|c5n.18xlarge|✓|Instance store not supported|✓|✗|✓|✓|
|c5n.metal|✓|Instance store not supported|✓|✗|✗|✗|
|C6a|||||||
|c6a.large|✓|Instance store not supported|✓|✓|✓|✗|


Security specifications 154


-----

|Instance type|EBS encryptio n|Instance store encryptio n|Encryptio n in transit|AMD SEV-SNP|NitroTPM|Nitro Enclaves|
|---|---|---|---|---|---|---|
|c6a.xlarge|✓|Instance store not supported|✓|✓|✓|✓|
|c6a.2xlarge|✓|Instance store not supported|✓|✓|✓|✓|
|c6a.4xlarge|✓|Instance store not supported|✓|✓|✓|✓|
|c6a.8xlarge|✓|Instance store not supported|✓|✓|✓|✓|
|c6a.12xlarge|✓|Instance store not supported|✓|✓|✓|✓|
|c6a.16xlarge|✓|Instance store not supported|✓|✓|✓|✓|
|c6a.24xlarge|✓|Instance store not supported|✓|✗|✓|✓|
|c6a.32xlarge|✓|Instance store not supported|✓|✗|✓|✓|


Security specifications 155


-----

|Instance type|EBS encryptio n|Instance store encryptio n|Encryptio n in transit|AMD SEV-SNP|NitroTPM|Nitro Enclaves|
|---|---|---|---|---|---|---|
|c6a.48xlarge|✓|Instance store not supported|✓|✗|✓|✓|
|c6a.metal|✓|Instance store not supported|✓|✗|✗|✗|
|C6g|||||||
|c6g.medium|✓|Instance store not supported|✗|✗|✗|✗|
|c6g.large|✓|Instance store not supported|✗|✗|✗|✓|
|c6g.xlarge|✓|Instance store not supported|✗|✗|✗|✓|
|c6g.2xlarge|✓|Instance store not supported|✗|✗|✗|✓|
|c6g.4xlarge|✓|Instance store not supported|✗|✗|✗|✓|
|c6g.8xlarge|✓|Instance store not supported|✗|✗|✗|✓|


Security specifications 156


-----

|Instance type|EBS encryptio n|Instance store encryptio n|Encryptio n in transit|AMD SEV-SNP|NitroTPM|Nitro Enclaves|
|---|---|---|---|---|---|---|
|c6g.12xlarge|✓|Instance store not supported|✗|✗|✗|✓|
|c6g.16xlarge|✓|Instance store not supported|✗|✗|✗|✓|
|c6g.metal|✓|Instance store not supported|✗|✗|✗|✗|
|C6gd|||||||
|c6gd.medium|✓|✓|✗|✗|✗|✗|
|c6gd.large|✓|✓|✗|✗|✗|✓|
|c6gd.xlarge|✓|✓|✗|✗|✗|✓|
|c6gd.2xlarge|✓|✓|✗|✗|✗|✓|
|c6gd.4xlarge|✓|✓|✗|✗|✗|✓|
|c6gd.8xlarge|✓|✓|✗|✗|✗|✓|
|c6gd.12xlarge|✓|✓|✗|✗|✗|✓|
|c6gd.16xlarge|✓|✓|✗|✗|✗|✓|
|c6gd.metal|✓|✓|✗|✗|✗|✗|
|C6gn|||||||


Security specifications 157


-----

|Instance type|EBS encryptio n|Instance store encryptio n|Encryptio n in transit|AMD SEV-SNP|NitroTPM|Nitro Enclaves|
|---|---|---|---|---|---|---|
|c6gn.medium|✓|Instance store not supported|✓|✗|✗|✗|
|c6gn.large|✓|Instance store not supported|✓|✗|✗|✓|
|c6gn.xlarge|✓|Instance store not supported|✓|✗|✗|✓|
|c6gn.2xlarge|✓|Instance store not supported|✓|✗|✗|✓|
|c6gn.4xlarge|✓|Instance store not supported|✓|✗|✗|✓|
|c6gn.8xlarge|✓|Instance store not supported|✓|✗|✗|✓|
|c6gn.12xlarge|✓|Instance store not supported|✓|✗|✗|✓|
|c6gn.16xlarge|✓|Instance store not supported|✓|✗|✗|✓|
|C6i|||||||


Security specifications 158


-----

|Instance type|EBS encryptio n|Instance store encryptio n|Encryptio n in transit|AMD SEV-SNP|NitroTPM|Nitro Enclaves|
|---|---|---|---|---|---|---|
|c6i.large|✓|Instance store not supported|✓|✗|✓|✗|
|c6i.xlarge|✓|Instance store not supported|✓|✗|✓|✓|
|c6i.2xlarge|✓|Instance store not supported|✓|✗|✓|✓|
|c6i.4xlarge|✓|Instance store not supported|✓|✗|✓|✓|
|c6i.8xlarge|✓|Instance store not supported|✓|✗|✓|✓|
|c6i.12xlarge|✓|Instance store not supported|✓|✗|✓|✓|
|c6i.16xlarge|✓|Instance store not supported|✓|✗|✓|✓|
|c6i.24xlarge|✓|Instance store not supported|✓|✗|✓|✓|


Security specifications 159


-----

|Instance type|EBS encryptio n|Instance store encryptio n|Encryptio n in transit|AMD SEV-SNP|NitroTPM|Nitro Enclaves|
|---|---|---|---|---|---|---|
|c6i.32xlarge|✓|Instance store not supported|✓|✗|✓|✓|
|c6i.metal|✓|Instance store not supported|✓|✗|✗|✗|
|C6id|||||||
|c6id.large|✓|✓|✓|✗|✓|✗|
|c6id.xlarge|✓|✓|✓|✗|✓|✓|
|c6id.2xlarge|✓|✓|✓|✗|✓|✓|
|c6id.4xlarge|✓|✓|✓|✗|✓|✓|
|c6id.8xlarge|✓|✓|✓|✗|✓|✓|
|c6id.12xlarge|✓|✓|✓|✗|✓|✓|
|c6id.16xlarge|✓|✓|✓|✗|✓|✓|
|c6id.24xlarge|✓|✓|✓|✗|✓|✓|
|c6id.32xlarge|✓|✓|✓|✗|✓|✓|
|c6id.metal|✓|✓|✓|✗|✗|✗|
|C6in|||||||
|c6in.large|✓|Instance store not supported|✓|✗|✓|✗|


Security specifications 160


-----

|Instance type|EBS encryptio n|Instance store encryptio n|Encryptio n in transit|AMD SEV-SNP|NitroTPM|Nitro Enclaves|
|---|---|---|---|---|---|---|
|c6in.xlarge|✓|Instance store not supported|✓|✗|✓|✓|
|c6in.2xlarge|✓|Instance store not supported|✓|✗|✓|✓|
|c6in.4xlarge|✓|Instance store not supported|✓|✗|✓|✓|
|c6in.8xlarge|✓|Instance store not supported|✓|✗|✓|✓|
|c6in.12xlarge|✓|Instance store not supported|✓|✗|✓|✓|
|c6in.16xlarge|✓|Instance store not supported|✓|✗|✓|✓|
|c6in.24xlarge|✓|Instance store not supported|✓|✗|✓|✓|
|c6in.32xlarge|✓|Instance store not supported|✓|✗|✓|✓|


Security specifications 161


-----

|Instance type|EBS encryptio n|Instance store encryptio n|Encryptio n in transit|AMD SEV-SNP|NitroTPM|Nitro Enclaves|
|---|---|---|---|---|---|---|
|c6in.metal|✓|Instance store not supported|✓|✗|✗|✗|
|C7a|||||||
|c7a.medium|✓|Instance store not supported|✓|✗|✓|✗|
|c7a.large|✓|Instance store not supported|✓|✗|✓|✗|
|c7a.xlarge|✓|Instance store not supported|✓|✗|✓|✗|
|c7a.2xlarge|✓|Instance store not supported|✓|✗|✓|✗|
|c7a.4xlarge|✓|Instance store not supported|✓|✗|✓|✗|
|c7a.8xlarge|✓|Instance store not supported|✓|✗|✓|✗|
|c7a.12xlarge|✓|Instance store not supported|✓|✗|✓|✗|


Security specifications 162


-----

|Instance type|EBS encryptio n|Instance store encryptio n|Encryptio n in transit|AMD SEV-SNP|NitroTPM|Nitro Enclaves|
|---|---|---|---|---|---|---|
|c7a.16xlarge|✓|Instance store not supported|✓|✗|✓|✗|
|c7a.24xlarge|✓|Instance store not supported|✓|✗|✓|✗|
|c7a.32xlarge|✓|Instance store not supported|✓|✗|✓|✗|
|c7a.48xlarge|✓|Instance store not supported|✓|✗|✓|✗|
|c7a.metal-48xl|✓|Instance store not supported|✓|✗|✗|✗|
|C7g|||||||
|c7g.medium|✓|Instance store not supported|✓|✗|✗|✗|
|c7g.large|✓|Instance store not supported|✓|✗|✗|✓|
|c7g.xlarge|✓|Instance store not supported|✓|✗|✗|✓|


Security specifications 163


-----

|Instance type|EBS encryptio n|Instance store encryptio n|Encryptio n in transit|AMD SEV-SNP|NitroTPM|Nitro Enclaves|
|---|---|---|---|---|---|---|
|c7g.2xlarge|✓|Instance store not supported|✓|✗|✗|✓|
|c7g.4xlarge|✓|Instance store not supported|✓|✗|✗|✓|
|c7g.8xlarge|✓|Instance store not supported|✓|✗|✗|✓|
|c7g.12xlarge|✓|Instance store not supported|✓|✗|✗|✓|
|c7g.16xlarge|✓|Instance store not supported|✓|✗|✗|✓|
|c7g.metal|✓|Instance store not supported|✓|✗|✗|✗|
|C7gd|||||||
|c7gd.medium|✓|✓|✓|✗|✗|✗|
|c7gd.large|✓|✓|✓|✗|✗|✗|
|c7gd.xlarge|✓|✓|✓|✗|✗|✗|
|c7gd.2xlarge|✓|✓|✓|✗|✗|✗|


Security specifications 164


-----

|Instance type|EBS encryptio n|Instance store encryptio n|Encryptio n in transit|AMD SEV-SNP|NitroTPM|Nitro Enclaves|
|---|---|---|---|---|---|---|
|c7gd.4xlarge|✓|✓|✓|✗|✗|✗|
|c7gd.8xlarge|✓|✓|✓|✗|✗|✗|
|c7gd.12xlarge|✓|✓|✓|✗|✗|✗|
|c7gd.16xlarge|✓|✓|✓|✗|✗|✗|
|c7gd.metal|✓|✓|✓|✗|✗|✗|
|C7gn|||||||
|c7gn.medium|✓|Instance store not supported|✓|✗|✗|✗|
|c7gn.large|✓|Instance store not supported|✓|✗|✗|✗|
|c7gn.xlarge|✓|Instance store not supported|✓|✗|✗|✗|
|c7gn.2xlarge|✓|Instance store not supported|✓|✗|✗|✗|
|c7gn.4xlarge|✓|Instance store not supported|✓|✗|✗|✗|


Security specifications 165


-----

|Instance type|EBS encryptio n|Instance store encryptio n|Encryptio n in transit|AMD SEV-SNP|NitroTPM|Nitro Enclaves|
|---|---|---|---|---|---|---|
|c7gn.8xlarge|✓|Instance store not supported|✓|✗|✗|✗|
|c7gn.12xlarge|✓|Instance store not supported|✓|✗|✗|✗|
|c7gn.16xlarge|✓|Instance store not supported|✓|✗|✗|✗|
|c7gn.metal|✓|Instance store not supported|✓|✗|✗|✗|
|C7i|||||||
|c7i.large|✓|Instance store not supported|✓|✗|✓|✗|
|c7i.xlarge|✓|Instance store not supported|✓|✗|✓|✗|
|c7i.2xlarge|✓|Instance store not supported|✓|✗|✓|✗|
|c7i.4xlarge|✓|Instance store not supported|✓|✗|✓|✗|


Security specifications 166


-----

|Instance type|EBS encryptio n|Instance store encryptio n|Encryptio n in transit|AMD SEV-SNP|NitroTPM|Nitro Enclaves|
|---|---|---|---|---|---|---|
|c7i.8xlarge|✓|Instance store not supported|✓|✗|✓|✗|
|c7i.12xlarge|✓|Instance store not supported|✓|✗|✓|✗|
|c7i.16xlarge|✓|Instance store not supported|✓|✗|✓|✗|
|c7i.24xlarge|✓|Instance store not supported|✓|✗|✓|✗|
|c7i.48xlarge|✓|Instance store not supported|✓|✗|✓|✗|
|c7i.metal-24xl|✓|Instance store not supported|✓|✗|✗|✗|
|c7i.metal-48xl|✓|Instance store not supported|✓|✗|✗|✗|
|C7i-flex|||||||
|c7i-flex.large|✓|Instance store not supported|✓|✗|✓|✗|


Security specifications 167


-----

|Instance type|EBS encryptio n|Instance store encryptio n|Encryptio n in transit|AMD SEV-SNP|NitroTPM|Nitro Enclaves|
|---|---|---|---|---|---|---|
|c7i-flex.xlarge|✓|Instance store not supported|✓|✗|✓|✗|
|c7i-flex.2xlarge|✓|Instance store not supported|✓|✗|✓|✗|
|c7i-flex.4xlarge|✓|Instance store not supported|✓|✗|✓|✗|
|c7i-flex.8xlarge|✓|Instance store not supported|✓|✗|✓|✗|


### Specifications for Amazon EC2 memory optimized instances

Memory optimized instances are designed to deliver fast performance for workloads that process
large data sets in memory.

For information on previous generation instance types of this category, such as R4 instances, see
Specifications for Amazon EC2 previous generation instances.

**Contents**

-  Available sizes

-  Platform summary

-  Performance specifications

-  Network specifications

-  Amazon EBS specifications

-  Instance store specifications

Memory optimized 168


-----

-  Security specifications

**Pricing**

[For pricing information, see Amazon EC2 On-Demand Pricing.](https://aws.amazon.com/ec2/pricing/on-demand/)

#### Available sizes

|Instance type|Available sizes|
|---|---|
|R5|r5.large | r5.xlarge | r5.2xlarge | r5.4xlarge | r5.8xlarge | r5.12xlarge | r5.16xlarge | r5.24xlarge | r5.metal|
|R5a|r5a.large | r5a.xlarge | r5a.2xlarge | r5a.4xlarge | r5a.8xlar ge | r5a.12xlarge | r5a.16xlarge | r5a.24xlarge|
|R5ad|r5ad.large | r5ad.xlarge | r5ad.2xlarge | r5ad.4xlarge | r5ad.8xlarge | r5ad.12xlarge | r5ad.16xlarge | r5ad.24xlarge|
|R5b|r5b.large | r5b.xlarge | r5b.2xlarge | r5b.4xlarge | r5b.8xlar ge | r5b.12xlarge | r5b.16xlarge | r5b.24xlarge | r5b.metal|
|R5d|r5d.large | r5d.xlarge | r5d.2xlarge | r5d.4xlarge | r5d.8xlar ge | r5d.12xlarge | r5d.16xlarge | r5d.24xlarge | r5d.metal|
|R5dn|r5dn.large | r5dn.xlarge | r5dn.2xlarge | r5dn.4xlarge | r5dn.8xlarge | r5dn.12xlarge | r5dn.16xlarge | r5dn.24xlarge | r5dn.metal|
|R5n|r5n.large | r5n.xlarge | r5n.2xlarge | r5n.4xlarge | r5n.8xlar ge | r5n.12xlarge | r5n.16xlarge | r5n.24xlarge | r5n.metal|
|R6a|r6a.large | r6a.xlarge | r6a.2xlarge | r6a.4xlarge | r6a.8xlar ge | r6a.12xlarge | r6a.16xlarge | r6a.24xlarge | r6a.32xlarge | r6a.48xlarge | r6a.metal|
|R6g|r6g.medium | r6g.large | r6g.xlarge | r6g.2xlarge | r6g.4xlarge | r6g.8xlarge | r6g.12xlarge | r6g.16xlarge | r6g.metal|



Available sizes 169


-----

|Instance type|Available sizes|
|---|---|
|R6gd|r6gd.medium | r6gd.large | r6gd.xlarge | r6gd.2xlarge | r6gd.4xlarge | r6gd.8xlarge | r6gd.12xlarge | r6gd.16xlarge | r6gd.metal|
|R6i|r6i.large | r6i.xlarge | r6i.2xlarge | r6i.4xlarge | r6i.8xlar ge | r6i.12xlarge | r6i.16xlarge | r6i.24xlarge | r6i.32xlarge | r6i.metal|
|R6idn|r6idn.large | r6idn.xlarge | r6idn.2xlarge | r6idn.4xlarge | r6idn.8xlarge | r6idn.12xlarge | r6idn.16xlarge | r6idn.24x large | r6idn.32xlarge | r6idn.metal|
|R6in|r6in.large | r6in.xlarge | r6in.2xlarge | r6in.4xlarge | r6in.8xlarge | r6in.12xlarge | r6in.16xlarge | r6in.24xlarge | r6in.32xlarge | r6in.metal|
|R6id|r6id.large | r6id.xlarge | r6id.2xlarge | r6id.4xlarge | r6id.8xlarge | r6id.12xlarge | r6id.16xlarge | r6id.24xlarge | r6id.32xlarge | r6id.metal|
|R7a|r7a.medium | r7a.large | r7a.xlarge | r7a.2xlarge | r7a.4xlar ge | r7a.8xlarge | r7a.12xlarge | r7a.16xlarge | r7a.24xlarge | r7a.32xlarge | r7a.48xlarge | r7a.metal-48xl|
|R7g|r7g.medium | r7g.large | r7g.xlarge | r7g.2xlarge | r7g.4xlarge | r7g.8xlarge | r7g.12xlarge | r7g.16xlarge | r7g.metal|
|R7gd|r7gd.medium | r7gd.large | r7gd.xlarge | r7gd.2xlarge | r7gd.4xlarge | r7gd.8xlarge | r7gd.12xlarge | r7gd.16xlarge | r7gd.metal|
|R7i|r7i.large | r7i.xlarge | r7i.2xlarge | r7i.4xlarge | r7i.8xlar ge | r7i.12xlarge | r7i.16xlarge | r7i.24xlarge | r7i.48xlarge | r7i.metal-24xl | r7i.metal-48xl|


Available sizes 170


-----

|Instance type|Available sizes|
|---|---|
|R7iz|r7iz.large | r7iz.xlarge | r7iz.2xlarge | r7iz.4xlarge | r7iz.8xlarge | r7iz.12xlarge | r7iz.16xlarge | r7iz.32xlarge | r7iz.metal-16xl | r7iz.metal-32xl|
|R8g|r8g.medium | r8g.large | r8g.xlarge | r8g.2xlarge | r8g.4xlar ge | r8g.8xlarge | r8g.12xlarge | r8g.16xlarge | r8g.24xlarge | r8g.48xlarge | r8g.metal-24xl | r8g.metal-48xl|
|U-3tb1|u-3tb1.56xlarge|
|U-6tb1|u-6tb1.56xlarge | u-6tb1.112xlarge | u-6tb1.metal|
|U-9tb1|u-9tb1.112xlarge | u-9tb1.metal|
|U-12tb1|u-12tb1.112xlarge | u-12tb1.metal|
|U-18tb1|u-18tb1.112xlarge | u-18tb1.metal|
|U-24tb1|u-24tb1.112xlarge | u-24tb1.metal|
|U7i-12tb|u7i-12tb.224xlarge|
|U7in-16tb|u7in-16tb.224xlarge|
|U7in-24tb|u7in-24tb.224xlarge|
|U7in-32tb|u7in-32tb.224xlarge|
|X1|x1.16xlarge | x1.32xlarge|
|X2gd|x2gd.medium | x2gd.large | x2gd.xlarge | x2gd.2xlarge | x2gd.4xlarge | x2gd.8xlarge | x2gd.12xlarge | x2gd.16xlarge | x2gd.metal|
|X2idn|x2idn.16xlarge | x2idn.24xlarge | x2idn.32xlarge | x2idn.metal|


Available sizes 171


-----

|Instance type|Available sizes|
|---|---|
|X2iedn|x2iedn.xlarge | x2iedn.2xlarge | x2iedn.4xlarge | x2iedn.8x large | x2iedn.16xlarge | x2iedn.24xlarge | x2iedn.32xlarge | x2iedn.metal|
|X2iezn|x2iezn.2xlarge | x2iezn.4xlarge | x2iezn.6xlarge | x2iezn.8x large | x2iezn.12xlarge | x2iezn.metal|
|X1e|x1e.xlarge | x1e.2xlarge | x1e.4xlarge | x1e.8xlarge | x1e.16xla rge | x1e.32xlarge|
|z1d|z1d.large | z1d.xlarge | z1d.2xlarge | z1d.3xlarge | z1d.6xlar ge | z1d.12xlarge | z1d.metal|


#### Platform summary

|Instance type|Hypervi r|soP rocessor type (architec ture)|Metal instances available|Dedicate Hosts support|dS pot support|Hibernati on support|Support operatin systems|
|---|---|---|---|---|---|---|---|
|R5|Nitro v2|Intel (x86_64)|✓|✓|✓|✓|Window | Linux|
|R5a|Nitro v2|AMD (x86_64)|✗|✓|✓|✓|Window | Linux|
|R5ad|Nitro v2|AMD (x86_64)|✗|✗|✓|✓|Window | Linux|
|R5b|Nitro v2|Intel (x86_64)|✓|✓|✓|✗|Window | Linux|
|R5d|Nitro v2|Intel (x86_64)|✓|✓|✓|✓|Window | Linux|



Platform summary 172


-----

**Instance**


**Hyperviso Processor**


**Metal**


**Dedicated Spot**


**Hibernati**


**Supported**

|type|r|type (architec ture)|instances available|Hosts support|support|on support|operatin systems|
|---|---|---|---|---|---|---|---|
|R5dn|Nitro v3|Intel (x86_64)|✓|✓|✓|✗|Window | Linux|
|R5n|Nitro v3|Intel (x86_64)|✓|✓|✓|✗|Window | Linux|
|R6a|Nitro v4|AMD (x86_64)|✓|✓|✓|✗|Window | Linux|
|R6g|Nitro v2|AWS Graviton (arm64)|✓|✓|✓|✓|Linux|
|R6gd|Nitro v2|AWS Graviton (arm64)|✓|✓|✓|✓|Linux|
|R6i|Nitro v4|Intel (x86_64)|✓|✓|✓|✗|Window | Linux|
|R6idn|Nitro v4|Intel (x86_64)|✓|✓|✓|✗|Window | Linux|
|R6in|Nitro v4|Intel (x86_64)|✓|✓|✓|✗|Window | Linux|
|R6id|Nitro v4|Intel (x86_64)|✓|✓|✓|✗|Window | Linux|
|R7a|Nitro v4|AMD (x86_64)|✓|✓|✓|✓|Window | Linux|


Platform summary 173


-----

**Instance**


**Hyperviso Processor**


**Metal**


**Dedicated Spot**


**Hibernati**


**Supported**

|type|r|type (architec ture)|instances available|Hosts support|support|on support|operatin systems|
|---|---|---|---|---|---|---|---|
|R7g|Nitro v4|AWS Graviton (arm64)|✓|✓|✓|✓|Linux|
|R7gd|Nitro v4|AWS Graviton (arm64)|✓|✓|✓|✓|Linux|
|R7i|Nitro v4|Intel (x86_64)|✓|✓|✓|✓|Window | Linux|
|R7iz|Nitro v4|Intel (x86_64)|✓|✓|✓|✓|Window | Linux|
|R8g|Nitro v5|AWS Graviton (arm64)|✓|✓|✓|✗|Linux|
|U-3tb1|Nitro v3|Intel (x86_64)|✗|✗|✗|✗|Window | Linux|
|U-6tb1|Nitro v3|Intel (x86_64)|✓|✓|✗|✗|Window | Linux|
|U-9tb1|Nitro v3|Intel (x86_64)|✓|✓|✗|✗|Window | Linux|
|U-12tb1|Nitro v3|Intel (x86_64)|✓|✓|✗|✗|Window | Linux|
|U-18tb1|Nitro v3|Intel (x86_64)|✓|✓|✗|✗|Window | Linux|


Platform summary 174


-----

**Instance**


**Hyperviso Processor**


**Metal**


**Dedicated Spot**


**Hibernati**


**Supported**

|type|r|type (architec ture)|instances available|Hosts support|support|on support|operatin systems|
|---|---|---|---|---|---|---|---|
|U-24tb1|Nitro v3|Intel (x86_64)|✓|✓|✗|✗|Window | Linux|
|U7i-12tb|Nitro v4|Intel (x86_64)|✗|✓|✗|✗|Window | Linux|
|U7in-16|tbNitro v4|Intel (x86_64)|✗|✓|✗|✗|Window | Linux|
|U7in-24|tbNitro v4|Intel (x86_64)|✗|✓|✗|✗|Window | Linux|
|U7in-32|tbNitro v4|Intel (x86_64)|✗|✓|✗|✗|Window | Linux|
|X1|Xen|Intel (x86_64)|✗|✓|✓|✗|Window | Linux|
|X2gd|Nitro v2|AWS Graviton (arm64)|✓|✓|✓|✗|Linux|
|X2idn|Nitro v4|Intel (x86_64)|✓|✓|✓|✗|Window | Linux|
|X2iedn|Nitro v4|Intel (x86_64)|✓|✓|✓|✗|Window | Linux|
|X2iezn|Nitro v3|Intel (x86_64)|✓|✓|✓|✗|Window | Linux|
|X1e|Xen|Intel (x86_64)|✗|✓|✓|✗|Window | Linux|


Platform summary 175


-----

|z1d|Nitro v2|Intel (x86_64)|✓|✓|✓|✗|Window | Linux|
|---|---|---|---|---|---|---|---|


**Instance** **Hyperviso Processor** **Metal** **Dedicated Spot** **Hibernati** **Supported**
**type** **r** **type** **instances** **Hosts** **support** **on support** **operating**

**(architec** **available** **support** **systems**
**ture)**


#### Performance specifications

|Instance type|Burstabl|eMemor (GiB)|y Processor|vCPUs|CPU cores|Thread per core|s Accelerat ors|Acceler or memor|
|---|---|---|---|---|---|---|---|---|
|R5|||||||||
|r5.large|✗|16.00|Intel Xeon Platinum 8175|2|1|2|✗|✗|
|r5.xlarge|✗|32.00|Intel Xeon Platinum 8175|4|2|2|✗|✗|
|r5.2xlarge|✗|64.00|Intel Xeon Platinum 8175|8|4|2|✗|✗|
|r5.4xlarge|✗|128.00|Intel Xeon Platinum 8175|16|8|2|✗|✗|
|r5.8xlarge|✗|256.00|Intel Xeon Platinum 8175|32|16|2|✗|✗|


Performance specifications 176


-----

**Instance**


**BurstableMemory**


**Processor** **vCPUs CPU**


**Threads Accelerat**


**Accelerat**

|type|Col2|(GiB)|Col4|Col5|cores|per core|ors|or memor|
|---|---|---|---|---|---|---|---|---|
|r5.12xlarge|✗|384.00|Intel Xeon Platinum 8175|48|24|2|✗|✗|
|r5.16xlarge|✗|512.00|Intel Xeon Platinum 8175|64|32|2|✗|✗|
|r5.24xlarge|✗|768.00|Intel Xeon Platinum 8175|96|48|2|✗|✗|
|r5.metal|✗|768.00|Intel Xeon Platinum 8175|96|48|2|✗|✗|
|R5a|||||||||
|r5a.large|✗|16.00|AMD EPYC 7571|2|1|2|✗|✗|
|r5a.xlarge|✗|32.00|AMD EPYC 7571|4|2|2|✗|✗|
|r5a.2xlarge|✗|64.00|AMD EPYC 7571|8|4|2|✗|✗|
|r5a.4xlarge|✗|128.00|AMD EPYC 7571|16|8|2|✗|✗|
|r5a.8xlarge|✗|256.00|AMD EPYC 7571|32|16|2|✗|✗|
|r5a.12xlarge|✗|384.00|AMD EPYC 7571|48|24|2|✗|✗|


Performance specifications 177


-----

**Instance**


**BurstableMemory**


**Processor** **vCPUs CPU**


**Threads Accelerat**


**Accelerat**

|type|Col2|(GiB)|Col4|Col5|cores|per core|ors|or memor|
|---|---|---|---|---|---|---|---|---|
|r5a.16xlarge|✗|512.00|AMD EPYC 7571|64|32|2|✗|✗|
|r5a.24xlarge|✗|768.00|AMD EPYC 7571|96|48|2|✗|✗|
|R5ad|||||||||
|r5ad.large|✗|16.00|AMD EPYC 7571|2|1|2|✗|✗|
|r5ad.xlarge|✗|32.00|AMD EPYC 7571|4|2|2|✗|✗|
|r5ad.2xlarge|✗|64.00|AMD EPYC 7571|8|4|2|✗|✗|
|r5ad.4xlarge|✗|128.00|AMD EPYC 7571|16|8|2|✗|✗|
|r5ad.8xlarge|✗|256.00|AMD EPYC 7571|32|16|2|✗|✗|
|r5ad.12xl arge|✗|384.00|AMD EPYC 7571|48|24|2|✗|✗|
|r5ad.16xl arge|✗|512.00|AMD EPYC 7571|64|32|2|✗|✗|
|r5ad.24xl arge|✗|768.00|AMD EPYC 7571|96|48|2|✗|✗|
|R5b|||||||||


Performance specifications 178


-----

**Instance**


**BurstableMemory**


**Processor** **vCPUs CPU**


**Threads Accelerat**


**Accelerat**

|type|Col2|(GiB)|Col4|Col5|cores|per core|ors|or memor|
|---|---|---|---|---|---|---|---|---|
|r5b.large|✗|16.00|Intel Xeon Platinum 8259|2|1|2|✗|✗|
|r5b.xlarge|✗|32.00|Intel Xeon Platinum 8259|4|2|2|✗|✗|
|r5b.2xlarge|✗|64.00|Intel Xeon Platinum 8259|8|4|2|✗|✗|
|r5b.4xlarge|✗|128.00|Intel Xeon Platinum 8259|16|8|2|✗|✗|
|r5b.8xlarge|✗|256.00|Intel Xeon Platinum 8259|32|16|2|✗|✗|
|r5b.12xlarge|✗|384.00|Intel Xeon Platinum 8259|48|24|2|✗|✗|
|r5b.16xlarge|✗|512.00|Intel Xeon Platinum 8259|64|32|2|✗|✗|
|r5b.24xlarge|✗|768.00|Intel Xeon Platinum 8259|96|48|2|✗|✗|
|r5b.metal|✗|768.00|Intel Xeon Platinum 8259|96|48|2|✗|✗|


Performance specifications 179


-----

|R5d|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
|r5d.large|✗|16.00|Intel Xeon Platinum 8175|2|1|2|✗|✗|
|r5d.xlarge|✗|32.00|Intel Xeon Platinum 8175|4|2|2|✗|✗|
|r5d.2xlarge|✗|64.00|Intel Xeon Platinum 8175|8|4|2|✗|✗|
|r5d.4xlarge|✗|128.00|Intel Xeon Platinum 8175|16|8|2|✗|✗|
|r5d.8xlarge|✗|256.00|Intel Xeon Platinum 8175|32|16|2|✗|✗|
|r5d.12xlarge|✗|384.00|Intel Xeon Platinum 8175|48|24|2|✗|✗|
|r5d.16xlarge|✗|512.00|Intel Xeon Platinum 8175|64|32|2|✗|✗|
|r5d.24xlarge|✗|768.00|Intel Xeon Platinum 8175|96|48|2|✗|✗|


**Instance** **BurstableMemory Processor** **vCPUs CPU** **Threads Accelerat** **Accelerat**
**type** **(GiB)** **cores** **per** **ors** **or**

**core** **memory**

Performance specifications 180


-----

**Instance**


**BurstableMemory**


**Processor** **vCPUs CPU**


**Threads Accelerat**


**Accelerat**

|type|Col2|(GiB)|Col4|Col5|cores|per core|ors|or memor|
|---|---|---|---|---|---|---|---|---|
|r5d.metal|✗|768.00|Intel Xeon Platinum 8175|96|48|2|✗|✗|
|R5dn|||||||||
|r5dn.large|✗|16.00|Intel Xeon Platinum 8259|2|1|2|✗|✗|
|r5dn.xlarge|✗|32.00|Intel Xeon Platinum 8259|4|2|2|✗|✗|
|r5dn.2xlarge|✗|64.00|Intel Xeon Platinum 8259|8|4|2|✗|✗|
|r5dn.4xlarge|✗|128.00|Intel Xeon Platinum 8259|16|8|2|✗|✗|
|r5dn.8xlarge|✗|256.00|Intel Xeon Platinum 8259|32|16|2|✗|✗|
|r5dn.12xl arge|✗|384.00|Intel Xeon Platinum 8259|48|24|2|✗|✗|
|r5dn.16xl arge|✗|512.00|Intel Xeon Platinum 8259|64|32|2|✗|✗|


Performance specifications 181


-----

**Instance**


**BurstableMemory**


**Processor** **vCPUs CPU**


**Threads Accelerat**


**Accelerat**

|type|Col2|(GiB)|Col4|Col5|cores|per core|ors|or memor|
|---|---|---|---|---|---|---|---|---|
|r5dn.24xl arge|✗|768.00|Intel Xeon Platinum 8259|96|48|2|✗|✗|
|r5dn.metal|✗|768.00|Intel Xeon Platinum 8259|96|48|2|✗|✗|
|R5n|||||||||
|r5n.large|✗|16.00|Intel Xeon Platinum 8259|2|1|2|✗|✗|
|r5n.xlarge|✗|32.00|Intel Xeon Platinum 8259|4|2|2|✗|✗|
|r5n.2xlarge|✗|64.00|Intel Xeon Platinum 8259|8|4|2|✗|✗|
|r5n.4xlarge|✗|128.00|Intel Xeon Platinum 8259|16|8|2|✗|✗|
|r5n.8xlarge|✗|256.00|Intel Xeon Platinum 8259|32|16|2|✗|✗|
|r5n.12xlarge|✗|384.00|Intel Xeon Platinum 8259|48|24|2|✗|✗|


Performance specifications 182


-----

**Instance**


**BurstableMemory**


**Processor** **vCPUs CPU**


**Threads Accelerat**


**Accelerat**

|type|Col2|(GiB)|Col4|Col5|cores|per core|ors|or memor|
|---|---|---|---|---|---|---|---|---|
|r5n.16xlarge|✗|512.00|Intel Xeon Platinum 8259|64|32|2|✗|✗|
|r5n.24xlarge|✗|768.00|Intel Xeon Platinum 8259|96|48|2|✗|✗|
|r5n.metal|✗|768.00|Intel Xeon Platinum 8259|96|48|2|✗|✗|
|R6a|||||||||
|r6a.large|✗|16.00|AMD EPYC 7R13|2|1|2|✗|✗|
|r6a.xlarge|✗|32.00|AMD EPYC 7R13|4|2|2|✗|✗|
|r6a.2xlarge|✗|64.00|AMD EPYC 7R13|8|4|2|✗|✗|
|r6a.4xlarge|✗|128.00|AMD EPYC 7R13|16|8|2|✗|✗|
|r6a.8xlarge|✗|256.00|AMD EPYC 7R13|32|16|2|✗|✗|
|r6a.12xlarge|✗|384.00|AMD EPYC 7R13|48|24|2|✗|✗|
|r6a.16xlarge|✗|512.00|AMD EPYC 7R13|64|32|2|✗|✗|


Performance specifications 183


-----

**Instance**


**BurstableMemory**


**Processor** **vCPUs CPU**


**Threads Accelerat**


**Accelerat**

|type|Col2|(GiB)|Col4|Col5|cores|per core|ors|or memor|
|---|---|---|---|---|---|---|---|---|
|r6a.24xlarge|✗|768.00|AMD EPYC 7R13|96|48|2|✗|✗|
|r6a.32xlarge|✗|1024.00|AMD EPYC 7R13|128|64|2|✗|✗|
|r6a.48xlarge|✗|1536.00|AMD EPYC 7R13|192|96|2|✗|✗|
|r6a.metal|✗|1536.00|AMD EPYC 7R13|192|96|2|✗|✗|
|R6g|||||||||
|r6g.medium|✗|8.00|AWS Graviton2 Processor|1|1|1|✗|✗|
|r6g.large|✗|16.00|AWS Graviton2 Processor|2|2|1|✗|✗|
|r6g.xlarge|✗|32.00|AWS Graviton2 Processor|4|4|1|✗|✗|
|r6g.2xlarge|✗|64.00|AWS Graviton2 Processor|8|8|1|✗|✗|
|r6g.4xlarge|✗|128.00|AWS Graviton2 Processor|16|16|1|✗|✗|


Performance specifications 184


-----

**Instance**


**BurstableMemory**


**Processor** **vCPUs CPU**


**Threads Accelerat**


**Accelerat**

|type|Col2|(GiB)|Col4|Col5|cores|per core|ors|or memor|
|---|---|---|---|---|---|---|---|---|
|r6g.8xlarge|✗|256.00|AWS Graviton2 Processor|32|32|1|✗|✗|
|r6g.12xlarge|✗|384.00|AWS Graviton2 Processor|48|48|1|✗|✗|
|r6g.16xlarge|✗|512.00|AWS Graviton2 Processor|64|64|1|✗|✗|
|r6g.metal|✗|512.00|AWS Graviton2 Processor|64|64|1|✗|✗|
|R6gd|||||||||
|r6gd.medi um|✗|8.00|AWS Graviton2 Processor|1|1|1|✗|✗|
|r6gd.large|✗|16.00|AWS Graviton2 Processor|2|2|1|✗|✗|
|r6gd.xlarge|✗|32.00|AWS Graviton2 Processor|4|4|1|✗|✗|
|r6gd.2xlarge|✗|64.00|AWS Graviton2 Processor|8|8|1|✗|✗|


Performance specifications 185


-----

**Instance**


**BurstableMemory**


**Processor** **vCPUs CPU**


**Threads Accelerat**


**Accelerat**

|type|Col2|(GiB)|Col4|Col5|cores|per core|ors|or memor|
|---|---|---|---|---|---|---|---|---|
|r6gd.4xlarge|✗|128.00|AWS Graviton2 Processor|16|16|1|✗|✗|
|r6gd.8xlarge|✗|256.00|AWS Graviton2 Processor|32|32|1|✗|✗|
|r6gd.12xl arge|✗|384.00|AWS Graviton2 Processor|48|48|1|✗|✗|
|r6gd.16xl arge|✗|512.00|AWS Graviton2 Processor|64|64|1|✗|✗|
|r6gd.metal|✗|512.00|AWS Graviton2 Processor|64|64|1|✗|✗|
|R6i|||||||||
|r6i.large|✗|16.00|Intel Xeon Ice Lake|2|1|2|✗|✗|
|r6i.xlarge|✗|32.00|Intel Xeon Ice Lake|4|2|2|✗|✗|
|r6i.2xlarge|✗|64.00|Intel Xeon Ice Lake|8|4|2|✗|✗|
|r6i.4xlarge|✗|128.00|Intel Xeon Ice Lake|16|8|2|✗|✗|


Performance specifications 186


-----

**Instance**


**BurstableMemory**


**Processor** **vCPUs CPU**


**Threads Accelerat**


**Accelerat**

|type|Col2|(GiB)|Col4|Col5|cores|per core|ors|or memor|
|---|---|---|---|---|---|---|---|---|
|r6i.8xlarge|✗|256.00|Intel Xeon Ice Lake|32|16|2|✗|✗|
|r6i.12xlarge|✗|384.00|Intel Xeon Ice Lake|48|24|2|✗|✗|
|r6i.16xlarge|✗|512.00|Intel Xeon Ice Lake|64|32|2|✗|✗|
|r6i.24xlarge|✗|768.00|Intel Xeon Ice Lake|96|48|2|✗|✗|
|r6i.32xlarge|✗|1024.00|Intel Xeon Ice Lake|128|64|2|✗|✗|
|r6i.metal|✗|1024.00|Intel Xeon Ice Lake|128|64|2|✗|✗|
|R6idn|||||||||
|r6idn.large|✗|16.00|Intel Xeon Ice Lake|2|1|2|✗|✗|
|r6idn.xlarge|✗|32.00|Intel Xeon Ice Lake|4|2|2|✗|✗|
|r6idn.2xl arge|✗|64.00|Intel Xeon Ice Lake|8|4|2|✗|✗|
|r6idn.4xl arge|✗|128.00|Intel Xeon Ice Lake|16|8|2|✗|✗|
|r6idn.8xl arge|✗|256.00|Intel Xeon Ice Lake|32|16|2|✗|✗|


Performance specifications 187


-----

**Instance**


**BurstableMemory**


**Processor** **vCPUs CPU**


**Threads Accelerat**


**Accelerat**

|type|Col2|(GiB)|Col4|Col5|cores|per core|ors|or memor|
|---|---|---|---|---|---|---|---|---|
|r6idn.12x large|✗|384.00|Intel Xeon Ice Lake|48|24|2|✗|✗|
|r6idn.16x large|✗|512.00|Intel Xeon Ice Lake|64|32|2|✗|✗|
|r6idn.24x large|✗|768.00|Intel Xeon Ice Lake|96|48|2|✗|✗|
|r6idn.32x large|✗|1024.00|Intel Xeon Ice Lake|128|64|2|✗|✗|
|r6idn.metal|✗|1024.00|Intel Xeon Ice Lake|128|64|2|✗|✗|
|R6in|||||||||
|r6in.large|✗|16.00|Intel Xeon Ice Lake|2|1|2|✗|✗|
|r6in.xlarge|✗|32.00|Intel Xeon Ice Lake|4|2|2|✗|✗|
|r6in.2xlarge|✗|64.00|Intel Xeon Ice Lake|8|4|2|✗|✗|
|r6in.4xlarge|✗|128.00|Intel Xeon Ice Lake|16|8|2|✗|✗|
|r6in.8xlarge|✗|256.00|Intel Xeon Ice Lake|32|16|2|✗|✗|
|r6in.12xl arge|✗|384.00|Intel Xeon Ice Lake|48|24|2|✗|✗|


Performance specifications 188


-----

**Instance**


**BurstableMemory**


**Processor** **vCPUs CPU**


**Threads Accelerat**


**Accelerat**

|type|Col2|(GiB)|Col4|Col5|cores|per core|ors|or memor|
|---|---|---|---|---|---|---|---|---|
|r6in.16xl arge|✗|512.00|Intel Xeon Ice Lake|64|32|2|✗|✗|
|r6in.24xl arge|✗|768.00|Intel Xeon Ice Lake|96|48|2|✗|✗|
|r6in.32xl arge|✗|1024.00|Intel Xeon Ice Lake|128|64|2|✗|✗|
|r6in.metal|✗|1024.00|Intel Xeon Ice Lake|128|64|2|✗|✗|
|R6id|||||||||
|r6id.large|✗|16.00|Intel Xeon Ice Lake|2|1|2|✗|✗|
|r6id.xlarge|✗|32.00|Intel Xeon Ice Lake|4|2|2|✗|✗|
|r6id.2xlarge|✗|64.00|Intel Xeon Ice Lake|8|4|2|✗|✗|
|r6id.4xlarge|✗|128.00|Intel Xeon Ice Lake|16|8|2|✗|✗|
|r6id.8xlarge|✗|256.00|Intel Xeon Ice Lake|32|16|2|✗|✗|
|r6id.12xl arge|✗|384.00|Intel Xeon Ice Lake|48|24|2|✗|✗|
|r6id.16xl arge|✗|512.00|Intel Xeon Ice Lake|64|32|2|✗|✗|


Performance specifications 189


-----

**Instance**


**BurstableMemory**


**Processor** **vCPUs CPU**


**Threads Accelerat**


**Accelerat**

|type|Col2|(GiB)|Col4|Col5|cores|per core|ors|or memor|
|---|---|---|---|---|---|---|---|---|
|r6id.24xl arge|✗|768.00|Intel Xeon Ice Lake|96|48|2|✗|✗|
|r6id.32xl arge|✗|1024.00|Intel Xeon Ice Lake|128|64|2|✗|✗|
|r6id.metal|✗|1024.00|Intel Xeon Ice Lake|128|64|2|✗|✗|
|R7a|||||||||
|r7a.medium|✗|8.00|AMD EPYC 9R14|1|1|1|✗|✗|
|r7a.large|✗|16.00|AMD EPYC 9R14|2|2|1|✗|✗|
|r7a.xlarge|✗|32.00|AMD EPYC 9R14|4|4|1|✗|✗|
|r7a.2xlarge|✗|64.00|AMD EPYC 9R14|8|8|1|✗|✗|
|r7a.4xlarge|✗|128.00|AMD EPYC 9R14|16|16|1|✗|✗|
|r7a.8xlarge|✗|256.00|AMD EPYC 9R14|32|32|1|✗|✗|
|r7a.12xlarge|✗|384.00|AMD EPYC 9R14|48|48|1|✗|✗|
|r7a.16xlarge|✗|512.00|AMD EPYC 9R14|64|64|1|✗|✗|


Performance specifications 190


-----

**Instance**


**BurstableMemory**


**Processor** **vCPUs CPU**


**Threads Accelerat**


**Accelerat**

|type|Col2|(GiB)|Col4|Col5|cores|per core|ors|or memor|
|---|---|---|---|---|---|---|---|---|
|r7a.24xlarge|✗|768.00|AMD EPYC 9R14|96|96|1|✗|✗|
|r7a.32xlarge|✗|1024.00|AMD EPYC 9R14|128|128|1|✗|✗|
|r7a.48xlarge|✗|1536.00|AMD EPYC 9R14|192|192|1|✗|✗|
|r7a.metal -48xl|✗|1536.00|AMD EPYC 9R14|192|192|1|✗|✗|
|R7g|||||||||
|r7g.medium|✗|8.00|AWS Graviton3 Processor|1|1|1|✗|✗|
|r7g.large|✗|16.00|AWS Graviton3 Processor|2|2|1|✗|✗|
|r7g.xlarge|✗|32.00|AWS Graviton3 Processor|4|4|1|✗|✗|
|r7g.2xlarge|✗|64.00|AWS Graviton3 Processor|8|8|1|✗|✗|
|r7g.4xlarge|✗|128.00|AWS Graviton3 Processor|16|16|1|✗|✗|


Performance specifications 191


-----

**Instance**


**BurstableMemory**


**Processor** **vCPUs CPU**


**Threads Accelerat**


**Accelerat**

|type|Col2|(GiB)|Col4|Col5|cores|per core|ors|or memor|
|---|---|---|---|---|---|---|---|---|
|r7g.8xlarge|✗|256.00|AWS Graviton3 Processor|32|32|1|✗|✗|
|r7g.12xlarge|✗|384.00|AWS Graviton3 Processor|48|48|1|✗|✗|
|r7g.16xlarge|✗|512.00|AWS Graviton3 Processor|64|64|1|✗|✗|
|r7g.metal|✗|512.00|AWS Graviton3 Processor|64|64|1|✗|✗|
|R7gd|||||||||
|r7gd.medi um|✗|8.00|AWS Graviton3 Processor|1|1|1|✗|✗|
|r7gd.large|✗|16.00|AWS Graviton3 Processor|2|2|1|✗|✗|
|r7gd.xlarge|✗|32.00|AWS Graviton3 Processor|4|4|1|✗|✗|
|r7gd.2xlarge|✗|64.00|AWS Graviton3 Processor|8|8|1|✗|✗|


Performance specifications 192


-----

**Instance**


**BurstableMemory**


**Processor** **vCPUs CPU**


**Threads Accelerat**


**Accelerat**

|type|Col2|(GiB)|Col4|Col5|cores|per core|ors|or memor|
|---|---|---|---|---|---|---|---|---|
|r7gd.4xlarge|✗|128.00|AWS Graviton3 Processor|16|16|1|✗|✗|
|r7gd.8xlarge|✗|256.00|AWS Graviton3 Processor|32|32|1|✗|✗|
|r7gd.12xl arge|✗|384.00|AWS Graviton3 Processor|48|48|1|✗|✗|
|r7gd.16xl arge|✗|512.00|AWS Graviton3 Processor|64|64|1|✗|✗|
|r7gd.metal|✗|512.00|AWS Graviton3 Processor|64|64|1|✗|✗|
|R7i|||||||||
|r7i.large|✗|16.00|Intel Xeon Sapphire Rapids|2|1|2|✗|✗|
|r7i.xlarge|✗|32.00|Intel Xeon Sapphire Rapids|4|2|2|✗|✗|
|r7i.2xlarge|✗|64.00|Intel Xeon Sapphire Rapids|8|4|2|✗|✗|


Performance specifications 193


-----

**Instance**


**BurstableMemory**


**Processor** **vCPUs CPU**


**Threads Accelerat**


**Accelerat**

|type|Col2|(GiB)|Col4|Col5|cores|per core|ors|or memor|
|---|---|---|---|---|---|---|---|---|
|r7i.4xlarge|✗|128.00|Intel Xeon Sapphire Rapids|16|8|2|✗|✗|
|r7i.8xlarge|✗|256.00|Intel Xeon Sapphire Rapids|32|16|2|✗|✗|
|r7i.12xlarge|✗|384.00|Intel Xeon Sapphire Rapids|48|24|2|✗|✗|
|r7i.16xlarge|✗|512.00|Intel Xeon Sapphire Rapids|64|32|2|✗|✗|
|r7i.24xlarge|✗|768.00|Intel Xeon Sapphire Rapids|96|48|2|✗|✗|
|r7i.48xlarge|✗|1536.00|Intel Xeon Sapphire Rapids|192|96|2|✗|✗|
|r7i.metal -24xl|✗|768.00|Intel Xeon Sapphire Rapids|96|48|2|✗|✗|
|r7i.metal -48xl|✗|1536.00|Intel Xeon Sapphire Rapids|192|96|2|✗|✗|
|R7iz|||||||||


Performance specifications 194


-----

**Instance**


**BurstableMemory**


**Processor** **vCPUs CPU**


**Threads Accelerat**


**Accelerat**

|type|Col2|(GiB)|Col4|Col5|cores|per core|ors|or memor|
|---|---|---|---|---|---|---|---|---|
|r7iz.large|✗|16.00|Intel Xeon Sapphire Rapids|2|1|2|✗|✗|
|r7iz.xlarge|✗|32.00|Intel Xeon Sapphire Rapids|4|2|2|✗|✗|
|r7iz.2xlarge|✗|64.00|Intel Xeon Sapphire Rapids|8|4|2|✗|✗|
|r7iz.4xlarge|✗|128.00|Intel Xeon Sapphire Rapids|16|8|2|✗|✗|
|r7iz.8xlarge|✗|256.00|Intel Xeon Sapphire Rapids|32|16|2|✗|✗|
|r7iz.12xl arge|✗|384.00|Intel Xeon Sapphire Rapids|48|24|2|✗|✗|
|r7iz.16xl arge|✗|512.00|Intel Xeon Sapphire Rapids|64|32|2|✗|✗|
|r7iz.32xl arge|✗|1024.00|Intel Xeon Sapphire Rapids|128|64|2|✗|✗|
|r7iz.meta l-16xl|✗|512.00|Intel Xeon Sapphire Rapids|64|32|2|✗|✗|


Performance specifications 195


-----

**Instance**


**BurstableMemory**


**Processor** **vCPUs CPU**


**Threads Accelerat**


**Accelerat**

|type|Col2|(GiB)|Col4|Col5|cores|per core|ors|or memor|
|---|---|---|---|---|---|---|---|---|
|r7iz.meta l-32xl|✗|1024.00|Intel Xeon Sapphire Rapids|128|64|2|✗|✗|
|R8g|||||||||
|r8g.medium|✗|8.00|AWS Graviton4 Processor|1|1|1|✗|✗|
|r8g.large|✗|16.00|AWS Graviton4 Processor|2|2|1|✗|✗|
|r8g.xlarge|✗|32.00|AWS Graviton4 Processor|4|4|1|✗|✗|
|r8g.2xlarge|✗|64.00|AWS Graviton4 Processor|8|8|1|✗|✗|
|r8g.4xlarge|✗|128.00|AWS Graviton4 Processor|16|16|1|✗|✗|
|r8g.8xlarge|✗|256.00|AWS Graviton4 Processor|32|32|1|✗|✗|
|r8g.12xlarge|✗|384.00|AWS Graviton4 Processor|48|48|1|✗|✗|


Performance specifications 196


-----

**Instance**


**BurstableMemory**


**Processor** **vCPUs CPU**


**Threads Accelerat**


**Accelerat**

|type|Col2|(GiB)|Col4|Col5|cores|per core|ors|or memor|
|---|---|---|---|---|---|---|---|---|
|r8g.16xlarge|✗|512.00|AWS Graviton4 Processor|64|64|1|✗|✗|
|r8g.24xlarge|✗|768.00|AWS Graviton4 Processor|96|96|1|✗|✗|
|r8g.48xlarge|✗|1536.00|AWS Graviton4 Processor|192|192|1|✗|✗|
|r8g.metal -24xl|✗|768.00|AWS Graviton4 Processor|96|96|1|✗|✗|
|r8g.metal -48xl|✗|1536.00|AWS Graviton4 Processor|192|192|1|✗|✗|
|U-3tb1|||||||||
|u-3tb1.56 xlarge|✗|3072.00|Intel Xeon Platinum 8176M|224|112|2|✗|✗|
|U-6tb1|||||||||
|u-6tb1.56 xlarge|✗|6144.00|Intel Xeon Platinum 8176M|224|224|1|✗|✗|
|u-6tb1.11 2xlarge|✗|6144.00|Intel Xeon Platinum 8176M|448|224|2|✗|✗|


Performance specifications 197


-----

**Instance**


**BurstableMemory**


**Processor** **vCPUs CPU**


**Threads Accelerat**


**Accelerat**

|type|Col2|(GiB)|Col4|Col5|cores|per core|ors|or memor|
|---|---|---|---|---|---|---|---|---|
|u-6tb1.me tal|✗|6144.00|Intel Xeon Platinum 8176M|448|224|2|✗|✗|
|U-9tb1|||||||||
|u-9tb1.11 2xlarge|✗|9216.00|Intel Xeon Platinum 8176M|448|224|2|✗|✗|
|u-9tb1.me tal|✗|9216.00|Intel Xeon Platinum 8176M|448|224|2|✗|✗|
|U-12tb1|||||||||
|u-12tb1.1 12xlarge|✗|12288.0|0Intel Xeon Platinum 8176M|448|224|2|✗|✗|
|u-12tb1.m etal|✗|12288.0|0Intel Xeon Platinum 8176M|448|224|2|✗|✗|
|U-18tb1|||||||||
|u-18tb1.1 12xlarge|✗|18432.0|0Intel Xeon Platinum 8280L|448|224|2|✗|✗|
|u-18tb1.m etal|✗|18432.0|0Intel Xeon Platinum 8280L|448|224|2|✗|✗|
|U-24tb1|||||||||


Performance specifications 198


-----

**Instance**


**BurstableMemory**


**Processor** **vCPUs CPU**


**Threads Accelerat**


**Accelerat**

|type|Col2|(GiB)|Col4|Col5|cores|per core|ors|or memor|
|---|---|---|---|---|---|---|---|---|
|u-24tb1.1 12xlarge|✗|24576.0|0Intel Xeon Platinum 8280L|448|224|2|✗|✗|
|u-24tb1.m etal|✗|24576.0|0Intel Xeon Platinum 8280L|448|224|2|✗|✗|
|U7i-12tb|||||||||
|u7i-12tb. 224xlarge|✗|12288.0|0Intel Xeon Sapphire Rapids|896|448|2|✗|✗|
|U7in-16tb|||||||||
|u7in-16tb .224xlarge|✗|16384.0|0Intel Xeon Sapphire Rapids|896|448|2|✗|✗|
|U7in-24tb|||||||||
|u7in-24tb .224xlarge|✗|24576.0|0Intel Xeon Sapphire Rapids|896|448|2|✗|✗|
|U7in-32tb|||||||||
|u7in-32tb .224xlarge|✗|32768.0|0Intel Xeon Sapphire Rapids|896|448|2|✗|✗|
|X1|||||||||


Performance specifications 199


-----

**Instance**


**BurstableMemory**


**Processor** **vCPUs CPU**


**Threads Accelerat**


**Accelerat**

|type|Col2|(GiB)|Col4|Col5|cores|per core|ors|or memor|
|---|---|---|---|---|---|---|---|---|
|x1.16xlarge|✗|976.00|Intel Xeon E7 8880 v3|64|32|2|✗|✗|
|x1.32xlarge|✗|1952.00|Intel Xeon E7 8880 v3|128|64|2|✗|✗|
|X2gd|||||||||
|x2gd.medi um|✗|16.00|AWS Graviton2 Processor|1|1|1|✗|✗|
|x2gd.large|✗|32.00|AWS Graviton2 Processor|2|2|1|✗|✗|
|x2gd.xlarge|✗|64.00|AWS Graviton2 Processor|4|4|1|✗|✗|
|x2gd.2xla rge|✗|128.00|AWS Graviton2 Processor|8|8|1|✗|✗|
|x2gd.4xla rge|✗|256.00|AWS Graviton2 Processor|16|16|1|✗|✗|
|x2gd.8xla rge|✗|512.00|AWS Graviton2 Processor|32|32|1|✗|✗|
|x2gd.12xl arge|✗|768.00|AWS Graviton2 Processor|48|48|1|✗|✗|


Performance specifications 200


-----

**Instance**


**BurstableMemory**


**Processor** **vCPUs CPU**


**Threads Accelerat**


**Accelerat**

|type|Col2|(GiB)|Col4|Col5|cores|per core|ors|or memor|
|---|---|---|---|---|---|---|---|---|
|x2gd.16xl arge|✗|1024.00|AWS Graviton2 Processor|64|64|1|✗|✗|
|x2gd.metal|✗|1024.00|AWS Graviton2 Processor|64|64|1|✗|✗|
|X2idn|||||||||
|x2idn.16x large|✗|1024.00|Intel Xeon Ice Lake|64|32|2|✗|✗|
|x2idn.24x large|✗|1536.00|Intel Xeon Ice Lake|96|48|2|✗|✗|
|x2idn.32x large|✗|2048.00|Intel Xeon Ice Lake|128|64|2|✗|✗|
|x2idn.metal|✗|2048.00|Intel Xeon Ice Lake|128|64|2|✗|✗|
|X2iedn|||||||||
|x2iedn.xl arge|✗|128.00|Intel Xeon Ice Lake|4|2|2|✗|✗|
|x2iedn.2x large|✗|256.00|Intel Xeon Ice Lake|8|4|2|✗|✗|
|x2iedn.4x large|✗|512.00|Intel Xeon Ice Lake|16|8|2|✗|✗|
|x2iedn.8x large|✗|1024.00|Intel Xeon Ice Lake|32|16|2|✗|✗|


Performance specifications 201


-----

**Instance**


**BurstableMemory**


**Processor** **vCPUs CPU**


**Threads Accelerat**


**Accelerat**

|type|Col2|(GiB)|Col4|Col5|cores|per core|ors|or memor|
|---|---|---|---|---|---|---|---|---|
|x2iedn.16 xlarge|✗|2048.00|Intel Xeon Ice Lake|64|32|2|✗|✗|
|x2iedn.24 xlarge|✗|3072.00|Intel Xeon Ice Lake|96|48|2|✗|✗|
|x2iedn.32 xlarge|✗|4096.00|Intel Xeon Ice Lake|128|64|2|✗|✗|
|x2iedn.me tal|✗|4096.00|Intel Xeon Ice Lake|128|64|2|✗|✗|
|X2iezn|||||||||
|x2iezn.2x large|✗|256.00|Intel Xeon Platinum 8252|8|4|2|✗|✗|
|x2iezn.4x large|✗|512.00|Intel Xeon Platinum 8252|16|8|2|✗|✗|
|x2iezn.6x large|✗|768.00|Intel Xeon Platinum 8252|24|12|2|✗|✗|
|x2iezn.8x large|✗|1024.00|Intel Xeon Platinum 8252|32|16|2|✗|✗|
|x2iezn.12 xlarge|✗|1536.00|Intel Xeon Platinum 8252|48|24|2|✗|✗|


Performance specifications 202


-----

**Instance**


**BurstableMemory**


**Processor** **vCPUs CPU**


**Threads Accelerat**


**Accelerat**

|type|Col2|(GiB)|Col4|Col5|cores|per core|ors|or memor|
|---|---|---|---|---|---|---|---|---|
|x2iezn.metal|✗|1536.00|Intel Xeon Platinum 8252|48|24|2|✗|✗|
|X1e|||||||||
|x1e.xlarge|✗|122.00|Intel Haswell E7 8880v3|4|2|2|✗|✗|
|x1e.2xlarge|✗|244.00|Intel Haswell E7 8880v3|8|4|2|✗|✗|
|x1e.4xlarge|✗|488.00|Intel Haswell E7 8880v3|16|8|2|✗|✗|
|x1e.8xlarge|✗|976.00|Intel Haswell E7 8880v3|32|16|2|✗|✗|
|x1e.16xlarge|✗|1952.00|Intel Haswell E7 8880v3|64|32|2|✗|✗|
|x1e.32xlarge|✗|3904.00|Intel Haswell E7 8880v3|128|64|2|✗|✗|
|z1d|||||||||
|z1d.large|✗|16.00|Intel Xeon Platinum 8151|2|1|2|✗|✗|
|z1d.xlarge|✗|32.00|Intel Xeon Platinum 8151|4|2|2|✗|✗|


Performance specifications 203


-----

**Instance**


**BurstableMemory**


**Processor** **vCPUs CPU**


**Threads Accelerat**


**Accelerat**

|type|Col2|(GiB)|Col4|Col5|cores|per core|ors|or memor|
|---|---|---|---|---|---|---|---|---|
|z1d.2xlarge|✗|64.00|Intel Xeon Platinum 8151|8|4|2|✗|✗|
|z1d.3xlarge|✗|96.00|Intel Xeon Platinum 8151|12|6|2|✗|✗|
|z1d.6xlarge|✗|192.00|Intel Xeon Platinum 8151|24|12|2|✗|✗|
|z1d.12xla rge|✗|384.00|Intel Xeon Platinum 8151|48|24|2|✗|✗|
|z1d.metal|✗|384.00|Intel Xeon Platinum 8151|48|24|2|✗|✗|


#### Network specifications

|Instance type|Baseline / Burst bandwidth (Gbps)|EFA|ENA|ENA Express|Network cards|Max. network interface s|IP addresses per interface|IPv6|
|---|---|---|---|---|---|---|---|---|
|R5|||||||||
|1 r5.large|0.75 / 10.0|✗|✓|✗|1|3|10|✓|
|1 r5.xlarge|1.25 / 10.0|✗|✓|✗|1|4|15|✓|



Network specifications 204


-----

|Col1|bandwidth (Gbps)|Col3|Col4|Col5|Col6|interface s|per interface|Col9|
|---|---|---|---|---|---|---|---|---|
|1 r5.2xlarge|2.5 / 10.0|✗|✓|✗|1|4|15|✓|
|1 r5.4xlarge|5.0 / 10.0|✗|✓|✗|1|8|30|✓|
|r5.8xlarge|10 Gigabit|✗|✓|✗|1|8|30|✓|
|r5.12xlarge|12 Gigabit|✗|✓|✗|1|8|30|✓|
|r5.16xlarge|20 Gigabit|✗|✓|✗|1|15|50|✓|
|r5.24xlarge|25 Gigabit|✗|✓|✗|1|15|50|✓|
|r5.metal|25 Gigabit|✗|✓|✗|1|15|50|✓|
|R5a|||||||||
|1 r5a.large|0.75 / 10.0|✗|✓|✗|1|3|10|✓|
|1 r5a.xlarge|1.25 / 10.0|✗|✓|✗|1|4|15|✓|
|1 r5a.2xlarge|2.5 / 10.0|✗|✓|✗|1|4|15|✓|
|1 r5a.4xlarge|5.0 / 10.0|✗|✓|✗|1|8|30|✓|
|1 r5a.8xlarge|7.5 / 10.0|✗|✓|✗|1|8|30|✓|
|r5a.12xlarge|10 Gigabit|✗|✓|✗|1|8|30|✓|
|r5a.16xlarge|12 Gigabit|✗|✓|✗|1|15|50|✓|
|r5a.24xlarge|20 Gigabit|✗|✓|✗|1|15|50|✓|
|R5ad|||||||||
|1 r5ad.large|0.75 / 10.0|✗|✓|✗|1|3|10|✓|
|1 r5ad.xlarge|1.25 / 10.0|✗|✓|✗|1|4|15|✓|


**Instance type** **Baseline /** **EFA** **ENA** **ENA** **Network** **Max.** **IP** **IPv6**
**Burst** **Express** **cards** **network** **addresses**
**bandwidth** **interface** **per**
**(Gbps)** **s** **interface**


Network specifications 205


-----

|Col1|bandwidth (Gbps)|Col3|Col4|Col5|Col6|interface s|per interface|Col9|
|---|---|---|---|---|---|---|---|---|
|1 r5ad.2xlarge|2.5 / 10.0|✗|✓|✗|1|4|15|✓|
|1 r5ad.4xlarge|5.0 / 10.0|✗|✓|✗|1|8|30|✓|
|1 r5ad.8xlarge|7.5 / 10.0|✗|✓|✗|1|8|30|✓|
|r5ad.12xlarge|10 Gigabit|✗|✓|✗|1|8|30|✓|
|r5ad.16xlarge|12 Gigabit|✗|✓|✗|1|15|50|✓|
|r5ad.24xlarge|20 Gigabit|✗|✓|✗|1|15|50|✓|
|R5b|||||||||
|1 r5b.large|0.75 / 10.0|✗|✓|✗|1|3|10|✓|
|1 r5b.xlarge|1.25 / 10.0|✗|✓|✗|1|4|15|✓|
|1 r5b.2xlarge|2.5 / 10.0|✗|✓|✗|1|4|15|✓|
|1 r5b.4xlarge|5.0 / 10.0|✗|✓|✗|1|8|30|✓|
|r5b.8xlarge|10 Gigabit|✗|✓|✗|1|8|30|✓|
|r5b.12xlarge|12 Gigabit|✗|✓|✗|1|8|30|✓|
|r5b.16xlarge|20 Gigabit|✗|✓|✗|1|15|50|✓|
|r5b.24xlarge|25 Gigabit|✗|✓|✗|1|15|50|✓|
|r5b.metal|25 Gigabit|✗|✓|✗|1|15|50|✓|
|R5d|||||||||
|1 r5d.large|0.75 / 10.0|✗|✓|✗|1|3|10|✓|
|1 r5d.xlarge|1.25 / 10.0|✗|✓|✗|1|4|15|✓|


**Instance type** **Baseline /** **EFA** **ENA** **ENA** **Network** **Max.** **IP** **IPv6**
**Burst** **Express** **cards** **network** **addresses**
**bandwidth** **interface** **per**
**(Gbps)** **s** **interface**


Network specifications 206


-----

|Col1|bandwidth (Gbps)|Col3|Col4|Col5|Col6|interface s|per interface|Col9|
|---|---|---|---|---|---|---|---|---|
|1 r5d.2xlarge|2.5 / 10.0|✗|✓|✗|1|4|15|✓|
|1 r5d.4xlarge|5.0 / 10.0|✗|✓|✗|1|8|30|✓|
|r5d.8xlarge|10 Gigabit|✗|✓|✗|1|8|30|✓|
|r5d.12xlarge|12 Gigabit|✗|✓|✗|1|8|30|✓|
|r5d.16xlarge|20 Gigabit|✗|✓|✗|1|15|50|✓|
|r5d.24xlarge|25 Gigabit|✗|✓|✗|1|15|50|✓|
|r5d.metal|25 Gigabit|✗|✓|✗|1|15|50|✓|
|R5dn|||||||||
|1 r5dn.large|2.1 / 25.0|✗|✓|✗|1|3|10|✓|
|1 r5dn.xlarge|4.1 / 25.0|✗|✓|✗|1|4|15|✓|
|1 r5dn.2xlarge|8.125 / 25.0|✗|✓|✗|1|4|15|✓|
|1 r5dn.4xlarge|16.25 / 25.0|✗|✓|✗|1|8|30|✓|
|r5dn.8xlarge|25 Gigabit|✗|✓|✗|1|8|30|✓|
|r5dn.12xlarge|50 Gigabit|✗|✓|✗|1|8|30|✓|
|r5dn.16xlarge|75 Gigabit|✗|✓|✗|1|15|50|✓|
|r5dn.24xlarge|100 Gigabit|✓|✓|✗|1|15|50|✓|
|r5dn.metal|100 Gigabit|✓|✓|✗|1|15|50|✓|
|R5n|||||||||
|1 r5n.large|2.1 / 25.0|✗|✓|✗|1|3|10|✓|


**Instance type** **Baseline /** **EFA** **ENA** **ENA** **Network** **Max.** **IP** **IPv6**
**Burst** **Express** **cards** **network** **addresses**
**bandwidth** **interface** **per**
**(Gbps)** **s** **interface**


Network specifications 207


-----

|Col1|bandwidth (Gbps)|Col3|Col4|Col5|Col6|interface s|per interface|Col9|
|---|---|---|---|---|---|---|---|---|
|1 r5n.xlarge|4.1 / 25.0|✗|✓|✗|1|4|15|✓|
|1 r5n.2xlarge|8.125 / 25.0|✗|✓|✗|1|4|15|✓|
|1 r5n.4xlarge|16.25 / 25.0|✗|✓|✗|1|8|30|✓|
|r5n.8xlarge|25 Gigabit|✗|✓|✗|1|8|30|✓|
|r5n.12xlarge|50 Gigabit|✗|✓|✗|1|8|30|✓|
|r5n.16xlarge|75 Gigabit|✗|✓|✗|1|15|50|✓|
|r5n.24xlarge|100 Gigabit|✓|✓|✗|1|15|50|✓|
|r5n.metal|100 Gigabit|✓|✓|✗|1|15|50|✓|
|R6a|||||||||
|1 r6a.large|0.781 / 12.5|✗|✓|✗|1|3|10|✓|
|1 r6a.xlarge|1.562 / 12.5|✗|✓|✗|1|4|15|✓|
|1 r6a.2xlarge|3.125 / 12.5|✗|✓|✗|1|4|15|✓|
|1 r6a.4xlarge|6.25 / 12.5|✗|✓|✗|1|8|30|✓|
|r6a.8xlarge|12.5 Gigabit|✗|✓|✗|1|8|30|✓|
|r6a.12xlarge|18.75 Gigabit|✗|✓|✓|1|8|30|✓|
|r6a.16xlarge|25 Gigabit|✗|✓|✓|1|15|50|✓|
|r6a.24xlarge|37.5 Gigabit|✗|✓|✓|1|15|50|✓|
|r6a.32xlarge|50 Gigabit|✗|✓|✓|1|15|50|✓|
|r6a.48xlarge|50 Gigabit|✓|✓|✓|1|15|50|✓|


**Instance type** **Baseline /** **EFA** **ENA** **ENA** **Network** **Max.** **IP** **IPv6**
**Burst** **Express** **cards** **network** **addresses**
**bandwidth** **interface** **per**
**(Gbps)** **s** **interface**


Network specifications 208


-----

|Col1|bandwidth (Gbps)|Col3|Col4|Col5|Col6|interface s|per interface|Col9|
|---|---|---|---|---|---|---|---|---|
|r6a.metal|50 Gigabit|✓|✓|✓|1|15|50|✓|
|R6g|||||||||
|1 r6g.medium|0.5 / 10.0|✗|✓|✗|1|2|4|✓|
|1 r6g.large|0.75 / 10.0|✗|✓|✗|1|3|10|✓|
|1 r6g.xlarge|1.25 / 10.0|✗|✓|✗|1|4|15|✓|
|1 r6g.2xlarge|2.5 / 10.0|✗|✓|✗|1|4|15|✓|
|1 r6g.4xlarge|5.0 / 10.0|✗|✓|✗|1|8|30|✓|
|r6g.8xlarge|12 Gigabit|✗|✓|✗|1|8|30|✓|
|r6g.12xlarge|20 Gigabit|✗|✓|✗|1|8|30|✓|
|r6g.16xlarge|25 Gigabit|✗|✓|✗|1|15|50|✓|
|r6g.metal|25 Gigabit|✗|✓|✗|1|15|50|✓|
|R6gd|||||||||
|r6gd.medium 1|0.5 / 10.0|✗|✓|✗|1|2|4|✓|
|1 r6gd.large|0.75 / 10.0|✗|✓|✗|1|3|10|✓|
|1 r6gd.xlarge|1.25 / 10.0|✗|✓|✗|1|4|15|✓|
|1 r6gd.2xlarge|2.5 / 10.0|✗|✓|✗|1|4|15|✓|
|1 r6gd.4xlarge|5.0 / 10.0|✗|✓|✗|1|8|30|✓|
|r6gd.8xlarge|12 Gigabit|✗|✓|✗|1|8|30|✓|


**Instance type** **Baseline /** **EFA** **ENA** **ENA** **Network** **Max.** **IP** **IPv6**
**Burst** **Express** **cards** **network** **addresses**
**bandwidth** **interface** **per**
**(Gbps)** **s** **interface**


Network specifications 209


-----

|Col1|bandwidth (Gbps)|Col3|Col4|Col5|Col6|interface s|per interface|Col9|
|---|---|---|---|---|---|---|---|---|
|r6gd.12xlarge|20 Gigabit|✗|✓|✗|1|8|30|✓|
|r6gd.16xlarge|25 Gigabit|✗|✓|✗|1|15|50|✓|
|r6gd.metal|25 Gigabit|✗|✓|✗|1|15|50|✓|
|R6i|||||||||
|1 r6i.large|0.781 / 12.5|✗|✓|✗|1|3|10|✓|
|1 r6i.xlarge|1.562 / 12.5|✗|✓|✗|1|4|15|✓|
|1 r6i.2xlarge|3.125 / 12.5|✗|✓|✗|1|4|15|✓|
|1 r6i.4xlarge|6.25 / 12.5|✗|✓|✗|1|8|30|✓|
|r6i.8xlarge|12.5 Gigabit|✗|✓|✓|1|8|30|✓|
|r6i.12xlarge|18.75 Gigabit|✗|✓|✓|1|8|30|✓|
|r6i.16xlarge|25 Gigabit|✗|✓|✓|1|15|50|✓|
|r6i.24xlarge|37.5 Gigabit|✗|✓|✓|1|15|50|✓|
|r6i.32xlarge|50 Gigabit|✓|✓|✓|1|15|50|✓|
|r6i.metal|50 Gigabit|✓|✓|✓|1|15|50|✓|
|R6idn|||||||||
|1 r6idn.large|3.125 / 25.0|✗|✓|✗|1|3|10|✓|
|1 r6idn.xlarge|6.25 / 30.0|✗|✓|✗|1|4|15|✓|
|r6idn.2xlarge 1|12.5 / 40.0|✗|✓|✗|1|4|15|✓|


**Instance type** **Baseline /** **EFA** **ENA** **ENA** **Network** **Max.** **IP** **IPv6**
**Burst** **Express** **cards** **network** **addresses**
**bandwidth** **interface** **per**
**(Gbps)** **s** **interface**


Network specifications 210


-----

|Col1|bandwidth (Gbps)|Col3|Col4|Col5|Col6|interface s|per interface|Col9|
|---|---|---|---|---|---|---|---|---|
|r6idn.4xlarge 1|25.0 / 50.0|✗|✓|✗|1|8|30|✓|
|r6idn.8xlarge|50 Gigabit|✗|✓|✗|1|8|30|✓|
|r6idn.12xlarge|75 Gigabit|✗|✓|✗|1|8|30|✓|
|r6idn.16xlarge|100 Gigabit|✗|✓|✗|1|15|50|✓|
|r6idn.24xlarge|150 Gigabit|✗|✓|✗|1|15|50|✓|
|r6idn.32xlarge|200 Gigabit|✓|✓|✗|2|16|50|✓|
|r6idn.metal|200 Gigabit|✓|✓|✗|2|16|50|✓|
|R6in|||||||||
|1 r6in.large|3.125 / 25.0|✗|✓|✗|1|3|10|✓|
|1 r6in.xlarge|6.25 / 30.0|✗|✓|✗|1|4|15|✓|
|1 r6in.2xlarge|12.5 / 40.0|✗|✓|✗|1|4|15|✓|
|1 r6in.4xlarge|25.0 / 50.0|✗|✓|✗|1|8|30|✓|
|r6in.8xlarge|50 Gigabit|✗|✓|✗|1|8|30|✓|
|r6in.12xlarge|75 Gigabit|✗|✓|✗|1|8|30|✓|
|r6in.16xlarge|100 Gigabit|✗|✓|✗|1|15|50|✓|
|r6in.24xlarge|150 Gigabit|✗|✓|✗|1|15|50|✓|
|r6in.32xlarge|200 Gigabit|✓|✓|✗|2|16|50|✓|
|r6in.metal|200 Gigabit|✓|✓|✗|2|16|50|✓|


**Instance type** **Baseline /** **EFA** **ENA** **ENA** **Network** **Max.** **IP** **IPv6**
**Burst** **Express** **cards** **network** **addresses**
**bandwidth** **interface** **per**
**(Gbps)** **s** **interface**


Network specifications 211


-----

|Instance type Baseline / Burst bandwidth (Gbps) EFA ENA ENA Express Network cards Max. network interface s IP addresses per interface IPv6|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
|R6id|||||||||
|1 r6id.large|0.781 / 12.5|✗|✓|✗|1|3|10|✓|
|1 r6id.xlarge|1.562 / 12.5|✗|✓|✗|1|4|15|✓|
|1 r6id.2xlarge|3.125 / 12.5|✗|✓|✗|1|4|15|✓|
|1 r6id.4xlarge|6.25 / 12.5|✗|✓|✗|1|8|30|✓|
|r6id.8xlarge|12.5 Gigabit|✗|✓|✓|1|8|30|✓|
|r6id.12xlarge|18.75 Gigabit|✗|✓|✓|1|8|30|✓|
|r6id.16xlarge|25 Gigabit|✗|✓|✓|1|15|50|✓|
|r6id.24xlarge|37.5 Gigabit|✗|✓|✓|1|15|50|✓|
|r6id.32xlarge|50 Gigabit|✓|✓|✓|1|15|50|✓|
|r6id.metal|50 Gigabit|✓|✓|✓|1|15|50|✓|
|R7a|||||||||
|1 r7a.medium|0.39 / 12.5|✗|✓|✗|1|2|4|✓|
|1 r7a.large|0.781 / 12.5|✗|✓|✗|1|3|10|✓|
|1 r7a.xlarge|1.562 / 12.5|✗|✓|✗|1|4|15|✓|
|1 r7a.2xlarge|3.125 / 12.5|✗|✓|✗|1|4|15|✓|
|1 r7a.4xlarge|6.25 / 12.5|✗|✓|✗|1|8|30|✓|
|r7a.8xlarge|12.5 Gigabit|✗|✓|✗|1|8|30|✓|
|r7a.12xlarge|18.75 Gigabit|✗|✓|✗|1|8|30|✓|


Network specifications 212


-----

|Col1|bandwidth (Gbps)|Col3|Col4|Col5|Col6|interface s|per interface|Col9|
|---|---|---|---|---|---|---|---|---|
|r7a.16xlarge|25 Gigabit|✗|✓|✗|1|15|50|✓|
|r7a.24xlarge|37.5 Gigabit|✗|✓|✗|1|15|50|✓|
|r7a.32xlarge|50 Gigabit|✗|✓|✗|1|15|50|✓|
|r7a.48xlarge|50 Gigabit|✓|✓|✗|1|15|50|✓|
|r7a.metal -48xl|50 Gigabit|✓|✓|✗|1|15|50|✓|
|R7g|||||||||
|1 r7g.medium|0.52 / 12.5|✗|✓|✗|1|2|4|✓|
|1 r7g.large|0.937 / 12.5|✗|✓|✗|1|3|10|✓|
|1 r7g.xlarge|1.876 / 12.5|✗|✓|✗|1|4|15|✓|
|1 r7g.2xlarge|3.75 / 15.0|✗|✓|✗|1|4|15|✓|
|1 r7g.4xlarge|7.5 / 15.0|✗|✓|✗|1|8|30|✓|
|r7g.8xlarge|15 Gigabit|✗|✓|✗|1|8|30|✓|
|r7g.12xlarge|22.5 Gigabit|✗|✓|✓|1|8|30|✓|
|r7g.16xlarge|30 Gigabit|✓|✓|✓|1|15|50|✓|
|r7g.metal|30 Gigabit|✓|✓|✓|1|15|50|✓|
|R7gd|||||||||
|r7gd.medium 1|0.52 / 12.5|✗|✓|✗|1|2|4|✓|


**Instance type** **Baseline /** **EFA** **ENA** **ENA** **Network** **Max.** **IP** **IPv6**
**Burst** **Express** **cards** **network** **addresses**
**bandwidth** **interface** **per**
**(Gbps)** **s** **interface**


Network specifications 213


-----

|Col1|bandwidth (Gbps)|Col3|Col4|Col5|Col6|interface s|per interface|Col9|
|---|---|---|---|---|---|---|---|---|
|1 r7gd.large|0.937 / 12.5|✗|✓|✗|1|3|10|✓|
|1 r7gd.xlarge|1.876 / 12.5|✗|✓|✗|1|4|15|✓|
|1 r7gd.2xlarge|3.75 / 15.0|✗|✓|✗|1|4|15|✓|
|1 r7gd.4xlarge|7.5 / 15.0|✗|✓|✗|1|8|30|✓|
|r7gd.8xlarge|15 Gigabit|✗|✓|✗|1|8|30|✓|
|r7gd.12xlarge|22.5 Gigabit|✗|✓|✓|1|8|30|✓|
|r7gd.16xlarge|30 Gigabit|✓|✓|✓|1|15|50|✓|
|r7gd.metal|30 Gigabit|✓|✓|✓|1|15|50|✓|
|R7i|||||||||
|1 r7i.large|0.781 / 12.5|✗|✓|✗|1|3|10|✓|
|1 r7i.xlarge|1.562 / 12.5|✗|✓|✗|1|4|15|✓|
|1 r7i.2xlarge|3.125 / 12.5|✗|✓|✗|1|4|15|✓|
|1 r7i.4xlarge|6.25 / 12.5|✗|✓|✗|1|8|30|✓|
|r7i.8xlarge|12.5 Gigabit|✗|✓|✗|1|8|30|✓|
|r7i.12xlarge|18.75 Gigabit|✗|✓|✓|1|8|30|✓|
|r7i.16xlarge|25 Gigabit|✗|✓|✓|1|15|50|✓|
|r7i.24xlarge|37.5 Gigabit|✗|✓|✓|1|15|50|✓|
|r7i.48xlarge|50 Gigabit|✓|✓|✓|1|15|50|✓|
|r7i.metal-24xl|37.5 Gigabit|✗|✓|✓|1|15|50|✓|


**Instance type** **Baseline /** **EFA** **ENA** **ENA** **Network** **Max.** **IP** **IPv6**
**Burst** **Express** **cards** **network** **addresses**
**bandwidth** **interface** **per**
**(Gbps)** **s** **interface**


Network specifications 214


-----

|Col1|bandwidth (Gbps)|Col3|Col4|Col5|Col6|interface s|per interface|Col9|
|---|---|---|---|---|---|---|---|---|
|r7i.metal-48xl|50 Gigabit|✓|✓|✓|1|15|50|✓|
|R7iz|||||||||
|1 r7iz.large|0.781 / 12.5|✗|✓|✗|1|3|10|✓|
|1 r7iz.xlarge|1.562 / 12.5|✗|✓|✗|1|4|15|✓|
|1 r7iz.2xlarge|3.125 / 12.5|✗|✓|✗|1|4|15|✓|
|1 r7iz.4xlarge|6.25 / 12.5|✗|✓|✗|1|8|30|✓|
|r7iz.8xlarge|12.5 Gigabit|✗|✓|✗|1|8|30|✓|
|r7iz.12xlarge|25 Gigabit|✗|✓|✗|1|8|30|✓|
|r7iz.16xlarge|25 Gigabit|✗|✓|✗|1|15|50|✓|
|r7iz.32xlarge|50 Gigabit|✓|✓|✗|1|15|50|✓|
|r7iz.meta l-16xl|25 Gigabit|✗|✓|✗|1|15|50|✓|
|r7iz.meta l-32xl|50 Gigabit|✓|✓|✗|1|15|50|✓|
|R8g|||||||||
|1 r8g.medium|0.52 / 12.5|✗|✓|✗|1|2|4|✓|
|1 r8g.large|0.937 / 12.5|✗|✓|✗|1|3|10|✓|
|1 r8g.xlarge|1.876 / 12.5|✗|✓|✗|1|4|15|✓|
|1 r8g.2xlarge|3.75 / 15.0|✗|✓|✗|1|4|15|✓|


**Instance type** **Baseline /** **EFA** **ENA** **ENA** **Network** **Max.** **IP** **IPv6**
**Burst** **Express** **cards** **network** **addresses**
**bandwidth** **interface** **per**
**(Gbps)** **s** **interface**


Network specifications 215


-----

|Col1|bandwidth (Gbps)|Col3|Col4|Col5|Col6|interface s|per interface|Col9|
|---|---|---|---|---|---|---|---|---|
|1 r8g.4xlarge|7.5 / 15.0|✗|✓|✗|1|8|30|✓|
|r8g.8xlarge|15 Gigabit|✗|✓|✗|1|8|30|✓|
|r8g.12xlarge|22.5 Gigabit|✗|✓|✓|1|8|30|✓|
|r8g.16xlarge|30 Gigabit|✗|✓|✓|1|15|50|✓|
|r8g.24xlarge|40 Gigabit|✓|✓|✓|1|15|50|✓|
|r8g.48xlarge|50 Gigabit|✓|✓|✓|1|15|50|✓|
|r8g.metal -24xl|40 Gigabit|✓|✓|✓|1|15|50|✓|
|r8g.metal -48xl|50 Gigabit|✓|✓|✓|1|15|50|✓|
|U-3tb1|||||||||
|u-3tb1.56 xlarge|50 Gigabit|✗|✓|✗|1|8|30|✓|
|U-6tb1|||||||||
|u-6tb1.56 xlarge|100 Gigabit|✗|✓|✗|1|15|50|✓|
|u-6tb1.11 2xlarge|100 Gigabit|✗|✓|✗|1|15|50|✓|
|u-6tb1.metal|100|✗|✓|✗|1|5|30|✓|
|U-9tb1|||||||||


**Instance type** **Baseline /** **EFA** **ENA** **ENA** **Network** **Max.** **IP** **IPv6**
**Burst** **Express** **cards** **network** **addresses**
**bandwidth** **interface** **per**
**(Gbps)** **s** **interface**


Network specifications 216


-----

|Col1|bandwidth (Gbps)|Col3|Col4|Col5|Col6|interface s|per interface|Col9|
|---|---|---|---|---|---|---|---|---|
|u-9tb1.11 2xlarge|100 Gigabit|✗|✓|✗|1|15|50|✓|
|u-9tb1.metal|100|✗|✓|✗|1|5|30|✓|
|U-12tb1|||||||||
|u-12tb1.1 12xlarge|100 Gigabit|✗|✓|✗|1|15|50|✓|
|u-12tb1.metal|100|✗|✓|✗|1|5|30|✓|
|U-18tb1|||||||||
|u-18tb1.1 12xlarge|100 Gigabit|✗|✓|✗|1|15|50|✓|
|u-18tb1.metal|100 Gigabit|✗|✓|✗|1|15|50|✓|
|U-24tb1|||||||||
|u-24tb1.1 12xlarge|100 Gigabit|✗|✓|✗|1|15|50|✓|
|u-24tb1.metal|100 Gigabit|✗|✓|✗|1|15|50|✓|
|U7i-12tb|||||||||
|u7i-12tb. 224xlarge|100 Gigabit|✓|✓|✓|1|15|50|✓|
|U7in-16tb|||||||||
|u7in-16tb .224xlarge|200 Gigabit|✓|✓|✓|2|16|50|✓|


**Instance type** **Baseline /** **EFA** **ENA** **ENA** **Network** **Max.** **IP** **IPv6**
**Burst** **Express** **cards** **network** **addresses**
**bandwidth** **interface** **per**
**(Gbps)** **s** **interface**


Network specifications 217


-----

|Instance type Baseline / Burst bandwidth (Gbps) EFA ENA ENA Express Network cards Max. network interface s IP addresses per interface IPv6|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
|U7in-24tb|||||||||
|u7in-24tb .224xlarge|200 Gigabit|✓|✓|✓|2|16|50|✓|
|U7in-32tb|||||||||
|u7in-32tb .224xlarge|200 Gigabit|✓|✓|✓|2|16|50|✓|
|X1|||||||||
|x1.16xlarge|10 Gigabit|✗|✓|✗|1|8|30|✓|
|x1.32xlarge|25 Gigabit|✗|✓|✗|1|8|30|✓|
|X2gd|||||||||
|x2gd.medium 1|0.5 / 10.0|✗|✓|✗|1|2|4|✓|
|1 x2gd.large|0.75 / 10.0|✗|✓|✗|1|3|10|✓|
|1 x2gd.xlarge|1.25 / 10.0|✗|✓|✗|1|4|15|✓|
|1 x2gd.2xlarge|2.5 / 10.0|✗|✓|✗|1|4|15|✓|
|1 x2gd.4xlarge|5.0 / 10.0|✗|✓|✗|1|8|30|✓|
|x2gd.8xlarge|12 Gigabit|✗|✓|✗|1|8|30|✓|
|x2gd.12xlarge|20 Gigabit|✗|✓|✗|1|8|30|✓|
|x2gd.16xlarge|25 Gigabit|✗|✓|✗|1|15|50|✓|
|x2gd.metal|25 Gigabit|✗|✓|✗|1|15|50|✓|


Network specifications 218


-----

|Instance type Baseline / Burst bandwidth (Gbps) EFA ENA ENA Express Network cards Max. network interface s IP addresses per interface IPv6|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
|X2idn|||||||||
|x2idn.16x large|50 Gigabit|✗|✓|✓|1|15|50|✓|
|x2idn.24x large|75 Gigabit|✗|✓|✓|1|15|50|✓|
|x2idn.32x large|100 Gigabit|✓|✓|✓|1|15|50|✓|
|x2idn.metal|100 Gigabit|✓|✓|✓|1|15|50|✓|
|X2iedn|||||||||
|x2iedn.xlarge 1|1.875 / 25.0|✗|✓|✗|1|4|15|✓|
|x2iedn.2x 1 large|5.0 / 25.0|✗|✓|✗|1|4|15|✓|
|x2iedn.4x 1 large|12.5 / 25.0|✗|✓|✗|1|8|30|✓|
|x2iedn.8x large|25 Gigabit|✗|✓|✓|1|8|30|✓|
|x2iedn.16 xlarge|50 Gigabit|✗|✓|✓|1|15|50|✓|
|x2iedn.24 xlarge|75 Gigabit|✗|✓|✓|1|15|50|✓|
|x2iedn.32 xlarge|100 Gigabit|✓|✓|✓|1|15|50|✓|


Network specifications 219


-----

|Col1|bandwidth (Gbps)|Col3|Col4|Col5|Col6|interface s|per interface|Col9|
|---|---|---|---|---|---|---|---|---|
|x2iedn.metal|100 Gigabit|✓|✓|✓|1|15|50|✓|
|X2iezn|||||||||
|x2iezn.2xlarge 1|12.5 / 25.0|✗|✓|✗|1|4|15|✓|
|x2iezn.4xlarge 1|15.0 / 25.0|✗|✓|✗|1|8|30|✓|
|x2iezn.6xlarge|50 Gigabit|✗|✓|✗|1|8|30|✓|
|x2iezn.8xlarge|75 Gigabit|✗|✓|✗|1|8|30|✓|
|x2iezn.12 xlarge|100 Gigabit|✓|✓|✗|1|15|50|✓|
|x2iezn.metal|100 Gigabit|✓|✓|✗|1|15|50|✓|
|X1e|||||||||
|1 x1e.xlarge|0.625 / 10.0|✗|✓|✗|1|3|10|✓|
|1 x1e.2xlarge|1.25 / 10.0|✗|✓|✗|1|4|15|✓|
|1 x1e.4xlarge|2.5 / 10.0|✗|✓|✗|1|4|15|✓|
|1 x1e.8xlarge|5.0 / 10.0|✗|✓|✗|1|4|15|✓|
|x1e.16xlarge|10 Gigabit|✗|✓|✗|1|8|30|✓|
|x1e.32xlarge|25 Gigabit|✗|✓|✗|1|8|30|✓|
|z1d|||||||||
|1 z1d.large|0.75 / 10.0|✗|✓|✗|1|3|10|✓|


**Instance type** **Baseline /** **EFA** **ENA** **ENA** **Network** **Max.** **IP** **IPv6**
**Burst** **Express** **cards** **network** **addresses**
**bandwidth** **interface** **per**
**(Gbps)** **s** **interface**


Network specifications 220


-----

|Col1|bandwidth (Gbps)|Col3|Col4|Col5|Col6|interface s|per interface|Col9|
|---|---|---|---|---|---|---|---|---|
|1 z1d.xlarge|1.25 / 10.0|✗|✓|✗|1|4|15|✓|
|1 z1d.2xlarge|2.5 / 10.0|✗|✓|✗|1|4|15|✓|
|1 z1d.3xlarge|5.0 / 10.0|✗|✓|✗|1|8|30|✓|
|z1d.6xlarge|12 Gigabit|✗|✓|✗|1|8|30|✓|
|z1d.12xlarge|25 Gigabit|✗|✓|✗|1|15|50|✓|
|z1d.metal|25 Gigabit|✗|✓|✗|1|15|50|✓|


**Instance type** **Baseline /** **EFA** **ENA** **ENA** **Network** **Max.** **IP** **IPv6**
**Burst** **Express** **cards** **network** **addresses**
**bandwidth** **interface** **per**
**(Gbps)** **s** **interface**


**Note**

1
These instances have a baseline bandwidth and can use a network I/O credit mechanism
to burst beyond their baseline bandwidth on a best effort basis. Other instances types
[can sustain their maximum performance indefinitely. For more information, see instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-network-bandwidth.html)
[network bandwidth.](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-network-bandwidth.html)

For 32xlarge and metal instance types that support 200 Gbps, at least 2 ENIs, each
attached to a different network card, are required on the instance to achieve 200 Gbps
throughput. Each ENI attached to a network card can achieve a max of 170 Gbps.
```
   u-6tb1.metal, u-9tb1.metal, and u-12tb1.metal instances launched after March 12,

```
2020 provide network performance of 100 Gbps. u-6tb1.metal, u-9tb1.metal, and
```
   u-12tb1.metal instances launched before March 12, 2020 mightonly provide network

```
performance of 25 Gbps. To ensure that instances launched before March 12, 2020 have a
network performance of 100 Gbps, contact your account team to upgrade your instance at
no additional cost.

Network specifications 221


-----

#### Amazon EBS specifications

The following table indicates which instance types are Amazon EBS optimized by default and
which optionally support it. It also describes their EBS-optimized performance, including dedicated
bandwidth to Amazon EBS, the typical maximum aggregate throughput that can be achieved on
that dedicated connection with a streaming read workload and 128 KiB I/O size, and the maximum
IOPS the instance type can support when using a 16 KiB I/O size. Instance types not listed do not
support Amazon EBS optimization.

**Important**

An instance's EBS performance is bounded by the instance's performance limits, or
the aggregated performance of its attached volumes, whichever is smaller. To achieve
maximum EBS performance, an instance must have attached volumes that provide a

combined performance equal to or greater than the maximum instance performance. For

example, to achieve 80,000 IOPS for r6i.16xlarge, the instance must have at least 5
```
   gp3 volumes provisioned with 16,000 IOPS each (5 volumes x 16,000 IOPS = 80,000

```
IOPS).
We recommand that you choose an EBS–optimized instance type that provides more
dedicated Amazon EBS throughput than your application needs; otherwise, the connection
between Amazon EBS and Amazon EC2 can become a performance bottleneck.

|Instance type|Baseline / Maximum bandwidth (Mbps)|Baseline / Maximum throughput (MB/s, 128 KiB I/O)|Baseline / Maximum IOPS (16 KiB I/O)|NVMe|EBS optimization 2|
|---|---|---|---|---|---|
|R5||||||
|1 r5.large|650.00 / 4750.00|81.25 / 593.75|3600.00 / 18750.00|✓|default|
|1 r5.xlarge|1150.00 / 4750.00|143.75 / 593.75|6000.00 / 18750.00|✓|default|



Amazon EBS specifications 222


-----

**Instance**


**Baseline /**


**Baseline /**


**Baseline /**


**NVMe** **EBS**

|type|Maximum bandwidth (Mbps)|Maximum throughput (MB/s, 128 KiB I/O)|Maximum IOPS (16 KiB I/O)|Col5|optimization 2|
|---|---|---|---|---|---|
|1 r5.2xlarge|2300.00 / 4750.00|287.50 / 593.75|12000.00 / 18750.00|✓|default|
|r5.4xlarge|4750.00|593.75|18750.00|✓|default|
|r5.8xlarge|6800.00|850.00|30000.00|✓|default|
|r5.12xlarge|9500.00|1187.50|40000.00|✓|default|
|r5.16xlarge|13600.00|1700.00|60000.00|✓|default|
|r5.24xlarge|19000.00|2375.00|80000.00|✓|default|
|r5.metal|19000.00|2375.00|80000.00|✓|default|
|R5a||||||
|1 r5a.large|650.00 / 2880.00|81.25 / 360.00|3600.00 / 16000.00|✓|default|
|1 r5a.xlarge|1085.00 / 2880.00|135.62 / 360.00|6000.00 / 16000.00|✓|default|
|1 r5a.2xlarge|1580.00 / 2880.00|197.50 / 360.00|8333.00 / 16000.00|✓|default|
|r5a.4xlarge|2880.00|360.00|16000.00|✓|default|
|r5a.8xlarge|4750.00|593.75|20000.00|✓|default|
|r5a.12xlarge|6780.00|847.50|30000.00|✓|default|
|r5a.16xlarge|9500.00|1187.50|40000.00|✓|default|
|r5a.24xlarge|13570.00|1696.25|60000.00|✓|default|


Amazon EBS specifications 223


-----

**Instance**


**Baseline /**


**Baseline /**


**Baseline /**


**NVMe** **EBS**

|type Maximum bandwidth (Mbps) Maximum throughput (MB/s, 128 KiB I/O) Maximum IOPS (16 KiB I/O) optimization 2|Col2|Col3|Col4|Col5|Col6|
|---|---|---|---|---|---|
|R5ad||||||
|1 r5ad.large|650.00 / 2880.00|81.25 / 360.00|3600.00 / 16000.00|✓|default|
|1 r5ad.xlarge|1085.00 / 2880.00|135.62 / 360.00|6000.00 / 16000.00|✓|default|
|r5ad.2xlarge 1|1580.00 / 2880.00|197.50 / 360.00|8333.00 / 16000.00|✓|default|
|r5ad.4xlarge|2880.00|360.00|16000.00|✓|default|
|r5ad.8xlarge|4750.00|593.75|20000.00|✓|default|
|r5ad.12xl arge|6780.00|847.50|30000.00|✓|default|
|r5ad.16xl arge|9500.00|1187.50|40000.00|✓|default|
|r5ad.24xl arge|13570.00|1696.25|60000.00|✓|default|
|R5b||||||
|1 r5b.large|1250.00 / 10000.00|156.25 / 1250.00|5417.00 / 43333.00|✓|default|
|1 r5b.xlarge|2500.00 / 10000.00|312.50 / 1250.00|10833.00 / 43333.00|✓|default|
|1 r5b.2xlarge|5000.00 / 10000.00|625.00 / 1250.00|21667.00 / 43333.00|✓|default|


Amazon EBS specifications 224


-----

**Instance**


**Baseline /**


**Baseline /**


**Baseline /**


**NVMe** **EBS**

|type|Maximum bandwidth (Mbps)|Maximum throughput (MB/s, 128 KiB I/O)|Maximum IOPS (16 KiB I/O)|Col5|optimization 2|
|---|---|---|---|---|---|
|r5b.4xlarge|10000.00|1250.00|43333.00|✓|default|
|r5b.8xlarge|20000.00|2500.00|86667.00|✓|default|
|r5b.12xlarge|30000.00|3750.00|130000.00|✓|default|
|r5b.16xlarge|40000.00|5000.00|173333.00|✓|default|
|r5b.24xlarge|60000.00|7500.00|260000.00|✓|default|
|r5b.metal|60000.00|7500.00|260000.00|✓|default|
|R5d||||||
|1 r5d.large|650.00 / 4750.00|81.25 / 593.75|3600.00 / 18750.00|✓|default|
|1 r5d.xlarge|1150.00 / 4750.00|143.75 / 593.75|6000.00 / 18750.00|✓|default|
|1 r5d.2xlarge|2300.00 / 4750.00|287.50 / 593.75|12000.00 / 18750.00|✓|default|
|r5d.4xlarge|4750.00|593.75|18750.00|✓|default|
|r5d.8xlarge|6800.00|850.00|30000.00|✓|default|
|r5d.12xlarge|9500.00|1187.50|40000.00|✓|default|
|r5d.16xlarge|13600.00|1700.00|60000.00|✓|default|
|r5d.24xlarge|19000.00|2375.00|80000.00|✓|default|
|r5d.metal|19000.00|2375.00|80000.00|✓|default|


Amazon EBS specifications 225


-----

**Instance**


**Baseline /**


**Baseline /**


**Baseline /**


**NVMe** **EBS**

|type Maximum bandwidth (Mbps) Maximum throughput (MB/s, 128 KiB I/O) Maximum IOPS (16 KiB I/O) optimization 2|Col2|Col3|Col4|Col5|Col6|
|---|---|---|---|---|---|
|R5dn||||||
|1 r5dn.large|650.00 / 4750.00|81.25 / 593.75|3600.00 / 18750.00|✓|default|
|1 r5dn.xlarge|1150.00 / 4750.00|143.75 / 593.75|6000.00 / 18750.00|✓|default|
|r5dn.2xlarge 1|2300.00 / 4750.00|287.50 / 593.75|12000.00 / 18750.00|✓|default|
|r5dn.4xlarge|4750.00|593.75|18750.00|✓|default|
|r5dn.8xlarge|6800.00|850.00|30000.00|✓|default|
|r5dn.12xl arge|9500.00|1187.50|40000.00|✓|default|
|r5dn.16xl arge|13600.00|1700.00|60000.00|✓|default|
|r5dn.24xl arge|19000.00|2375.00|80000.00|✓|default|
|r5dn.metal|19000.00|2375.00|80000.00|✓|default|
|R5n||||||
|1 r5n.large|650.00 / 4750.00|81.25 / 593.75|3600.00 / 18750.00|✓|default|
|1 r5n.xlarge|1150.00 / 4750.00|143.75 / 593.75|6000.00 / 18750.00|✓|default|


Amazon EBS specifications 226


-----

**Instance**


**Baseline /**


**Baseline /**


**Baseline /**


**NVMe** **EBS**

|type|Maximum bandwidth (Mbps)|Maximum throughput (MB/s, 128 KiB I/O)|Maximum IOPS (16 KiB I/O)|Col5|optimization 2|
|---|---|---|---|---|---|
|1 r5n.2xlarge|2300.00 / 4750.00|287.50 / 593.75|12000.00 / 18750.00|✓|default|
|r5n.4xlarge|4750.00|593.75|18750.00|✓|default|
|r5n.8xlarge|6800.00|850.00|30000.00|✓|default|
|r5n.12xlarge|9500.00|1187.50|40000.00|✓|default|
|r5n.16xlarge|13600.00|1700.00|60000.00|✓|default|
|r5n.24xlarge|19000.00|2375.00|80000.00|✓|default|
|r5n.metal|19000.00|2375.00|80000.00|✓|default|
|R6a||||||
|1 r6a.large|650.00 / 10000.00|81.25 / 1250.00|3600.00 / 40000.00|✓|default|
|1 r6a.xlarge|1250.00 / 10000.00|156.25 / 1250.00|6000.00 / 40000.00|✓|default|
|1 r6a.2xlarge|2500.00 / 10000.00|312.50 / 1250.00|12000.00 / 40000.00|✓|default|
|1 r6a.4xlarge|5000.00 / 10000.00|625.00 / 1250.00|20000.00 / 40000.00|✓|default|
|r6a.8xlarge|10000.00|1250.00|40000.00|✓|default|
|r6a.12xlarge|15000.00|1875.00|60000.00|✓|default|
|r6a.16xlarge|20000.00|2500.00|80000.00|✓|default|


Amazon EBS specifications 227


-----

**Instance**


**Baseline /**


**Baseline /**


**Baseline /**


**NVMe** **EBS**

|type|Maximum bandwidth (Mbps)|Maximum throughput (MB/s, 128 KiB I/O)|Maximum IOPS (16 KiB I/O)|Col5|optimization 2|
|---|---|---|---|---|---|
|r6a.24xlarge|30000.00|3750.00|120000.00|✓|default|
|r6a.32xlarge|40000.00|5000.00|160000.00|✓|default|
|r6a.48xlarge|40000.00|5000.00|240000.00|✓|default|
|r6a.metal|40000.00|5000.00|240000.00|✓|default|
|R6g||||||
|r6g.medium 1|315.00 / 4750.00|39.38 / 593.75|2500.00 / 20000.00|✓|default|
|1 r6g.large|630.00 / 4750.00|78.75 / 593.75|3600.00 / 20000.00|✓|default|
|1 r6g.xlarge|1188.00 / 4750.00|148.50 / 593.75|6000.00 / 20000.00|✓|default|
|1 r6g.2xlarge|2375.00 / 4750.00|296.88 / 593.75|12000.00 / 20000.00|✓|default|
|r6g.4xlarge|4750.00|593.75|20000.00|✓|default|
|r6g.8xlarge|9500.00|1187.50|40000.00|✓|default|
|r6g.12xlarge|14250.00|1781.25|50000.00|✓|default|
|r6g.16xlarge|19000.00|2375.00|80000.00|✓|default|
|r6g.metal|19000.00|2375.00|80000.00|✓|default|
|R6gd||||||


Amazon EBS specifications 228


-----

**Instance**


**Baseline /**


**Baseline /**


**Baseline /**


**NVMe** **EBS**

|type|Maximum bandwidth (Mbps)|Maximum throughput (MB/s, 128 KiB I/O)|Maximum IOPS (16 KiB I/O)|Col5|optimization 2|
|---|---|---|---|---|---|
|r6gd.medium 1|315.00 / 4750.00|39.38 / 593.75|2500.00 / 20000.00|✓|default|
|1 r6gd.large|630.00 / 4750.00|78.75 / 593.75|3600.00 / 20000.00|✓|default|
|1 r6gd.xlarge|1188.00 / 4750.00|148.50 / 593.75|6000.00 / 20000.00|✓|default|
|r6gd.2xlarge 1|2375.00 / 4750.00|296.88 / 593.75|12000.00 / 20000.00|✓|default|
|r6gd.4xlarge|4750.00|593.75|20000.00|✓|default|
|r6gd.8xlarge|9500.00|1187.50|40000.00|✓|default|
|r6gd.12xl arge|14250.00|1781.25|50000.00|✓|default|
|r6gd.16xl arge|19000.00|2375.00|80000.00|✓|default|
|r6gd.metal|19000.00|2375.00|80000.00|✓|default|
|R6i||||||
|1 r6i.large|650.00 / 10000.00|81.25 / 1250.00|3600.00 / 40000.00|✓|default|
|1 r6i.xlarge|1250.00 / 10000.00|156.25 / 1250.00|6000.00 / 40000.00|✓|default|
|1 r6i.2xlarge|2500.00 / 10000.00|312.50 / 1250.00|12000.00 / 40000.00|✓|default|


Amazon EBS specifications 229


-----

**Instance**


**Baseline /**


**Baseline /**


**Baseline /**


**NVMe** **EBS**

|type|Maximum bandwidth (Mbps)|Maximum throughput (MB/s, 128 KiB I/O)|Maximum IOPS (16 KiB I/O)|Col5|optimization 2|
|---|---|---|---|---|---|
|1 r6i.4xlarge|5000.00 / 10000.00|625.00 / 1250.00|20000.00 / 40000.00|✓|default|
|r6i.8xlarge|10000.00|1250.00|40000.00|✓|default|
|r6i.12xlarge|15000.00|1875.00|60000.00|✓|default|
|r6i.16xlarge|20000.00|2500.00|80000.00|✓|default|
|r6i.24xlarge|30000.00|3750.00|120000.00|✓|default|
|r6i.32xlarge|40000.00|5000.00|160000.00|✓|default|
|r6i.metal|40000.00|5000.00|160000.00|✓|default|
|R6idn||||||
|1 r6idn.large|1562.00 / 25000.00|195.31 / 3125.00|6250.00 / 100000.00|✓|default|
|1 r6idn.xlarge|3125.00 / 25000.00|390.62 / 3125.00|12500.00 / 100000.00|✓|default|
|r6idn.2xlarge 1|6250.00 / 25000.00|781.25 / 3125.00|25000.00 / 100000.00|✓|default|
|r6idn.4xlarge 1|12500.00 / 25000.00|1562.50 / 3125.00|50000.00 / 100000.00|✓|default|
|r6idn.8xlarge|25000.00|3125.00|100000.00|✓|default|
|r6idn.12x large|37500.00|4687.50|150000.00|✓|default|


Amazon EBS specifications 230


-----

**Instance**


**Baseline /**


**Baseline /**


**Baseline /**


**NVMe** **EBS**

|type|Maximum bandwidth (Mbps)|Maximum throughput (MB/s, 128 KiB I/O)|Maximum IOPS (16 KiB I/O)|Col5|optimization 2|
|---|---|---|---|---|---|
|r6idn.16x large|50000.00|6250.00|200000.00|✓|default|
|r6idn.24x large|75000.00|9375.00|300000.00|✓|default|
|r6idn.32x large|100000.00|12500.00|400000.00|✓|default|
|r6idn.metal|100000.00|12500.00|400000.00|✓|default|
|R6in||||||
|1 r6in.large|1562.00 / 25000.00|195.31 / 3125.00|6250.00 / 100000.00|✓|default|
|1 r6in.xlarge|3125.00 / 25000.00|390.62 / 3125.00|12500.00 / 100000.00|✓|default|
|1 r6in.2xlarge|6250.00 / 25000.00|781.25 / 3125.00|25000.00 / 100000.00|✓|default|
|1 r6in.4xlarge|12500.00 / 25000.00|1562.50 / 3125.00|50000.00 / 100000.00|✓|default|
|r6in.8xlarge|25000.00|3125.00|100000.00|✓|default|
|r6in.12xlarge|37500.00|4687.50|150000.00|✓|default|
|r6in.16xlarge|50000.00|6250.00|200000.00|✓|default|
|r6in.24xlarge|75000.00|9375.00|300000.00|✓|default|
|r6in.32xlarge|100000.00|12500.00|400000.00|✓|default|


Amazon EBS specifications 231


-----

**Instance**


**Baseline /**


**Baseline /**


**Baseline /**


**NVMe** **EBS**

|type|Maximum bandwidth (Mbps)|Maximum throughput (MB/s, 128 KiB I/O)|Maximum IOPS (16 KiB I/O)|Col5|optimization 2|
|---|---|---|---|---|---|
|r6in.metal|100000.00|12500.00|400000.00|✓|default|
|R6id||||||
|1 r6id.large|650.00 / 10000.00|81.25 / 1250.00|3600.00 / 40000.00|✓|default|
|1 r6id.xlarge|1250.00 / 10000.00|156.25 / 1250.00|6000.00 / 40000.00|✓|default|
|1 r6id.2xlarge|2500.00 / 10000.00|312.50 / 1250.00|12000.00 / 40000.00|✓|default|
|1 r6id.4xlarge|5000.00 / 10000.00|625.00 / 1250.00|20000.00 / 40000.00|✓|default|
|r6id.8xlarge|10000.00|1250.00|40000.00|✓|default|
|r6id.12xlarge|15000.00|1875.00|60000.00|✓|default|
|r6id.16xlarge|20000.00|2500.00|80000.00|✓|default|
|r6id.24xlarge|30000.00|3750.00|120000.00|✓|default|
|r6id.32xlarge|40000.00|5000.00|160000.00|✓|default|
|r6id.metal|40000.00|5000.00|160000.00|✓|default|
|R7a||||||
|1 r7a.medium|325.00 / 10000.00|40.62 / 1250.00|2500.00 / 40000.00|✓|default|


Amazon EBS specifications 232


-----

**Instance**


**Baseline /**


**Baseline /**


**Baseline /**


**NVMe** **EBS**

|type|Maximum bandwidth (Mbps)|Maximum throughput (MB/s, 128 KiB I/O)|Maximum IOPS (16 KiB I/O)|Col5|optimization 2|
|---|---|---|---|---|---|
|1 r7a.large|650.00 / 10000.00|81.25 / 1250.00|3600.00 / 40000.00|✓|default|
|1 r7a.xlarge|1250.00 / 10000.00|156.25 / 1250.00|6000.00 / 40000.00|✓|default|
|1 r7a.2xlarge|2500.00 / 10000.00|312.50 / 1250.00|12000.00 / 40000.00|✓|default|
|1 r7a.4xlarge|5000.00 / 10000.00|625.00 / 1250.00|20000.00 / 40000.00|✓|default|
|r7a.8xlarge|10000.00|1250.00|40000.00|✓|default|
|r7a.12xlarge|15000.00|1875.00|60000.00|✓|default|
|r7a.16xlarge|20000.00|2500.00|80000.00|✓|default|
|r7a.24xlarge|30000.00|3750.00|120000.00|✓|default|
|r7a.32xlarge|40000.00|5000.00|160000.00|✓|default|
|r7a.48xlarge|40000.00|5000.00|240000.00|✓|default|
|r7a.metal -48xl|40000.00|5000.00|240000.00|✓|default|
|R7g||||||
|r7g.medium 1|315.00 / 10000.00|39.38 / 1250.00|2500.00 / 40000.00|✓|default|
|1 r7g.large|630.00 / 10000.00|78.75 / 1250.00|3600.00 / 40000.00|✓|default|


Amazon EBS specifications 233


-----

**Instance**


**Baseline /**


**Baseline /**


**Baseline /**


**NVMe** **EBS**

|type|Maximum bandwidth (Mbps)|Maximum throughput (MB/s, 128 KiB I/O)|Maximum IOPS (16 KiB I/O)|Col5|optimization 2|
|---|---|---|---|---|---|
|1 r7g.xlarge|1250.00 / 10000.00|156.25 / 1250.00|6000.00 / 40000.00|✓|default|
|1 r7g.2xlarge|2500.00 / 10000.00|312.50 / 1250.00|12000.00 / 40000.00|✓|default|
|1 r7g.4xlarge|5000.00 / 10000.00|625.00 / 1250.00|20000.00 / 40000.00|✓|default|
|r7g.8xlarge|10000.00|1250.00|40000.00|✓|default|
|r7g.12xlarge|15000.00|1875.00|60000.00|✓|default|
|r7g.16xlarge|20000.00|2500.00|80000.00|✓|default|
|r7g.metal|20000.00|2500.00|80000.00|✓|default|
|R7gd||||||
|r7gd.medium 1|315.00 / 10000.00|39.38 / 1250.00|2500.00 / 40000.00|✓|default|
|1 r7gd.large|630.00 / 10000.00|78.75 / 1250.00|3600.00 / 40000.00|✓|default|
|1 r7gd.xlarge|1250.00 / 10000.00|156.25 / 1250.00|6000.00 / 40000.00|✓|default|
|r7gd.2xlarge 1|2500.00 / 10000.00|312.50 / 1250.00|12000.00 / 40000.00|✓|default|
|r7gd.4xlarge 1|5000.00 / 10000.00|625.00 / 1250.00|20000.00 / 40000.00|✓|default|


Amazon EBS specifications 234


-----

**Instance**


**Baseline /**


**Baseline /**


**Baseline /**


**NVMe** **EBS**

|type|Maximum bandwidth (Mbps)|Maximum throughput (MB/s, 128 KiB I/O)|Maximum IOPS (16 KiB I/O)|Col5|optimization 2|
|---|---|---|---|---|---|
|r7gd.8xlarge|10000.00|1250.00|40000.00|✓|default|
|r7gd.12xl arge|15000.00|1875.00|60000.00|✓|default|
|r7gd.16xl arge|20000.00|2500.00|80000.00|✓|default|
|r7gd.metal|20000.00|2500.00|80000.00|✓|default|
|R7i||||||
|1 r7i.large|650.00 / 10000.00|81.25 / 1250.00|3600.00 / 40000.00|✓|default|
|1 r7i.xlarge|1250.00 / 10000.00|156.25 / 1250.00|6000.00 / 40000.00|✓|default|
|1 r7i.2xlarge|2500.00 / 10000.00|312.50 / 1250.00|12000.00 / 40000.00|✓|default|
|1 r7i.4xlarge|5000.00 / 10000.00|625.00 / 1250.00|20000.00 / 40000.00|✓|default|
|r7i.8xlarge|10000.00|1250.00|40000.00|✓|default|
|r7i.12xlarge|15000.00|1875.00|60000.00|✓|default|
|r7i.16xlarge|20000.00|2500.00|80000.00|✓|default|
|r7i.24xlarge|30000.00|3750.00|120000.00|✓|default|
|r7i.48xlarge|40000.00|5000.00|240000.00|✓|default|


Amazon EBS specifications 235


-----

**Instance**


**Baseline /**


**Baseline /**


**Baseline /**


**NVMe** **EBS**

|type|Maximum bandwidth (Mbps)|Maximum throughput (MB/s, 128 KiB I/O)|Maximum IOPS (16 KiB I/O)|Col5|optimization 2|
|---|---|---|---|---|---|
|r7i.metal -24xl|30000.00|3750.00|120000.00|✓|default|
|r7i.metal -48xl|40000.00|5000.00|240000.00|✓|default|
|R7iz||||||
|1 r7iz.large|792.00 / 10000.00|99.00 / 1250.00|3600.00 / 40000.00|✓|default|
|1 r7iz.xlarge|1584.00 / 10000.00|198.00 / 1250.00|6667.00 / 40000.00|✓|default|
|1 r7iz.2xlarge|3168.00 / 10000.00|396.00 / 1250.00|13333.00 / 40000.00|✓|default|
|1 r7iz.4xlarge|5000.00 / 10000.00|625.00 / 1250.00|20000.00 / 40000.00|✓|default|
|r7iz.8xlarge|10000.00|1250.00|40000.00|✓|default|
|r7iz.12xlarge|19000.00|2375.00|76000.00|✓|default|
|r7iz.16xlarge|20000.00|2500.00|80000.00|✓|default|
|r7iz.32xlarge|40000.00|5000.00|160000.00|✓|default|
|r7iz.meta l-16xl|20000.00|2500.00|80000.00|✓|default|
|r7iz.meta l-32xl|40000.00|5000.00|160000.00|✓|default|


Amazon EBS specifications 236


-----

**Instance**


**Baseline /**


**Baseline /**


**Baseline /**


**NVMe** **EBS**

|type Maximum bandwidth (Mbps) Maximum throughput (MB/s, 128 KiB I/O) Maximum IOPS (16 KiB I/O) optimization 2|Col2|Col3|Col4|Col5|Col6|
|---|---|---|---|---|---|
|R8g||||||
|r8g.medium 1|315.00 / 10000.00|39.38 / 1250.00|2500.00 / 40000.00|✓|default|
|1 r8g.large|630.00 / 10000.00|78.75 / 1250.00|3600.00 / 40000.00|✓|default|
|1 r8g.xlarge|1250.00 / 10000.00|156.25 / 1250.00|6000.00 / 40000.00|✓|default|
|1 r8g.2xlarge|2500.00 / 10000.00|312.50 / 1250.00|12000.00 / 40000.00|✓|default|
|1 r8g.4xlarge|5000.00 / 10000.00|625.00 / 1250.00|20000.00 / 40000.00|✓|default|
|r8g.8xlarge|10000.00|1250.00|40000.00|✓|default|
|r8g.12xlarge|15000.00|1875.00|60000.00|✓|default|
|r8g.16xlarge|20000.00|2500.00|80000.00|✓|default|
|r8g.24xlarge|30000.00|3750.00|120000.00|✓|default|
|r8g.48xlarge|40000.00|5000.00|240000.00|✓|default|
|r8g.metal -24xl|30000.00|3750.00|120000.00|✓|default|
|r8g.metal -48xl|40000.00|5000.00|240000.00|✓|default|
|U-3tb1||||||


Amazon EBS specifications 237


-----

**Instance**


**Baseline /**


**Baseline /**


**Baseline /**


**NVMe** **EBS**

|type|Maximum bandwidth (Mbps)|Maximum throughput (MB/s, 128 KiB I/O)|Maximum IOPS (16 KiB I/O)|Col5|optimization 2|
|---|---|---|---|---|---|
|u-3tb1.56 xlarge|19000.00|2375.00|80000.00|✓|default|
|U-6tb1||||||
|u-6tb1.56 xlarge|38000.00|4750.00|160000.00|✓|default|
|u-6tb1.11 2xlarge|38000.00|4750.00|160000.00|✓|default|
|u-6tb1.metal|38000.00|4750.00|160000.00|✓|default|
|U-9tb1||||||
|u-9tb1.11 2xlarge|38000.00|4750.00|160000.00|✓|default|
|u-9tb1.metal|38000.00|4750.00|160000.00|✓|default|
|U-12tb1||||||
|u-12tb1.1 12xlarge|38000.00|4750.00|160000.00|✓|default|
|u-12tb1.m etal|38000.00|4750.00|160000.00|✓|default|
|U-18tb1||||||
|u-18tb1.1 12xlarge|38000.00|4750.00|160000.00|✓|default|


Amazon EBS specifications 238


-----

**Instance**


**Baseline /**


**Baseline /**


**Baseline /**


**NVMe** **EBS**

|type|Maximum bandwidth (Mbps)|Maximum throughput (MB/s, 128 KiB I/O)|Maximum IOPS (16 KiB I/O)|Col5|optimization 2|
|---|---|---|---|---|---|
|u-18tb1.m etal|38000.00|4750.00|160000.00|✓|default|
|U-24tb1||||||
|u-24tb1.1 12xlarge|38000.00|4750.00|160000.00|✓|default|
|u-24tb1.m etal|38000.00|4750.00|160000.00|✓|default|
|U7i-12tb||||||
|u7i-12tb. 224xlarge|60000.00|7500.00|420000.00|✓|default|
|U7in-16tb||||||
|u7in-16tb .224xlarge|100000.00|12500.00|420000.00|✓|default|
|U7in-24tb||||||
|u7in-24tb .224xlarge|100000.00|12500.00|420000.00|✓|default|
|U7in-32tb||||||
|u7in-32tb .224xlarge|100000.00|12500.00|420000.00|✓|default|
|X1||||||
|x1.16xlarge|7000.00|875.00|40000.00|✗|default|


Amazon EBS specifications 239


-----

**Instance**


**Baseline /**


**Baseline /**


**Baseline /**


**NVMe** **EBS**

|type|Maximum bandwidth (Mbps)|Maximum throughput (MB/s, 128 KiB I/O)|Maximum IOPS (16 KiB I/O)|Col5|optimization 2|
|---|---|---|---|---|---|
|x1.32xlarge|14000.00|1750.00|80000.00|✗|default|
|X2gd||||||
|x2gd.medi 1 um|315.00 / 4750.00|39.38 / 593.75|2500.00 / 20000.00|✓|default|
|1 x2gd.large|630.00 / 4750.00|78.75 / 593.75|3600.00 / 20000.00|✓|default|
|1 x2gd.xlarge|1188.00 / 4750.00|148.50 / 593.75|6000.00 / 20000.00|✓|default|
|x2gd.2xlarge 1|2375.00 / 4750.00|296.88 / 593.75|12000.00 / 20000.00|✓|default|
|x2gd.4xlarge|4750.00|593.75|20000.00|✓|default|
|x2gd.8xlarge|9500.00|1187.50|40000.00|✓|default|
|x2gd.12xl arge|14250.00|1781.25|60000.00|✓|default|
|x2gd.16xl arge|19000.00|2375.00|80000.00|✓|default|
|x2gd.metal|19000.00|2375.00|80000.00|✓|default|
|X2idn||||||
|x2idn.16x large|40000.00|5000.00|173333.00|✓|default|


Amazon EBS specifications 240


-----

**Instance**


**Baseline /**


**Baseline /**


**Baseline /**


**NVMe** **EBS**

|type|Maximum bandwidth (Mbps)|Maximum throughput (MB/s, 128 KiB I/O)|Maximum IOPS (16 KiB I/O)|Col5|optimization 2|
|---|---|---|---|---|---|
|x2idn.24x large|60000.00|7500.00|260000.00|✓|default|
|x2idn.32x large|80000.00|10000.00|260000.00|✓|default|
|x2idn.metal|80000.00|10000.00|260000.00|✓|default|
|X2iedn||||||
|x2iedn.xlarge 1|2500.00 / 20000.00|312.50 / 2500.00|8125.00 / 65000.00|✓|default|
|x2iedn.2x 1 large|5000.00 / 20000.00|625.00 / 2500.00|16250.00 / 65000.00|✓|default|
|x2iedn.4x 1 large|10000.00 / 20000.00|1250.00 / 2500.00|32500.00 / 65000.00|✓|default|
|x2iedn.8x large|20000.00|2500.00|65000.00|✓|default|
|x2iedn.16 xlarge|40000.00|5000.00|130000.00|✓|default|
|x2iedn.24 xlarge|60000.00|7500.00|195000.00|✓|default|
|x2iedn.32 xlarge|80000.00|10000.00|260000.00|✓|default|
|x2iedn.metal|80000.00|10000.00|260000.00|✓|default|
|X2iezn||||||


Amazon EBS specifications 241


-----

**Instance**


**Baseline /**


**Baseline /**


**Baseline /**


**NVMe** **EBS**

|type|Maximum bandwidth (Mbps)|Maximum throughput (MB/s, 128 KiB I/O)|Maximum IOPS (16 KiB I/O)|Col5|optimization 2|
|---|---|---|---|---|---|
|x2iezn.2x large|3170.00|396.25|13333.00|✓|default|
|x2iezn.4x large|4750.00|593.75|20000.00|✓|default|
|x2iezn.6x large|9500.00|1187.50|40000.00|✓|default|
|x2iezn.8x large|12000.00|1500.00|55000.00|✓|default|
|x2iezn.12 xlarge|19000.00|2375.00|80000.00|✓|default|
|x2iezn.metal|19000.00|2375.00|80000.00|✓|default|
|X1e||||||
|x1e.xlarge|500.00|62.50|3700.00|✗|default|
|x1e.2xlarge|1000.00|125.00|7400.00|✗|default|
|x1e.4xlarge|1750.00|218.75|10000.00|✗|default|
|x1e.8xlarge|3500.00|437.50|20000.00|✗|default|
|x1e.16xlarge|7000.00|875.00|40000.00|✗|default|
|x1e.32xlarge|14000.00|1750.00|80000.00|✗|default|
|z1d||||||


Amazon EBS specifications 242


-----

**Instance**

|type|Maximum bandwidth (Mbps)|Maximum throughput (MB/s, 128 KiB I/O)|Maximum IOPS (16 KiB I/O)|Col5|optimization 2|
|---|---|---|---|---|---|
|1 z1d.large|800.00 / 3170.00|100.00 / 396.25|3333.00 / 13333.00|✓|default|
|1 z1d.xlarge|1580.00 / 3170.00|197.50 / 396.25|6667.00 / 13333.00|✓|default|
|z1d.2xlarge|3170.00|396.25|13333.00|✓|default|
|z1d.3xlarge|4750.00|593.75|20000.00|✓|default|
|z1d.6xlarge|9500.00|1187.50|40000.00|✓|default|
|z1d.12xlarge|19000.00|2375.00|80000.00|✓|default|
|z1d.metal|19000.00|2375.00|80000.00|✓|default|



**Note**


**Baseline /**
**Maximum**
**bandwidth**
**(Mbps)**


**Baseline /**
**Maximum**
**throughput**
**(MB/s, 128**
**KiB I/O)**


**Baseline /**
**Maximum**
**IOPS (16 KiB**
**I/O)**


**NVMe** **EBS**
**optimization**


1
These instances can support maximum performance for 30 minutes at least once every 24
hours, after which they revert to their baseline performance. Other instances can sustain
the maximum performance indefinitely. If your workload requires sustained maximum
performance for longer than 30 minutes, use one of these instances.
2
```
   default indicates that instances are enabled for EBS optimization by default.
   supported indicates that instances can optionally be enabled for EBS optimization For

```
[more information, see Amazon EBS–optimized instances.](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-optimized.html)

#### Instance store specifications

The following table shows the instance store volume configuration for supported instance types,
along with the aggregated IOPS performance with 4,096 byte block size at queue depth saturation.

Instance store specifications 243


-----

|Instance type|Instance store volumes|Instance store type|100% random read IOPS / Write IOPS|Needs initializ 1 ation|TRIM support 2|
|---|---|---|---|---|---|
|R5ad||||||
|r5ad.large|1 x 75 GB|NVMe SSD|30,000 / 15,000||✓|
|r5ad.xlarge|1 x 150 GB|NVMe SSD|59,000 / 29,000||✓|
|r5ad.2xlarge|1 x 300 GB|NVMe SSD|117,000 / 57,000||✓|
|r5ad.4xlarge|2 x 300 GB|NVMe SSD|234,000 / 114,000||✓|
|r5ad.8xlarge|2 x 600 GB|NVMe SSD|466,666 / 233,334||✓|
|r5ad.12xlarge|2 x 900 GB|NVMe SSD|700,000 / 340,000||✓|
|r5ad.16xlarge|4 x 600 GB|NVMe SSD|933,332 / 466,668||✓|
|r5ad.24xlarge|4 x 900 GB|NVMe SSD|1,400,000 / 680,000||✓|
|R5d||||||
|r5d.large|1 x 75 GB|NVMe SSD|30,000 / 15,000||✓|
|r5d.xlarge|1 x 150 GB|NVMe SSD|59,000 / 29,000||✓|


Instance store specifications 244


-----

|Instance type|Instance store volumes|Instance store type|100% random read IOPS / Write IOPS|Needs initializ ation 1|TRIM support 2|
|---|---|---|---|---|---|
|r5d.2xlarge|1 x 300 GB|NVMe SSD|117,000 / 57,000||✓|
|r5d.4xlarge|2 x 300 GB|NVMe SSD|234,000 / 114,000||✓|
|r5d.8xlarge|2 x 600 GB|NVMe SSD|466,666 / 233,334||✓|
|r5d.12xlarge|2 x 900 GB|NVMe SSD|700,000 / 340,000||✓|
|r5d.16xlarge|4 x 600 GB|NVMe SSD|933,332 / 466,668||✓|
|r5d.24xlarge|4 x 900 GB|NVMe SSD|1,400,000 / 680,000||✓|
|r5d.metal|4 x 900 GB|NVMe SSD|1,400,000 / 680,000||✓|
|R5dn||||||
|r5dn.large|1 x 75 GB|NVMe SSD|29,000 / 14,500||✓|
|r5dn.xlarge|1 x 150 GB|NVMe SSD|58,000 / 29,000||✓|
|r5dn.2xlarge|1 x 300 GB|NVMe SSD|116,000 / 58,000||✓|
|r5dn.4xlarge|2 x 300 GB|NVMe SSD|232,000 / 116,000||✓|


Instance store specifications 245


-----

|Instance type|Instance store volumes|Instance store type|100% random read IOPS / Write IOPS|Needs initializ ation 1|TRIM support 2|
|---|---|---|---|---|---|
|r5dn.8xlarge|2 x 600 GB|NVMe SSD|464,000 / 232,000||✓|
|r5dn.12xlarge|2 x 900 GB|NVMe SSD|700,000 / 350,000||✓|
|r5dn.16xlarge|4 x 600 GB|NVMe SSD|930,000 / 465,000||✓|
|r5dn.24xlarge|4 x 900 GB|NVMe SSD|1,400,000 / 700,000||✓|
|r5dn.metal|4 x 900 GB|NVMe SSD|1,400,000 / 700,000||✓|
|R6gd||||||
|r6gd.medium|1 x 59 GB|NVMe SSD|13,438 / 5,625||✓|
|r6gd.large|1 x 118 GB|NVMe SSD|26,875 / 11,250||✓|
|r6gd.xlarge|1 x 237 GB|NVMe SSD|53,750 / 22,500||✓|
|r6gd.2xlarge|1 x 474 GB|NVMe SSD|107,500 / 45,000||✓|
|r6gd.4xlarge|1 x 950 GB|NVMe SSD|215,000 / 90,000||✓|
|r6gd.8xlarge|1 x 1900 GB|NVMe SSD|430,000 / 180,000||✓|


Instance store specifications 246


-----

|Instance type|Instance store volumes|Instance store type|100% random read IOPS / Write IOPS|Needs initializ ation 1|TRIM support 2|
|---|---|---|---|---|---|
|r6gd.12xlarge|2 x 1425 GB|NVMe SSD|645,000 / 270,000||✓|
|r6gd.16xlarge|2 x 1900 GB|NVMe SSD|860,000 / 360,000||✓|
|r6gd.metal|2 x 1900 GB|NVMe SSD|860,000 / 360,000||✓|
|R6idn||||||
|r6idn.large|1 x 118 GB|NVMe SSD|33,542 / 16,771||✓|
|r6idn.xlarge|1 x 237 GB|NVMe SSD|67,083 / 33,542||✓|
|r6idn.2xlarge|1 x 474 GB|NVMe SSD|134,167 / 67,084||✓|
|r6idn.4xlarge|1 x 950 GB|NVMe SSD|268,333 / 134,167||✓|
|r6idn.8xlarge|1 x 1900 GB|NVMe SSD|536,666 / 268,334||✓|
|r6idn.12xlarge|2 x 1425 GB|NVMe SSD|804,998 / 402,500||✓|
|r6idn.16xlarge|2 x 1900 GB|NVMe SSD|1,073,332 / 536,668||✓|
|r6idn.24xlarge|4 x 1425 GB|NVMe SSD|1,609,996 / 805,000||✓|


Instance store specifications 247


-----

|Instance type|Instance store volumes|Instance store type|100% random read IOPS / Write IOPS|Needs initializ ation 1|TRIM support 2|
|---|---|---|---|---|---|
|r6idn.32xlarge|4 x 1900 GB|NVMe SSD|2,146,664 / 1,073,336||✓|
|r6idn.metal|4 x 1900 GB|NVMe SSD|2,146,664 / 1,073,336||✓|
|R6id||||||
|r6id.large|1 x 118 GB|NVMe SSD|33,542 / 16,771||✓|
|r6id.xlarge|1 x 237 GB|NVMe SSD|67,083 / 33,542||✓|
|r6id.2xlarge|1 x 474 GB|NVMe SSD|134,167 / 67,084||✓|
|r6id.4xlarge|1 x 950 GB|NVMe SSD|268,333 / 134,167||✓|
|r6id.8xlarge|1 x 1900 GB|NVMe SSD|536,666 / 268,334||✓|
|r6id.12xlarge|2 x 1425 GB|NVMe SSD|804,998 / 402,500||✓|
|r6id.16xlarge|2 x 1900 GB|NVMe SSD|1,073,332 / 536,668||✓|
|r6id.24xlarge|4 x 1425 GB|NVMe SSD|1,609,996 / 805,000||✓|
|r6id.32xlarge|4 x 1900 GB|NVMe SSD|2,146,664 / 1,073,336||✓|


Instance store specifications 248


-----

|Instance type|Instance store volumes|Instance store type|100% random read IOPS / Write IOPS|Needs initializ ation 1|TRIM support 2|
|---|---|---|---|---|---|
|r6id.metal|4 x 1900 GB|NVMe SSD|2,146,664 / 1,073,336||✓|
|R7gd||||||
|r7gd.medium|1 x 59 GB|NVMe SSD|16,771 / 8,385||✓|
|r7gd.large|1 x 118 GB|NVMe SSD|33,542 / 16,771||✓|
|r7gd.xlarge|1 x 237 GB|NVMe SSD|67,083 / 33,542||✓|
|r7gd.2xlarge|1 x 474 GB|NVMe SSD|134,167 / 67,084||✓|
|r7gd.4xlarge|1 x 950 GB|NVMe SSD|268,333 / 134,167||✓|
|r7gd.8xlarge|1 x 1900 GB|NVMe SSD|536,666 / 268,334||✓|
|r7gd.12xlarge|2 x 1425 GB|NVMe SSD|804,998 / 402,500||✓|
|r7gd.16xlarge|2 x 1900 GB|NVMe SSD|1,073,332 / 536,668||✓|
|r7gd.metal|2 x 1900 GB|NVMe SSD|1,073,332 / 536,668||✓|
|X1||||||
|x1.16xlarge|1 x 1920 GB|SSD||✓||


Instance store specifications 249


-----

|Instance type|Instance store volumes|Instance store type|100% random read IOPS / Write IOPS|Needs initializ ation 1|TRIM support 2|
|---|---|---|---|---|---|
|x1.32xlarge|2 x 1920 GB|SSD||✓||
|X2gd||||||
|x2gd.medium|1 x 59 GB|NVMe SSD|13,438 / 5,625||✓|
|x2gd.large|1 x 118 GB|NVMe SSD|26,875 / 11,250||✓|
|x2gd.xlarge|1 x 237 GB|NVMe SSD|53,750 / 22,500||✓|
|x2gd.2xlarge|1 x 475 GB|NVMe SSD|107,500 / 45,000||✓|
|x2gd.4xlarge|1 x 950 GB|NVMe SSD|215,000 / 90,000||✓|
|x2gd.8xlarge|1 x 1900 GB|NVMe SSD|430,000 / 180,000||✓|
|x2gd.12xlarge|2 x 1425 GB|NVMe SSD|645,000 / 270,000||✓|
|x2gd.16xlarge|2 x 1900 GB|NVMe SSD|860,000 / 360,000||✓|
|x2gd.metal|2 x 1900 GB|NVMe SSD|860,000 / 360,000||✓|
|X2idn||||||
|x2idn.16xlarge|1 x 1900 GB|NVMe SSD|430,000 / 180,000||✓|


Instance store specifications 250


-----

|Instance type|Instance store volumes|Instance store type|100% random read IOPS / Write IOPS|Needs initializ ation 1|TRIM support 2|
|---|---|---|---|---|---|
|x2idn.24xlarge|2 x 1425 GB|NVMe SSD|645,000 / 270,000||✓|
|x2idn.32xlarge|2 x 1900 GB|NVMe SSD|860,000 / 360,000||✓|
|x2idn.metal|2 x 1900 GB|NVMe SSD|860,000 / 360,000||✓|
|X2iedn||||||
|x2iedn.xlarge|1 x 118 GB|NVMe SSD|26,875 / 11,250||✓|
|x2iedn.2xlarge|1 x 237 GB|NVMe SSD|53,750 / 22,500||✓|
|x2iedn.4xlarge|1 x 475 GB|NVMe SSD|107,500 / 45,000||✓|
|x2iedn.8xlarge|1 x 950 GB|NVMe SSD|215,000 / 90,000||✓|
|x2iedn.16xlarge|1 x 1900 GB|NVMe SSD|430,000 / 180,000||✓|
|x2iedn.24xlarge|2 x 1425 GB|NVMe SSD|645,000 / 270,000||✓|
|x2iedn.32xlarge|2 x 1900 GB|NVMe SSD|860,000 / 360,000||✓|
|x2iedn.metal|2 x 1900 GB|NVMe SSD|860,000 / 360,000||✓|
|X1e||||||


Instance store specifications 251


-----

|Instance type|Instance store volumes|Instance store type|100% random read IOPS / Write IOPS|Needs initializ ation 1|TRIM support 2|
|---|---|---|---|---|---|
|x1e.xlarge|1 x 120 GB|SSD||✓||
|x1e.2xlarge|1 x 240 GB|SSD||✓||
|x1e.4xlarge|1 x 480 GB|SSD||✓||
|x1e.8xlarge|1 x 960 GB|SSD||✓||
|x1e.16xlarge|1 x 1920 GB|SSD||✓||
|x1e.32xlarge|2 x 1920 GB|SSD||✓||
|z1d||||||
|z1d.large|1 x 75 GB|NVMe SSD|30,000 / 15,000||✓|
|z1d.xlarge|1 x 150 GB|NVMe SSD|59,000 / 29,000||✓|
|z1d.2xlarge|1 x 300 GB|NVMe SSD|117,000 / 57,000||✓|
|z1d.3xlarge|1 x 450 GB|NVMe SSD|175,000 / 75,000||✓|
|z1d.6xlarge|1 x 900 GB|NVMe SSD|350,000 / 170,000||✓|
|z1d.12xlarge|2 x 900 GB|NVMe SSD|700,000 / 340,000||✓|
|z1d.metal|2 x 900 GB|NVMe SSD|700,000 / 340,000||✓|


Instance store specifications 252


-----

1
Volumes attached to certain instances suffer a first-write penalty unless initialized. For more
[information, see Optimize disk performance for instance store volumes.](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/disk-performance.html)

2
[For more information, see Instance store volume TRIM support.](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ssd-instance-store.html#InstanceStoreTrimSupport)

#### Security specifications

|Instance type|EBS encryptio n|Instance store encryptio n|Encryptio n in transit|AMD SEV-SNP|NitroTPM|Nitro Enclaves|
|---|---|---|---|---|---|---|
|R5|||||||
|r5.large|✓|Instance store not supported|✗|✗|✓|✗|
|r5.xlarge|✓|Instance store not supported|✗|✗|✓|✓|
|r5.2xlarge|✓|Instance store not supported|✗|✗|✓|✓|
|r5.4xlarge|✓|Instance store not supported|✗|✗|✓|✓|
|r5.8xlarge|✓|Instance store not supported|✗|✗|✓|✓|
|r5.12xlarge|✓|Instance store not supported|✗|✗|✓|✓|



Security specifications 253


-----

|Instance type|EBS encryptio n|Instance store encryptio n|Encryptio n in transit|AMD SEV-SNP|NitroTPM|Nitro Enclaves|
|---|---|---|---|---|---|---|
|r5.16xlarge|✓|Instance store not supported|✗|✗|✓|✓|
|r5.24xlarge|✓|Instance store not supported|✗|✗|✓|✓|
|r5.metal|✓|Instance store not supported|✗|✗|✗|✗|
|R5a|||||||
|r5a.large|✓|Instance store not supported|✗|✗|✓|✗|
|r5a.xlarge|✓|Instance store not supported|✗|✗|✓|✓|
|r5a.2xlarge|✓|Instance store not supported|✗|✗|✓|✓|
|r5a.4xlarge|✓|Instance store not supported|✗|✗|✓|✓|
|r5a.8xlarge|✓|Instance store not supported|✗|✗|✓|✓|


Security specifications 254


-----

|Instance type|EBS encryptio n|Instance store encryptio n|Encryptio n in transit|AMD SEV-SNP|NitroTPM|Nitro Enclaves|
|---|---|---|---|---|---|---|
|r5a.12xlarge|✓|Instance store not supported|✗|✗|✓|✓|
|r5a.16xlarge|✓|Instance store not supported|✗|✗|✓|✓|
|r5a.24xlarge|✓|Instance store not supported|✗|✗|✓|✓|
|R5ad|||||||
|r5ad.large|✓|✓|✗|✗|✓|✗|
|r5ad.xlarge|✓|✓|✗|✗|✓|✓|
|r5ad.2xlarge|✓|✓|✗|✗|✓|✓|
|r5ad.4xlarge|✓|✓|✗|✗|✓|✓|
|r5ad.8xlarge|✓|✓|✗|✗|✓|✓|
|r5ad.12xlarge|✓|✓|✗|✗|✓|✓|
|r5ad.16xlarge|✓|✓|✗|✗|✓|✓|
|r5ad.24xlarge|✓|✓|✗|✗|✓|✓|
|R5b|||||||
|r5b.large|✓|Instance store not supported|✗|✗|✓|✗|


Security specifications 255


-----

|Instance type|EBS encryptio n|Instance store encryptio n|Encryptio n in transit|AMD SEV-SNP|NitroTPM|Nitro Enclaves|
|---|---|---|---|---|---|---|
|r5b.xlarge|✓|Instance store not supported|✗|✗|✓|✓|
|r5b.2xlarge|✓|Instance store not supported|✗|✗|✓|✓|
|r5b.4xlarge|✓|Instance store not supported|✗|✗|✓|✓|
|r5b.8xlarge|✓|Instance store not supported|✗|✗|✓|✓|
|r5b.12xlarge|✓|Instance store not supported|✗|✗|✓|✓|
|r5b.16xlarge|✓|Instance store not supported|✗|✗|✓|✓|
|r5b.24xlarge|✓|Instance store not supported|✗|✗|✓|✓|
|r5b.metal|✓|Instance store not supported|✗|✗|✗|✗|
|R5d|||||||


Security specifications 256


-----

|Instance type|EBS encryptio n|Instance store encryptio n|Encryptio n in transit|AMD SEV-SNP|NitroTPM|Nitro Enclaves|
|---|---|---|---|---|---|---|
|r5d.large|✓|✓|✗|✗|✓|✗|
|r5d.xlarge|✓|✓|✗|✗|✓|✓|
|r5d.2xlarge|✓|✓|✗|✗|✓|✓|
|r5d.4xlarge|✓|✓|✗|✗|✓|✓|
|r5d.8xlarge|✓|✓|✗|✗|✓|✓|
|r5d.12xlarge|✓|✓|✗|✗|✓|✓|
|r5d.16xlarge|✓|✓|✗|✗|✓|✓|
|r5d.24xlarge|✓|✓|✗|✗|✓|✓|
|r5d.metal|✓|✓|✗|✗|✗|✗|
|R5dn|||||||
|r5dn.large|✓|✓|✓|✗|✓|✗|
|r5dn.xlarge|✓|✓|✓|✗|✓|✓|
|r5dn.2xlarge|✓|✓|✓|✗|✓|✓|
|r5dn.4xlarge|✓|✓|✓|✗|✓|✓|
|r5dn.8xlarge|✓|✓|✓|✗|✓|✓|
|r5dn.12xlarge|✓|✓|✓|✗|✓|✓|
|r5dn.16xlarge|✓|✓|✓|✗|✓|✓|
|r5dn.24xlarge|✓|✓|✓|✗|✓|✓|
|r5dn.metal|✓|✓|✓|✗|✗|✗|


Security specifications 257


-----

|Instance type EBS encryptio n Instance store encryptio n Encryptio n in transit AMD SEV-SNP NitroTPM Nitro Enclaves|Col2|Col3|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
|R5n|||||||
|r5n.large|✓|Instance store not supported|✓|✗|✓|✗|
|r5n.xlarge|✓|Instance store not supported|✓|✗|✓|✓|
|r5n.2xlarge|✓|Instance store not supported|✓|✗|✓|✓|
|r5n.4xlarge|✓|Instance store not supported|✓|✗|✓|✓|
|r5n.8xlarge|✓|Instance store not supported|✓|✗|✓|✓|
|r5n.12xlarge|✓|Instance store not supported|✓|✗|✓|✓|
|r5n.16xlarge|✓|Instance store not supported|✓|✗|✓|✓|
|r5n.24xlarge|✓|Instance store not supported|✓|✗|✓|✓|


Security specifications 258


-----

|Instance type|EBS encryptio n|Instance store encryptio n|Encryptio n in transit|AMD SEV-SNP|NitroTPM|Nitro Enclaves|
|---|---|---|---|---|---|---|
|r5n.metal|✓|Instance store not supported|✓|✗|✗|✗|
|R6a|||||||
|r6a.large|✓|Instance store not supported|✓|✓|✓|✗|
|r6a.xlarge|✓|Instance store not supported|✓|✓|✓|✓|
|r6a.2xlarge|✓|Instance store not supported|✓|✓|✓|✓|
|r6a.4xlarge|✓|Instance store not supported|✓|✓|✓|✓|
|r6a.8xlarge|✓|Instance store not supported|✓|✗|✓|✓|
|r6a.12xlarge|✓|Instance store not supported|✓|✗|✓|✓|
|r6a.16xlarge|✓|Instance store not supported|✓|✗|✓|✓|


Security specifications 259


-----

|Instance type|EBS encryptio n|Instance store encryptio n|Encryptio n in transit|AMD SEV-SNP|NitroTPM|Nitro Enclaves|
|---|---|---|---|---|---|---|
|r6a.24xlarge|✓|Instance store not supported|✓|✗|✓|✓|
|r6a.32xlarge|✓|Instance store not supported|✓|✗|✓|✓|
|r6a.48xlarge|✓|Instance store not supported|✓|✗|✓|✓|
|r6a.metal|✓|Instance store not supported|✓|✗|✗|✗|
|R6g|||||||
|r6g.medium|✓|Instance store not supported|✗|✗|✗|✗|
|r6g.large|✓|Instance store not supported|✗|✗|✗|✓|
|r6g.xlarge|✓|Instance store not supported|✗|✗|✗|✓|
|r6g.2xlarge|✓|Instance store not supported|✗|✗|✗|✓|


Security specifications 260


-----

|Instance type|EBS encryptio n|Instance store encryptio n|Encryptio n in transit|AMD SEV-SNP|NitroTPM|Nitro Enclaves|
|---|---|---|---|---|---|---|
|r6g.4xlarge|✓|Instance store not supported|✗|✗|✗|✓|
|r6g.8xlarge|✓|Instance store not supported|✗|✗|✗|✓|
|r6g.12xlarge|✓|Instance store not supported|✗|✗|✗|✓|
|r6g.16xlarge|✓|Instance store not supported|✗|✗|✗|✓|
|r6g.metal|✓|Instance store not supported|✗|✗|✗|✗|
|R6gd|||||||
|r6gd.medium|✓|✓|✗|✗|✗|✗|
|r6gd.large|✓|✓|✗|✗|✗|✓|
|r6gd.xlarge|✓|✓|✗|✗|✗|✓|
|r6gd.2xlarge|✓|✓|✗|✗|✗|✓|
|r6gd.4xlarge|✓|✓|✗|✗|✗|✓|
|r6gd.8xlarge|✓|✓|✗|✗|✗|✓|
|r6gd.12xlarge|✓|✓|✗|✗|✗|✓|


Security specifications 261


-----

|Instance type|EBS encryptio n|Instance store encryptio n|Encryptio n in transit|AMD SEV-SNP|NitroTPM|Nitro Enclaves|
|---|---|---|---|---|---|---|
|r6gd.16xlarge|✓|✓|✗|✗|✗|✓|
|r6gd.metal|✓|✓|✗|✗|✗|✗|
|R6i|||||||
|r6i.large|✓|Instance store not supported|✓|✗|✓|✗|
|r6i.xlarge|✓|Instance store not supported|✓|✗|✓|✓|
|r6i.2xlarge|✓|Instance store not supported|✓|✗|✓|✓|
|r6i.4xlarge|✓|Instance store not supported|✓|✗|✓|✓|
|r6i.8xlarge|✓|Instance store not supported|✓|✗|✓|✓|
|r6i.12xlarge|✓|Instance store not supported|✓|✗|✓|✓|
|r6i.16xlarge|✓|Instance store not supported|✓|✗|✓|✓|


Security specifications 262


-----

|Instance type|EBS encryptio n|Instance store encryptio n|Encryptio n in transit|AMD SEV-SNP|NitroTPM|Nitro Enclaves|
|---|---|---|---|---|---|---|
|r6i.24xlarge|✓|Instance store not supported|✓|✗|✓|✓|
|r6i.32xlarge|✓|Instance store not supported|✓|✗|✓|✓|
|r6i.metal|✓|Instance store not supported|✓|✗|✗|✗|
|R6idn|||||||
|r6idn.large|✓|✓|✓|✗|✓|✗|
|r6idn.xlarge|✓|✓|✓|✗|✓|✓|
|r6idn.2xlarge|✓|✓|✓|✗|✓|✓|
|r6idn.4xlarge|✓|✓|✓|✗|✓|✓|
|r6idn.8xlarge|✓|✓|✓|✗|✓|✓|
|r6idn.12xlarge|✓|✓|✓|✗|✓|✓|
|r6idn.16xlarge|✓|✓|✓|✗|✓|✓|
|r6idn.24xlarge|✓|✓|✓|✗|✓|✓|
|r6idn.32xlarge|✓|✓|✓|✗|✓|✓|
|r6idn.metal|✓|✓|✓|✗|✗|✗|
|R6in|||||||


Security specifications 263


-----

|Instance type|EBS encryptio n|Instance store encryptio n|Encryptio n in transit|AMD SEV-SNP|NitroTPM|Nitro Enclaves|
|---|---|---|---|---|---|---|
|r6in.large|✓|Instance store not supported|✓|✗|✓|✗|
|r6in.xlarge|✓|Instance store not supported|✓|✗|✓|✓|
|r6in.2xlarge|✓|Instance store not supported|✓|✗|✓|✓|
|r6in.4xlarge|✓|Instance store not supported|✓|✗|✓|✓|
|r6in.8xlarge|✓|Instance store not supported|✓|✗|✓|✓|
|r6in.12xlarge|✓|Instance store not supported|✓|✗|✓|✓|
|r6in.16xlarge|✓|Instance store not supported|✓|✗|✓|✓|
|r6in.24xlarge|✓|Instance store not supported|✓|✗|✓|✓|


Security specifications 264


-----

|Instance type|EBS encryptio n|Instance store encryptio n|Encryptio n in transit|AMD SEV-SNP|NitroTPM|Nitro Enclaves|
|---|---|---|---|---|---|---|
|r6in.32xlarge|✓|Instance store not supported|✓|✗|✓|✓|
|r6in.metal|✓|Instance store not supported|✓|✗|✗|✗|
|R6id|||||||
|r6id.large|✓|✓|✓|✗|✓|✗|
|r6id.xlarge|✓|✓|✓|✗|✓|✓|
|r6id.2xlarge|✓|✓|✓|✗|✓|✓|
|r6id.4xlarge|✓|✓|✓|✗|✓|✓|
|r6id.8xlarge|✓|✓|✓|✗|✓|✓|
|r6id.12xlarge|✓|✓|✓|✗|✓|✓|
|r6id.16xlarge|✓|✓|✓|✗|✓|✓|
|r6id.24xlarge|✓|✓|✓|✗|✓|✓|
|r6id.32xlarge|✓|✓|✓|✗|✓|✓|
|r6id.metal|✓|✓|✓|✗|✗|✗|
|R7a|||||||
|r7a.medium|✓|Instance store not supported|✓|✗|✓|✗|


Security specifications 265


-----

|Instance type|EBS encryptio n|Instance store encryptio n|Encryptio n in transit|AMD SEV-SNP|NitroTPM|Nitro Enclaves|
|---|---|---|---|---|---|---|
|r7a.large|✓|Instance store not supported|✓|✗|✓|✗|
|r7a.xlarge|✓|Instance store not supported|✓|✗|✓|✗|
|r7a.2xlarge|✓|Instance store not supported|✓|✗|✓|✗|
|r7a.4xlarge|✓|Instance store not supported|✓|✗|✓|✗|
|r7a.8xlarge|✓|Instance store not supported|✓|✗|✓|✗|
|r7a.12xlarge|✓|Instance store not supported|✓|✗|✓|✗|
|r7a.16xlarge|✓|Instance store not supported|✓|✗|✓|✗|
|r7a.24xlarge|✓|Instance store not supported|✓|✗|✓|✗|


Security specifications 266


-----

|Instance type|EBS encryptio n|Instance store encryptio n|Encryptio n in transit|AMD SEV-SNP|NitroTPM|Nitro Enclaves|
|---|---|---|---|---|---|---|
|r7a.32xlarge|✓|Instance store not supported|✓|✗|✓|✗|
|r7a.48xlarge|✓|Instance store not supported|✓|✗|✓|✗|
|r7a.metal-48xl|✓|Instance store not supported|✓|✗|✗|✗|
|R7g|||||||
|r7g.medium|✓|Instance store not supported|✓|✗|✗|✗|
|r7g.large|✓|Instance store not supported|✓|✗|✗|✗|
|r7g.xlarge|✓|Instance store not supported|✓|✗|✗|✗|
|r7g.2xlarge|✓|Instance store not supported|✓|✗|✗|✗|
|r7g.4xlarge|✓|Instance store not supported|✓|✗|✗|✗|


Security specifications 267


-----

|Instance type|EBS encryptio n|Instance store encryptio n|Encryptio n in transit|AMD SEV-SNP|NitroTPM|Nitro Enclaves|
|---|---|---|---|---|---|---|
|r7g.8xlarge|✓|Instance store not supported|✓|✗|✗|✗|
|r7g.12xlarge|✓|Instance store not supported|✓|✗|✗|✗|
|r7g.16xlarge|✓|Instance store not supported|✓|✗|✗|✗|
|r7g.metal|✓|Instance store not supported|✓|✗|✗|✗|
|R7gd|||||||
|r7gd.medium|✓|✓|✓|✗|✗|✗|
|r7gd.large|✓|✓|✓|✗|✗|✗|
|r7gd.xlarge|✓|✓|✓|✗|✗|✗|
|r7gd.2xlarge|✓|✓|✓|✗|✗|✗|
|r7gd.4xlarge|✓|✓|✓|✗|✗|✗|
|r7gd.8xlarge|✓|✓|✓|✗|✗|✗|
|r7gd.12xlarge|✓|✓|✓|✗|✗|✗|
|r7gd.16xlarge|✓|✓|✓|✗|✗|✗|
|r7gd.metal|✓|✓|✓|✗|✗|✗|


Security specifications 268


-----

|Instance type EBS encryptio n Instance store encryptio n Encryptio n in transit AMD SEV-SNP NitroTPM Nitro Enclaves|Col2|Col3|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
|R7i|||||||
|r7i.large|✓|Instance store not supported|✓|✗|✓|✗|
|r7i.xlarge|✓|Instance store not supported|✓|✗|✓|✗|
|r7i.2xlarge|✓|Instance store not supported|✓|✗|✓|✗|
|r7i.4xlarge|✓|Instance store not supported|✓|✗|✓|✗|
|r7i.8xlarge|✓|Instance store not supported|✓|✗|✓|✗|
|r7i.12xlarge|✓|Instance store not supported|✓|✗|✓|✗|
|r7i.16xlarge|✓|Instance store not supported|✓|✗|✓|✗|
|r7i.24xlarge|✓|Instance store not supported|✓|✗|✓|✗|


Security specifications 269


-----

|Instance type|EBS encryptio n|Instance store encryptio n|Encryptio n in transit|AMD SEV-SNP|NitroTPM|Nitro Enclaves|
|---|---|---|---|---|---|---|
|r7i.48xlarge|✓|Instance store not supported|✓|✗|✓|✗|
|r7i.metal-24xl|✓|Instance store not supported|✓|✗|✗|✗|
|r7i.metal-48xl|✓|Instance store not supported|✓|✗|✗|✗|
|R7iz|||||||
|r7iz.large|✓|Instance store not supported|✓|✗|✓|✗|
|r7iz.xlarge|✓|Instance store not supported|✓|✗|✓|✗|
|r7iz.2xlarge|✓|Instance store not supported|✓|✗|✓|✗|
|r7iz.4xlarge|✓|Instance store not supported|✓|✗|✓|✗|
|r7iz.8xlarge|✓|Instance store not supported|✓|✗|✓|✗|


Security specifications 270


-----

|Instance type|EBS encryptio n|Instance store encryptio n|Encryptio n in transit|AMD SEV-SNP|NitroTPM|Nitro Enclaves|
|---|---|---|---|---|---|---|
|r7iz.12xlarge|✓|Instance store not supported|✓|✗|✓|✗|
|r7iz.16xlarge|✓|Instance store not supported|✓|✗|✓|✗|
|r7iz.32xlarge|✓|Instance store not supported|✓|✗|✓|✗|
|r7iz.metal-16xl|✓|Instance store not supported|✓|✗|✗|✗|
|r7iz.metal-32xl|✓|Instance store not supported|✓|✗|✗|✗|
|R8g|||||||
|r8g.medium|✓|Instance store not supported|✓|✗|✗|✗|
|r8g.large|✓|Instance store not supported|✓|✗|✗|✓|
|r8g.xlarge|✓|Instance store not supported|✓|✗|✗|✓|


Security specifications 271


-----

|Instance type|EBS encryptio n|Instance store encryptio n|Encryptio n in transit|AMD SEV-SNP|NitroTPM|Nitro Enclaves|
|---|---|---|---|---|---|---|
|r8g.2xlarge|✓|Instance store not supported|✓|✗|✗|✓|
|r8g.4xlarge|✓|Instance store not supported|✓|✗|✗|✓|
|r8g.8xlarge|✓|Instance store not supported|✓|✗|✗|✓|
|r8g.12xlarge|✓|Instance store not supported|✓|✗|✗|✓|
|r8g.16xlarge|✓|Instance store not supported|✓|✗|✗|✓|
|r8g.24xlarge|✓|Instance store not supported|✓|✗|✗|✓|
|r8g.48xlarge|✓|Instance store not supported|✓|✗|✗|✓|
|r8g.metal-24xl|✓|Instance store not supported|✓|✗|✗|✗|


Security specifications 272


-----

|Instance type|EBS encryptio n|Instance store encryptio n|Encryptio n in transit|AMD SEV-SNP|NitroTPM|Nitro Enclaves|
|---|---|---|---|---|---|---|
|r8g.metal-48xl|✓|Instance store not supported|✓|✗|✗|✗|
|U-3tb1|||||||
|u-3tb1.56xlarge|✓|Instance store not supported|✓|✗|✗|✗|
|U-6tb1|||||||
|u-6tb1.56xlarge|✓|Instance store not supported|✓|✗|✗|✗|
|u-6tb1.112xlarge|✓|Instance store not supported|✓|✗|✗|✗|
|u-6tb1.metal|✓|Instance store not supported|✓|✗|✗|✗|
|U-9tb1|||||||
|u-9tb1.112xlarge|✓|Instance store not supported|✓|✗|✗|✗|
|u-9tb1.metal|✓|Instance store not supported|✓|✗|✗|✗|


Security specifications 273


-----

|Instance type EBS encryptio n Instance store encryptio n Encryptio n in transit AMD SEV-SNP NitroTPM Nitro Enclaves|Col2|Col3|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
|U-12tb1|||||||
|u-12tb1.112xlarge|✓|Instance store not supported|✓|✗|✗|✗|
|u-12tb1.metal|✓|Instance store not supported|✓|✗|✗|✗|
|U-18tb1|||||||
|u-18tb1.112xlarge|✓|Instance store not supported|✓|✗|✗|✗|
|u-18tb1.metal|✓|Instance store not supported|✓|✗|✗|✗|
|U-24tb1|||||||
|u-24tb1.112xlarge|✓|Instance store not supported|✓|✗|✗|✗|
|u-24tb1.metal|✓|Instance store not supported|✓|✗|✗|✗|
|U7i-12tb|||||||


Security specifications 274


-----

|Instance type|EBS encryptio n|Instance store encryptio n|Encryptio n in transit|AMD SEV-SNP|NitroTPM|Nitro Enclaves|
|---|---|---|---|---|---|---|
|u7i-12tb. 224xlarge|✓|Instance store not supported|✓|✗|✓|✓|
|U7in-16tb|||||||
|u7in-16tb .224xlarge|✓|Instance store not supported|✓|✗|✓|✓|
|U7in-24tb|||||||
|u7in-24tb .224xlarge|✓|Instance store not supported|✓|✗|✓|✓|
|U7in-32tb|||||||
|u7in-32tb .224xlarge|✓|Instance store not supported|✓|✗|✓|✓|
|X1|||||||
|x1.16xlarge|✓|✗|✗|✗|✗|✗|
|x1.32xlarge|✓|✗|✗|✗|✗|✗|
|X2gd|||||||
|x2gd.medium|✓|✓|✗|✗|✗|✗|
|x2gd.large|✓|✓|✗|✗|✗|✓|
|x2gd.xlarge|✓|✓|✗|✗|✗|✓|


Security specifications 275


-----

|Instance type|EBS encryptio n|Instance store encryptio n|Encryptio n in transit|AMD SEV-SNP|NitroTPM|Nitro Enclaves|
|---|---|---|---|---|---|---|
|x2gd.2xlarge|✓|✓|✗|✗|✗|✓|
|x2gd.4xlarge|✓|✓|✗|✗|✗|✓|
|x2gd.8xlarge|✓|✓|✗|✗|✗|✓|
|x2gd.12xlarge|✓|✓|✗|✗|✗|✓|
|x2gd.16xlarge|✓|✓|✗|✗|✗|✓|
|x2gd.metal|✓|✓|✗|✗|✗|✗|
|X2idn|||||||
|x2idn.16xlarge|✓|✓|✓|✗|✓|✓|
|x2idn.24xlarge|✓|✓|✓|✗|✓|✓|
|x2idn.32xlarge|✓|✓|✓|✗|✓|✓|
|x2idn.metal|✓|✓|✓|✗|✗|✗|
|X2iedn|||||||
|x2iedn.xlarge|✓|✓|✓|✗|✓|✓|
|x2iedn.2xlarge|✓|✓|✓|✗|✓|✓|
|x2iedn.4xlarge|✓|✓|✓|✗|✓|✓|
|x2iedn.8xlarge|✓|✓|✓|✗|✓|✓|
|x2iedn.16xlarge|✓|✓|✓|✗|✓|✓|
|x2iedn.24xlarge|✓|✓|✓|✗|✓|✓|
|x2iedn.32xlarge|✓|✓|✓|✗|✓|✓|


Security specifications 276


-----

|Instance type|EBS encryptio n|Instance store encryptio n|Encryptio n in transit|AMD SEV-SNP|NitroTPM|Nitro Enclaves|
|---|---|---|---|---|---|---|
|x2iedn.metal|✓|✓|✓|✗|✗|✗|
|X2iezn|||||||
|x2iezn.2xlarge|✓|Instance store not supported|✓|✗|✓|✓|
|x2iezn.4xlarge|✓|Instance store not supported|✓|✗|✓|✓|
|x2iezn.6xlarge|✓|Instance store not supported|✓|✗|✓|✓|
|x2iezn.8xlarge|✓|Instance store not supported|✓|✗|✓|✓|
|x2iezn.12xlarge|✓|Instance store not supported|✓|✗|✓|✓|
|x2iezn.metal|✓|Instance store not supported|✓|✗|✗|✗|
|X1e|||||||
|x1e.xlarge|✓|✗|✗|✗|✗|✗|
|x1e.2xlarge|✓|✗|✗|✗|✗|✗|


Security specifications 277


-----

|Instance type|EBS encryptio n|Instance store encryptio n|Encryptio n in transit|AMD SEV-SNP|NitroTPM|Nitro Enclaves|
|---|---|---|---|---|---|---|
|x1e.4xlarge|✓|✗|✗|✗|✗|✗|
|x1e.8xlarge|✓|✗|✗|✗|✗|✗|
|x1e.16xlarge|✓|✗|✗|✗|✗|✗|
|x1e.32xlarge|✓|✗|✗|✗|✗|✗|
|z1d|||||||
|z1d.large|✓|✓|✗|✗|✓|✗|
|z1d.xlarge|✓|✓|✗|✗|✓|✓|
|z1d.2xlarge|✓|✓|✗|✗|✓|✓|
|z1d.3xlarge|✓|✓|✗|✗|✓|✓|
|z1d.6xlarge|✓|✓|✗|✗|✓|✓|
|z1d.12xlarge|✓|✓|✗|✗|✓|✓|
|z1d.metal|✓|✓|✗|✗|✗|✗|


### Specifications for Amazon EC2 storage optimized instances

Storage optimized instances are designed for workloads that require high, sequential read
and write access to very large data sets on local storage. They are optimized to deliver tens of
thousands of low-latency, random I/O operations per second (IOPS) to applications.

For information on previous generation instance types of this category, such as I2 instances, see
Specifications for Amazon EC2 previous generation instances.

**Contents**

-  Available sizes

Storage optimized 278


-----

-  Platform summary

-  Performance specifications

-  Network specifications

-  Amazon EBS specifications

-  Instance store specifications

-  Security specifications

**Pricing**

[For pricing information, see Amazon EC2 On-Demand Pricing.](https://aws.amazon.com/ec2/pricing/on-demand/)

#### Available sizes

|Instance type|Available sizes|
|---|---|
|D2|d2.xlarge | d2.2xlarge | d2.4xlarge | d2.8xlarge|
|D3|d3.xlarge | d3.2xlarge | d3.4xlarge | d3.8xlarge|
|D3en|d3en.xlarge | d3en.2xlarge | d3en.4xlarge | d3en.6xlarge | d3en.8xlarge | d3en.12xlarge|
|H1|h1.2xlarge | h1.4xlarge | h1.8xlarge | h1.16xlarge|
|I3|i3.large | i3.xlarge | i3.2xlarge | i3.4xlarge | i3.8xlarge | i3.16xlarge | i3.metal|
|I3en|i3en.large | i3en.xlarge | i3en.2xlarge | i3en.3xlarge | i3en.6xlarge | i3en.12xlarge | i3en.24xlarge | i3en.metal|
|I4g|i4g.large | i4g.xlarge | i4g.2xlarge | i4g.4xlarge | i4g.8xlar ge | i4g.16xlarge|
|I4i|i4i.large | i4i.xlarge | i4i.2xlarge | i4i.4xlarge | i4i.8xlar ge | i4i.12xlarge | i4i.16xlarge | i4i.24xlarge | i4i.32xlarge | i4i.metal|



Available sizes 279


-----

|Instance type|Available sizes|
|---|---|
|Im4gn|im4gn.large | im4gn.xlarge | im4gn.2xlarge | im4gn.4xlarge | im4gn.8xlarge | im4gn.16xlarge|
|Is4gen|is4gen.medium | is4gen.large | is4gen.xlarge | is4gen.2xlarge | is4gen.4xlarge | is4gen.8xlarge|


#### Platform summary

|Instance type|Hypervi r|soP rocessor type (architec ture)|Metal instances available|Dedicate Hosts support|dS pot support|Hibernati on support|Support operatin systems|
|---|---|---|---|---|---|---|---|
|D2|Xen|Intel (x86_64)|✗|✓|✓|✗|Window | Linux|
|D3|Nitro v3|Intel (x86_64)|✗|✗|✓|✗|Window | Linux|
|D3en|Nitro v3|Intel (x86_64)|✗|✗|✓|✗|Window | Linux|
|H1|Xen|Intel (x86_64)|✗|✓|✓|✗|Window | Linux|
|I3|Xen *|Intel (x86_64)|✓|✓|✓|✓|Window | Linux|
|I3en|Nitro v3|Intel (x86_64)|✓|✓|✓|✓|Window | Linux|
|I4g|Nitro v4|AWS Graviton (arm64)|✗|✓|✓|✗|Linux|



Platform summary 280


-----

**Instance**

|type|r|type (architec ture)|instances available|Hosts support|support|on support|operatin systems|
|---|---|---|---|---|---|---|---|
|I4i|Nitro v4|Intel (x86_64)|✓|✓|✓|✗|Window | Linux|
|Im4gn|Nitro v4|AWS Graviton (arm64)|✗|✓|✓|✗|Linux|
|Is4gen|Nitro v4|AWS Graviton (arm64)|✗|✗|✓|✗|Linux|



**Note**


**Hyperviso Processor**
**r** **type**

**(architec**
**ture)**


**Metal**
**instances**
**available**


**Dedicated Spot**
**Hosts** **support**
**support**


**Hibernati**
**on support**


**Supported**
**operating**
**systems**

Windows
| Linux

Linux

Linux



-  i3.metal instances are built on the AWS Nitro System.

#### Performance specifications

|Instance type|Burstabl|eMemor (GiB)|y Processor|vCPUs|CPU cores|Thread per core|s Accelerat ors|Acceler or memor|
|---|---|---|---|---|---|---|---|---|
|D2|||||||||
|d2.xlarge|✗|30.50|Intel Xeon E52676v3|4|2|2|✗|✗|
|d2.2xlarge|✗|61.00|Intel Xeon E52676v3|8|4|2|✗|✗|
|d2.4xlarge|✗|122.00|Intel Xeon E52676v3|16|8|2|✗|✗|


Performance specifications 281


-----

**Instance**


**BurstableMemory**


**Processor** **vCPUs CPU**


**Threads Accelerat**


**Accelerat**

|type|Col2|(GiB)|Col4|Col5|cores|per core|ors|or memor|
|---|---|---|---|---|---|---|---|---|
|d2.8xlarge|✗|244.00|Intel Xeon E52676v3|36|18|2|✗|✗|
|D3|||||||||
|d3.xlarge|✗|32.00|Intel Xeon Platinum 8259|4|2|2|✗|✗|
|d3.2xlarge|✗|64.00|Intel Xeon Platinum 8259|8|4|2|✗|✗|
|d3.4xlarge|✗|128.00|Intel Xeon Platinum 8259|16|8|2|✗|✗|
|d3.8xlarge|✗|256.00|Intel Xeon Platinum 8259|32|16|2|✗|✗|
|D3en|||||||||
|d3en.xlarge|✗|16.00|Intel Xeon Platinum 8259|4|2|2|✗|✗|
|d3en.2xla rge|✗|32.00|Intel Xeon Platinum 8259|8|4|2|✗|✗|
|d3en.4xla rge|✗|64.00|Intel Xeon Platinum 8259|16|8|2|✗|✗|


Performance specifications 282


-----

**Instance**


**BurstableMemory**


**Processor** **vCPUs CPU**


**Threads Accelerat**


**Accelerat**

|type|Col2|(GiB)|Col4|Col5|cores|per core|ors|or memor|
|---|---|---|---|---|---|---|---|---|
|d3en.6xla rge|✗|96.00|Intel Xeon Platinum 8259|24|12|2|✗|✗|
|d3en.8xla rge|✗|128.00|Intel Xeon Platinum 8259|32|16|2|✗|✗|
|d3en.12xl arge|✗|192.00|Intel Xeon Platinum 8259|48|24|2|✗|✗|
|H1|||||||||
|h1.2xlarge|✗|32.00|Intel Broadwell E5-2686v4|8|4|2|✗|✗|
|h1.4xlarge|✗|64.00|Intel Broadwell E5-2686v4|16|8|2|✗|✗|
|h1.8xlarge|✗|128.00|Intel Broadwell E5-2686v4|32|16|2|✗|✗|
|h1.16xlarge|✗|256.00|Intel Broadwell E5-2686v4|64|32|2|✗|✗|
|I3|||||||||
|i3.large|✗|15.25|Intel Broadwell E5-2686v4|2|1|2|✗|✗|


Performance specifications 283


-----

**Instance**


**BurstableMemory**


**Processor** **vCPUs CPU**


**Threads Accelerat**


**Accelerat**

|type|Col2|(GiB)|Col4|Col5|cores|per core|ors|or memor|
|---|---|---|---|---|---|---|---|---|
|i3.xlarge|✗|30.50|Intel Broadwell E5-2686v4|4|2|2|✗|✗|
|i3.2xlarge|✗|61.00|Intel Broadwell E5-2686v4|8|4|2|✗|✗|
|i3.4xlarge|✗|122.00|Intel Broadwell E5-2686v4|16|8|2|✗|✗|
|i3.8xlarge|✗|244.00|Intel Broadwell E5-2686v4|32|16|2|✗|✗|
|i3.16xlarge|✗|488.00|Intel Broadwell E5-2686v4|64|32|2|✗|✗|
|i3.metal|✗|512.00|Intel Broadwell E5-2686v4|72|36|2|✗|✗|
|I3en|||||||||
|i3en.large|✗|16.00|Intel Xeon Platinum 8175|2|1|2|✗|✗|
|i3en.xlarge|✗|32.00|Intel Xeon Platinum 8175|4|2|2|✗|✗|


Performance specifications 284


-----

**Instance**


**BurstableMemory**


**Processor** **vCPUs CPU**


**Threads Accelerat**


**Accelerat**

|type|Col2|(GiB)|Col4|Col5|cores|per core|ors|or memor|
|---|---|---|---|---|---|---|---|---|
|i3en.2xlarge|✗|64.00|Intel Xeon Platinum 8175|8|4|2|✗|✗|
|i3en.3xlarge|✗|96.00|Intel Xeon Platinum 8175|12|6|2|✗|✗|
|i3en.6xlarge|✗|192.00|Intel Xeon Platinum 8175|24|12|2|✗|✗|
|i3en.12xl arge|✗|384.00|Intel Xeon Platinum 8175|48|24|2|✗|✗|
|i3en.24xl arge|✗|768.00|Intel Xeon Platinum 8175|96|48|2|✗|✗|
|i3en.metal|✗|768.00|Intel Xeon Platinum 8175|96|48|2|✗|✗|
|I4g|||||||||
|i4g.large|✗|16.00|AWS Graviton2 Processor|2|2|1|✗|✗|
|i4g.xlarge|✗|32.00|AWS Graviton2 Processor|4|4|1|✗|✗|


Performance specifications 285


-----

**Instance**


**BurstableMemory**


**Processor** **vCPUs CPU**


**Threads Accelerat**


**Accelerat**

|type|Col2|(GiB)|Col4|Col5|cores|per core|ors|or memor|
|---|---|---|---|---|---|---|---|---|
|i4g.2xlarge|✗|64.00|AWS Graviton2 Processor|8|8|1|✗|✗|
|i4g.4xlarge|✗|128.00|AWS Graviton2 Processor|16|16|1|✗|✗|
|i4g.8xlarge|✗|256.00|AWS Graviton2 Processor|32|32|1|✗|✗|
|i4g.16xlarge|✗|512.00|AWS Graviton2 Processor|64|64|1|✗|✗|
|I4i|||||||||
|i4i.large|✗|16.00|Intel Xeon Ice Lake|2|1|2|✗|✗|
|i4i.xlarge|✗|32.00|Intel Xeon Ice Lake|4|2|2|✗|✗|
|i4i.2xlarge|✗|64.00|Intel Xeon Ice Lake|8|4|2|✗|✗|
|i4i.4xlarge|✗|128.00|Intel Xeon Ice Lake|16|8|2|✗|✗|
|i4i.8xlarge|✗|256.00|Intel Xeon Ice Lake|32|16|2|✗|✗|
|i4i.12xlarge|✗|384.00|Intel Xeon Ice Lake|48|24|2|✗|✗|


Performance specifications 286


-----

**Instance**


**BurstableMemory**


**Processor** **vCPUs CPU**


**Threads Accelerat**


**Accelerat**

|type|Col2|(GiB)|Col4|Col5|cores|per core|ors|or memor|
|---|---|---|---|---|---|---|---|---|
|i4i.16xlarge|✗|512.00|Intel Xeon Ice Lake|64|32|2|✗|✗|
|i4i.24xlarge|✗|768.00|Intel Xeon Ice Lake|96|48|2|✗|✗|
|i4i.32xlarge|✗|1024.00|Intel Xeon Ice Lake|128|64|2|✗|✗|
|i4i.metal|✗|1024.00|Intel Xeon Ice Lake|128|64|2|✗|✗|
|Im4gn|||||||||
|im4gn.large|✗|8.00|AWS Graviton2 Processor|2|2|1|✗|✗|
|im4gn.xla rge|✗|16.00|AWS Graviton2 Processor|4|4|1|✗|✗|
|im4gn.2xl arge|✗|32.00|AWS Graviton2 Processor|8|8|1|✗|✗|
|im4gn.4xl arge|✗|64.00|AWS Graviton2 Processor|16|16|1|✗|✗|
|im4gn.8xl arge|✗|128.00|AWS Graviton2 Processor|32|32|1|✗|✗|


Performance specifications 287


-----

**Instance**


**BurstableMemory**


**Processor** **vCPUs CPU**


**Threads Accelerat**


**Accelerat**

|type|Col2|(GiB)|Col4|Col5|cores|per core|ors|or memor|
|---|---|---|---|---|---|---|---|---|
|im4gn.16x large|✗|256.00|AWS Graviton2 Processor|64|64|1|✗|✗|
|Is4gen|||||||||
|is4gen.me dium|✗|6.00|AWS Graviton2 Processor|1|1|1|✗|✗|
|is4gen.large|✗|12.00|AWS Graviton2 Processor|2|2|1|✗|✗|
|is4gen.xl arge|✗|24.00|AWS Graviton2 Processor|4|4|1|✗|✗|
|is4gen.2x large|✗|48.00|AWS Graviton2 Processor|8|8|1|✗|✗|
|is4gen.4x large|✗|96.00|AWS Graviton2 Processor|16|16|1|✗|✗|
|is4gen.8x large|✗|192.00|AWS Graviton2 Processor|32|32|1|✗|✗|


Performance specifications 288


-----

#### Network specifications

|Instance type|Baseline / Burst bandwidth (Gbps)|EFA|ENA|ENA Express|Network cards|Max. network interface s|IP addresses per interface|IPv6|
|---|---|---|---|---|---|---|---|---|
|D2|||||||||
|d2.xlarge|Moderate|✗|2 ✗|✗|1|4|15|✓|
|d2.2xlarge|High|✗|2 ✗|✗|1|4|15|✓|
|d2.4xlarge|High|✗|2 ✗|✗|1|8|30|✓|
|d2.8xlarge|10 Gigabit|✗|2 ✗|✗|1|8|30|✓|
|D3|||||||||
|1 d3.xlarge|3.0 / 15.0|✗|✓|✗|1|4|3|✓|
|1 d3.2xlarge|6.0 / 15.0|✗|✓|✗|1|4|5|✓|
|1 d3.4xlarge|12.5 / 15.0|✗|✓|✗|1|4|10|✓|
|d3.8xlarge|25 Gigabit|✗|✓|✗|1|3|20|✓|
|D3en|||||||||
|1 d3en.xlarge|6.0 / 25.0|✗|✓|✗|1|4|3|✓|
|1 d3en.2xlarge|12.5 / 25.0|✗|✓|✗|1|4|5|✓|
|d3en.4xlarge|25 Gigabit|✗|✓|✗|1|4|10|✓|
|d3en.6xlarge|40 Gigabit|✗|✓|✗|1|4|15|✓|
|d3en.8xlarge|50 Gigabit|✗|✓|✗|1|4|20|✓|
|d3en.12xlarge|75 Gigabit|✗|✓|✗|1|3|30|✓|



Network specifications 289


-----

|Instance type Baseline / Burst bandwidth (Gbps) EFA ENA ENA Express Network cards Max. network interface s IP addresses per interface IPv6|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
|H1|||||||||
|1 h1.2xlarge|2.5 / 10.0|✗|✓|✗|1|4|15|✓|
|1 h1.4xlarge|5.0 / 10.0|✗|✓|✗|1|8|30|✓|
|h1.8xlarge|10 Gigabit|✗|✓|✗|1|8|30|✓|
|h1.16xlarge|25 Gigabit|✗|✓|✗|1|8|50|✓|
|I3|||||||||
|1 i3.large|0.75 / 10.0|✗|✓|✗|1|3|10|✓|
|1 i3.xlarge|1.25 / 10.0|✗|✓|✗|1|4|15|✓|
|1 i3.2xlarge|2.5 / 10.0|✗|✓|✗|1|4|15|✓|
|1 i3.4xlarge|5.0 / 10.0|✗|✓|✗|1|8|30|✓|
|i3.8xlarge|10 Gigabit|✗|✓|✗|1|8|30|✓|
|i3.16xlarge|25 Gigabit|✗|✓|✗|1|15|50|✓|
|i3.metal|25 Gigabit|✗|✓|✗|1|15|50|✓|
|I3en|||||||||
|1 i3en.large|2.1 / 25.0|✗|✓|✗|1|3|10|✓|
|1 i3en.xlarge|4.2 / 25.0|✗|✓|✗|1|4|15|✓|
|1 i3en.2xlarge|8.4 / 25.0|✗|✓|✗|1|4|15|✓|
|1 i3en.3xlarge|12.5 / 25.0|✗|✓|✗|1|4|15|✓|
|i3en.6xlarge|25 Gigabit|✗|✓|✗|1|8|30|✓|


Network specifications 290


-----

|Col1|bandwidth (Gbps)|Col3|Col4|Col5|Col6|interface s|per interface|Col9|
|---|---|---|---|---|---|---|---|---|
|i3en.12xlarge|50 Gigabit|✓|✓|✗|1|8|30|✓|
|i3en.24xlarge|100 Gigabit|✓|✓|✗|1|15|50|✓|
|i3en.metal|100 Gigabit|✓|✓|✗|1|15|50|✓|
|I4g|||||||||
|1 i4g.large|0.781 / 10.0|✗|✓|✗|1|3|10|✓|
|1 i4g.xlarge|1.875 / 10.0|✗|✓|✗|1|4|15|✓|
|1 i4g.2xlarge|4.687 / 12.0|✗|✓|✗|1|4|15|✓|
|1 i4g.4xlarge|9.375 / 25.0|✗|✓|✓|1|8|30|✓|
|i4g.8xlarge|18.75 Gigabit|✗|✓|✓|1|8|30|✓|
|i4g.16xlarge|37.5 Gigabit|✓|✓|✓|1|15|50|✓|
|I4i|||||||||
|1 i4i.large|0.781 / 10.0|✗|✓|✗|1|3|10|✓|
|1 i4i.xlarge|1.875 / 10.0|✗|✓|✗|1|4|15|✓|
|1 i4i.2xlarge|4.687 / 12.0|✗|✓|✗|1|4|15|✓|
|1 i4i.4xlarge|9.375 / 25.0|✗|✓|✗|1|8|30|✓|
|i4i.8xlarge|18.75 Gigabit|✗|✓|✓|1|8|30|✓|
|i4i.12xlarge|28.12 Gigabit|✗|✓|✓|1|8|30|✓|
|i4i.16xlarge|37.5 Gigabit|✗|✓|✓|1|15|50|✓|
|i4i.24xlarge|56.25 Gigabit|✗|✓|✓|1|15|30|✓|


**Instance type** **Baseline /** **EFA** **ENA** **ENA** **Network** **Max.** **IP** **IPv6**
**Burst** **Express** **cards** **network** **addresses**
**bandwidth** **interface** **per**
**(Gbps)** **s** **interface**


Network specifications 291


-----

|Col1|bandwidth (Gbps)|Col3|Col4|Col5|Col6|interface s|per interface|Col9|
|---|---|---|---|---|---|---|---|---|
|i4i.32xlarge|75 Gigabit|✓|✓|✓|1|15|50|✓|
|i4i.metal|75 Gigabit|✓|✓|✓|1|15|50|✓|
|Im4gn|||||||||
|1 im4gn.large|3.125 / 25.0|✗|✓|✗|1|3|10|✓|
|1 im4gn.xlarge|6.25 / 25.0|✗|✓|✗|1|4|15|✓|
|im4gn.2xlarge 1|12.5 / 25.0|✗|✓|✗|1|4|15|✓|
|im4gn.4xlarge|25 Gigabit|✗|✓|✓|1|8|30|✓|
|im4gn.8xlarge|50 Gigabit|✗|✓|✓|1|8|30|✓|
|im4gn.16x large|100 Gigabit|✓|✓|✓|1|15|50|✓|
|Is4gen|||||||||
|is4gen.me 1 dium|1.562 / 25.0|✗|✓|✗|1|2|4|✓|
|1 is4gen.large|3.125 / 25.0|✗|✓|✗|1|3|10|✓|
|is4gen.xlarge 1|6.25 / 25.0|✗|✓|✗|1|4|15|✓|
|is4gen.2xlarge 1|12.5 / 25.0|✗|✓|✗|1|4|15|✓|
|is4gen.4xlarge|25 Gigabit|✗|✓|✗|1|8|30|✓|
|is4gen.8xlarge|50 Gigabit|✗|✓|✗|1|8|30|✓|


**Instance type** **Baseline /** **EFA** **ENA** **ENA** **Network** **Max.** **IP** **IPv6**
**Burst** **Express** **cards** **network** **addresses**
**bandwidth** **interface** **per**
**(Gbps)** **s** **interface**


Network specifications 292


-----

**Note**

1
These instances have a baseline bandwidth and can use a network I/O credit mechanism
to burst beyond their baseline bandwidth on a best effort basis. Other instances types
[can sustain their maximum performance indefinitely. For more information, see instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-network-bandwidth.html)
[network bandwidth.](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-network-bandwidth.html)
2
These instances support enhanced networking using the Intel 82599 VF interface.

#### Amazon EBS specifications

The following table indicates which instance types are Amazon EBS optimized by default and
which optionally support it. It also describes their EBS-optimized performance, including dedicated
bandwidth to Amazon EBS, the typical maximum aggregate throughput that can be achieved on

that dedicated connection with a streaming read workload and 128 KiB I/O size, and the maximum
IOPS the instance type can support when using a 16 KiB I/O size. Instance types not listed do not
support Amazon EBS optimization.

**Important**

An instance's EBS performance is bounded by the instance's performance limits, or
the aggregated performance of its attached volumes, whichever is smaller. To achieve
maximum EBS performance, an instance must have attached volumes that provide a
combined performance equal to or greater than the maximum instance performance. For

example, to achieve 80,000 IOPS for r6i.16xlarge, the instance must have at least 5
```
   gp3 volumes provisioned with 16,000 IOPS each (5 volumes x 16,000 IOPS = 80,000

```
IOPS).
We recommand that you choose an EBS–optimized instance type that provides more
dedicated Amazon EBS throughput than your application needs; otherwise, the connection
between Amazon EBS and Amazon EC2 can become a performance bottleneck.

Amazon EBS specifications 293


-----

|Instance type|Baseline / Maximum bandwidth (Mbps)|Baseline / Maximum throughput (MB/s, 128 KiB I/O)|Baseline / Maximum IOPS (16 KiB I/O)|NVMe|EBS optimization 2|
|---|---|---|---|---|---|
|D2||||||
|d2.xlarge|750.00|93.75|6000.00|✗|default|
|d2.2xlarge|1000.00|125.00|8000.00|✗|default|
|d2.4xlarge|2000.00|250.00|16000.00|✗|default|
|d2.8xlarge|4000.00|500.00|32000.00|✗|default|
|D3||||||
|1 d3.xlarge|850.00 / 2800.00|106.25 / 350.00|5000.00 / 15000.00|✓|default|
|1 d3.2xlarge|1700.00 / 2800.00|212.50 / 350.00|10000.00 / 15000.00|✓|default|
|d3.4xlarge|2800.00|350.00|15000.00|✓|default|
|d3.8xlarge|5000.00|625.00|30000.00|✓|default|
|D3en||||||
|1 d3en.xlarge|850.00 / 2800.00|106.25 / 350.00|5000.00 / 15000.00|✓|default|
|d3en.2xlarge 1|1700.00 / 2800.00|212.50 / 350.00|10000.00 / 15000.00|✓|default|
|d3en.4xlarge|2800.00|350.00|15000.00|✓|default|
|d3en.6xlarge|4000.00|500.00|25000.00|✓|default|


Amazon EBS specifications 294


-----

**Instance**


**Baseline /**


**Baseline /**


**Baseline /**


**NVMe** **EBS**

|type|Maximum bandwidth (Mbps)|Maximum throughput (MB/s, 128 KiB I/O)|Maximum IOPS (16 KiB I/O)|Col5|optimization 2|
|---|---|---|---|---|---|
|d3en.8xlarge|5000.00|625.00|30000.00|✓|default|
|d3en.12xl arge|7000.00|875.00|40000.00|✓|default|
|H1||||||
|h1.2xlarge|1750.00|218.75|12000.00|✗|default|
|h1.4xlarge|3500.00|437.50|20000.00|✗|default|
|h1.8xlarge|7000.00|875.00|40000.00|✗|default|
|h1.16xlarge|14000.00|1750.00|80000.00|✗|default|
|I3||||||
|i3.large|425.00|53.12|3000.00|✗|default|
|i3.xlarge|850.00|106.25|6000.00|✗|default|
|i3.2xlarge|1700.00|212.50|12000.00|✗|default|
|i3.4xlarge|3500.00|437.50|16000.00|✗|default|
|i3.8xlarge|7000.00|875.00|32500.00|✗|default|
|i3.16xlarge|14000.00|1750.00|65000.00|✗|default|
|i3.metal|19000.00|2375.00|80000.00|✓|default|
|I3en||||||
|1 i3en.large|576.00 / 4750.00|72.10 / 593.75|3000.00 / 20000.00|✓|default|


Amazon EBS specifications 295


-----

**Instance**


**Baseline /**


**Baseline /**


**Baseline /**


**NVMe** **EBS**

|type|Maximum bandwidth (Mbps)|Maximum throughput (MB/s, 128 KiB I/O)|Maximum IOPS (16 KiB I/O)|Col5|optimization 2|
|---|---|---|---|---|---|
|1 i3en.xlarge|1153.00 / 4750.00|144.20 / 593.75|6000.00 / 20000.00|✓|default|
|i3en.2xlarge 1|2307.00 / 4750.00|288.39 / 593.75|12000.00 / 20000.00|✓|default|
|i3en.3xlarge 1|3800.00 / 4750.00|475.00 / 593.75|15000.00 / 20000.00|✓|default|
|i3en.6xlarge|4750.00|593.75|20000.00|✓|default|
|i3en.12xlarge|9500.00|1187.50|40000.00|✓|default|
|i3en.24xlarge|19000.00|2375.00|80000.00|✓|default|
|i3en.metal|19000.00|2375.00|80000.00|✓|default|
|I4g||||||
|1 i4g.large|625.00 / 10000.00|78.12 / 1250.00|2500.00 / 40000.00|✓|default|
|1 i4g.xlarge|1250.00 / 10000.00|156.25 / 1250.00|5000.00 / 40000.00|✓|default|
|1 i4g.2xlarge|2500.00 / 10000.00|312.50 / 1250.00|10000.00 / 40000.00|✓|default|
|1 i4g.4xlarge|5000.00 / 10000.00|625.00 / 1250.00|20000.00 / 40000.00|✓|default|
|i4g.8xlarge|10000.00|1250.00|40000.00|✓|default|
|i4g.16xlarge|20000.00|2500.00|80000.00|✓|default|


Amazon EBS specifications 296


-----

**Instance**


**Baseline /**


**Baseline /**


**Baseline /**


**NVMe** **EBS**

|type Maximum bandwidth (Mbps) Maximum throughput (MB/s, 128 KiB I/O) Maximum IOPS (16 KiB I/O) optimization 2|Col2|Col3|Col4|Col5|Col6|
|---|---|---|---|---|---|
|I4i||||||
|1 i4i.large|625.00 / 10000.00|78.12 / 1250.00|2500.00 / 40000.00|✓|default|
|1 i4i.xlarge|1250.00 / 10000.00|156.25 / 1250.00|5000.00 / 40000.00|✓|default|
|1 i4i.2xlarge|2500.00 / 10000.00|312.50 / 1250.00|10000.00 / 40000.00|✓|default|
|1 i4i.4xlarge|5000.00 / 10000.00|625.00 / 1250.00|20000.00 / 40000.00|✓|default|
|i4i.8xlarge|10000.00|1250.00|40000.00|✓|default|
|i4i.12xlarge|15000.00|1875.00|60000.00|✓|default|
|i4i.16xlarge|20000.00|2500.00|80000.00|✓|default|
|i4i.24xlarge|30000.00|3750.00|120000.00|✓|default|
|i4i.32xlarge|40000.00|5000.00|160000.00|✓|default|
|i4i.metal|40000.00|5000.00|160000.00|✓|default|
|Im4gn||||||
|1 im4gn.large|1250.00 / 10000.00|156.25 / 1250.00|5000.00 / 40000.00|✓|default|
|im4gn.xlarge 1|2500.00 / 10000.00|312.50 / 1250.00|10000.00 / 40000.00|✓|default|


Amazon EBS specifications 297


-----

**Instance**


**Baseline /**


**Baseline /**


**Baseline /**


**NVMe** **EBS**

|type|Maximum bandwidth (Mbps)|Maximum throughput (MB/s, 128 KiB I/O)|Maximum IOPS (16 KiB I/O)|Col5|optimization 2|
|---|---|---|---|---|---|
|im4gn.2xl 1 arge|5000.00 / 10000.00|625.00 / 1250.00|20000.00 / 40000.00|✓|default|
|im4gn.4xl arge|10000.00|1250.00|40000.00|✓|default|
|im4gn.8xl arge|20000.00|2500.00|80000.00|✓|default|
|im4gn.16x large|40000.00|5000.00|160000.00|✓|default|
|Is4gen||||||
|is4gen.me 1 dium|625.00 / 10000.00|78.12 / 1250.00|2500.00 / 40000.00|✓|default|
|1 is4gen.large|1250.00 / 10000.00|156.25 / 1250.00|5000.00 / 40000.00|✓|default|
|is4gen.xlarge 1|2500.00 / 10000.00|312.50 / 1250.00|10000.00 / 40000.00|✓|default|
|is4gen.2x 1 large|5000.00 / 10000.00|625.00 / 1250.00|20000.00 / 40000.00|✓|default|
|is4gen.4x large|10000.00|1250.00|40000.00|✓|default|
|is4gen.8x large|20000.00|2500.00|80000.00|✓|default|


Amazon EBS specifications 298


-----

**Note**

1
These instances can support maximum performance for 30 minutes at least once every 24
hours, after which they revert to their baseline performance. Other instances can sustain
the maximum performance indefinitely. If your workload requires sustained maximum
performance for longer than 30 minutes, use one of these instances.
2
```
   default indicates that instances are enabled for EBS optimization by default.
   supported indicates that instances can optionally be enabled for EBS optimization For

```
[more information, see Amazon EBS–optimized instances.](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-optimized.html)

#### Instance store specifications

The following table shows the instance store volume configuration for supported instance types,
along with the aggregated IOPS performance with 4,096 byte block size at queue depth saturation.

|Instance type|Instance store volumes|Instance store type|100% random read IOPS / Write IOPS|Needs initializ 1 ation|TRIM support 2|
|---|---|---|---|---|---|
|D2||||||
|d2.xlarge|3 x 2048 GB|HDD||✓||
|d2.2xlarge|6 x 2048 GB|HDD||✓||
|d2.4xlarge|12 x 2048 GB|HDD||✓||
|d2.8xlarge|24 x 2048 GB|HDD||✓||
|D3||||||
|d3.xlarge|3 x 1980 GB|NVMe HDD|||✓|
|d3.2xlarge|6 x 1980 GB|NVMe HDD|||✓|



Instance store specifications 299


-----

|Instance type|Instance store volumes|Instance store type|100% random read IOPS / Write IOPS|Needs initializ ation 1|TRIM support 2|
|---|---|---|---|---|---|
|d3.4xlarge|12 x 1980 GB|NVMe HDD|||✓|
|d3.8xlarge|24 x 1980 GB|NVMe HDD|||✓|
|D3en||||||
|d3en.xlarge|2 x 13980 GB|NVMe HDD|||✓|
|d3en.2xlarge|4 x 13980 GB|NVMe HDD|||✓|
|d3en.4xlarge|8 x 13980 GB|NVMe HDD|||✓|
|d3en.6xlarge|12 x 13980 GB|NVMe HDD|||✓|
|d3en.8xlarge|16 x 13980 GB|NVMe HDD|||✓|
|d3en.12xlarge|24 x 13980 GB|NVMe HDD|||✓|
|H1||||||
|h1.2xlarge|1 x 2000 GB|HDD||✓||
|h1.4xlarge|2 x 2000 GB|HDD||✓||
|h1.8xlarge|4 x 2000 GB|HDD||✓||
|h1.16xlarge|8 x 2000 GB|HDD||✓||


Instance store specifications 300


-----

|Instance type Instance store volumes Instance store type 100% random read IOPS / Write IOPS Needs initializ ation 1 TRIM support 2|Col2|Col3|Col4|Col5|Col6|
|---|---|---|---|---|---|
|I3||||||
|i3.large|1 x 475 GB|NVMe SSD|103,125 / 35,000||✓|
|i3.xlarge|1 x 950 GB|NVMe SSD|206,250 / 70,000||✓|
|i3.2xlarge|1 x 1900 GB|NVMe SSD|412,500 / 180,000||✓|
|i3.4xlarge|2 x 1900 GB|NVMe SSD|825,000 / 360,000||✓|
|i3.8xlarge|4 x 1900 GB|NVMe SSD|1,650,000 / 720,000||✓|
|i3.16xlarge|8 x 1900 GB|NVMe SSD|3,300,000 / 1,440,000||✓|
|i3.metal|8 x 1900 GB|NVMe SSD|3,300,000 / 1,440,000||✓|
|I3en||||||
|i3en.large|1 x 1250 GB|NVMe SSD|42,500 / 32,500||✓|
|i3en.xlarge|1 x 2500 GB|NVMe SSD|85,000 / 65,000||✓|
|i3en.2xlarge|2 x 2500 GB|NVMe SSD|170,000 / 130,000||✓|
|i3en.3xlarge|1 x 7500 GB|NVMe SSD|250,000 / 200,000||✓|


Instance store specifications 301


-----

|Instance type|Instance store volumes|Instance store type|100% random read IOPS / Write IOPS|Needs initializ ation 1|TRIM support 2|
|---|---|---|---|---|---|
|i3en.6xlarge|2 x 7500 GB|NVMe SSD|500,000 / 400,000||✓|
|i3en.12xlarge|4 x 7500 GB|NVMe SSD|1,000,000 / 800,000||✓|
|i3en.24xlarge|8 x 7500 GB|NVMe SSD|2,000,000 / 1,600,000||✓|
|i3en.metal|8 x 7500 GB|NVMe SSD|2,000,000 / 1,600,000||✓|
|I4g||||||
|i4g.large|1 x 468 GB|NVMe SSD|31,250 / 25,000||✓|
|i4g.xlarge|1 x 937 GB|NVMe SSD|62,500 / 50,000||✓|
|i4g.2xlarge|1 x 1875 GB|NVMe SSD|125,000 / 100,000||✓|
|i4g.4xlarge|1 x 3750 GB|NVMe SSD|250,000 / 200,000||✓|
|i4g.8xlarge|2 x 3750 GB|NVMe SSD|500,000 / 400,000||✓|
|i4g.16xlarge|4 x 3750 GB|NVMe SSD|1,000,000 / 800,000||✓|
|I4i||||||
|i4i.large|1 x 468 GB|NVMe SSD|50,000 / 27,500||✓|


Instance store specifications 302


-----

|Instance type|Instance store volumes|Instance store type|100% random read IOPS / Write IOPS|Needs initializ ation 1|TRIM support 2|
|---|---|---|---|---|---|
|i4i.xlarge|1 x 937 GB|NVMe SSD|100,000 / 55,000||✓|
|i4i.2xlarge|1 x 1875 GB|NVMe SSD|200,000 / 110,000||✓|
|i4i.4xlarge|1 x 3750 GB|NVMe SSD|400,000 / 220,000||✓|
|i4i.8xlarge|2 x 3750 GB|NVMe SSD|800,000 / 440,000||✓|
|i4i.12xlarge|3 x 3750 GB|NVMe SSD|1,200,000 / 660,000||✓|
|i4i.16xlarge|4 x 3750 GB|NVMe SSD|1,600,000 / 880,000||✓|
|i4i.24xlarge|6 x 3750 GB|NVMe SSD|2,400,000 / 1,320,000||✓|
|i4i.32xlarge|8 x 3750 GB|NVMe SSD|3,200,000 / 1,760,000||✓|
|i4i.metal|8 x 3750 GB|NVMe SSD|3,200,000 / 1,760,000||✓|
|Im4gn||||||
|im4gn.large|1 x 937 GB|NVMe SSD|31,250 / 25,000||✓|
|im4gn.xlarge|1 x 1875 GB|NVMe SSD|62,500 / 50,000||✓|


Instance store specifications 303


-----

|Instance type|Instance store volumes|Instance store type|100% random read IOPS / Write IOPS|Needs initializ ation 1|TRIM support 2|
|---|---|---|---|---|---|
|im4gn.2xlarge|1 x 3750 GB|NVMe SSD|125,000 / 100,000||✓|
|im4gn.4xlarge|1 x 7500 GB|NVMe SSD|250,000 / 200,000||✓|
|im4gn.8xlarge|2 x 7500 GB|NVMe SSD|500,000 / 400,000||✓|
|im4gn.16xlarge|4 x 7500 GB|NVMe SSD|1,000,000 / 800,000||✓|
|Is4gen||||||
|is4gen.medium|1 x 937 GB|NVMe SSD|31,250 / 25,000||✓|
|is4gen.large|1 x 1875 GB|NVMe SSD|62,500 / 50,000||✓|
|is4gen.xlarge|1 x 3750 GB|NVMe SSD|125,000 / 100,000||✓|
|is4gen.2xlarge|1 x 7500 GB|NVMe SSD|250,000 / 200,000||✓|
|is4gen.4xlarge|2 x 7500 GB|NVMe SSD|500,000 / 400,000||✓|
|is4gen.8xlarge|4 x 7500 GB|NVMe SSD|1,000,000 / 800,000||✓|


1
Volumes attached to certain instances suffer a first-write penalty unless initialized. For more
[information, see Optimize disk performance for instance store volumes.](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/disk-performance.html)

Instance store specifications 304


-----

2
[For more information, see Instance store volume TRIM support.](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ssd-instance-store.html#InstanceStoreTrimSupport)

#### Security specifications

|Instance type|EBS encryptio n|Instance store encryptio n|Encryptio n in transit|AMD SEV-SNP|NitroTPM|Nitro Enclaves|
|---|---|---|---|---|---|---|
|D2|||||||
|d2.xlarge|✓|✗|✗|✗|✗|✗|
|d2.2xlarge|✓|✗|✗|✗|✗|✗|
|d2.4xlarge|✓|✗|✗|✗|✗|✗|
|d2.8xlarge|✓|✗|✗|✗|✗|✗|
|D3|||||||
|d3.xlarge|✓|✓|✓|✗|✓|✓|
|d3.2xlarge|✓|✓|✓|✗|✓|✓|
|d3.4xlarge|✓|✓|✓|✗|✓|✓|
|d3.8xlarge|✓|✓|✓|✗|✓|✓|
|D3en|||||||
|d3en.xlarge|✓|✓|✓|✗|✓|✓|
|d3en.2xlarge|✓|✓|✓|✗|✓|✓|
|d3en.4xlarge|✓|✓|✓|✗|✓|✓|
|d3en.6xlarge|✓|✓|✓|✗|✓|✓|
|d3en.8xlarge|✓|✓|✓|✗|✓|✓|



Security specifications 305


-----

|Instance type|EBS encryptio n|Instance store encryptio n|Encryptio n in transit|AMD SEV-SNP|NitroTPM|Nitro Enclaves|
|---|---|---|---|---|---|---|
|d3en.12xlarge|✓|✓|✓|✗|✓|✓|
|H1|||||||
|h1.2xlarge|✓|✓|✗|✗|✗|✗|
|h1.4xlarge|✓|✓|✗|✗|✗|✗|
|h1.8xlarge|✓|✓|✗|✗|✗|✗|
|h1.16xlarge|✓|✓|✗|✗|✗|✗|
|I3|||||||
|i3.large|✓|✓|✗|✗|✗|✗|
|i3.xlarge|✓|✓|✗|✗|✗|✗|
|i3.2xlarge|✓|✓|✗|✗|✗|✗|
|i3.4xlarge|✓|✓|✗|✗|✗|✗|
|i3.8xlarge|✓|✓|✗|✗|✗|✗|
|i3.16xlarge|✓|✓|✗|✗|✗|✗|
|i3.metal|✓|✓|✗|✗|✗|✗|
|I3en|||||||
|i3en.large|✓|✓|✓|✗|✓|✗|
|i3en.xlarge|✓|✓|✓|✗|✓|✓|
|i3en.2xlarge|✓|✓|✓|✗|✓|✓|
|i3en.3xlarge|✓|✓|✓|✗|✓|✓|


Security specifications 306


-----

|Instance type|EBS encryptio n|Instance store encryptio n|Encryptio n in transit|AMD SEV-SNP|NitroTPM|Nitro Enclaves|
|---|---|---|---|---|---|---|
|i3en.6xlarge|✓|✓|✓|✗|✓|✓|
|i3en.12xlarge|✓|✓|✓|✗|✓|✓|
|i3en.24xlarge|✓|✓|✓|✗|✓|✓|
|i3en.metal|✓|✓|✓|✗|✗|✗|
|I4g|||||||
|i4g.large|✓|✓|✓|✗|✗|✓|
|i4g.xlarge|✓|✓|✓|✗|✗|✓|
|i4g.2xlarge|✓|✓|✓|✗|✗|✓|
|i4g.4xlarge|✓|✓|✓|✗|✗|✓|
|i4g.8xlarge|✓|✓|✓|✗|✗|✓|
|i4g.16xlarge|✓|✓|✓|✗|✗|✓|
|I4i|||||||
|i4i.large|✓|✓|✓|✗|✓|✗|
|i4i.xlarge|✓|✓|✓|✗|✓|✓|
|i4i.2xlarge|✓|✓|✓|✗|✓|✓|
|i4i.4xlarge|✓|✓|✓|✗|✓|✓|
|i4i.8xlarge|✓|✓|✓|✗|✓|✓|
|i4i.12xlarge|✓|✓|✓|✗|✓|✓|
|i4i.16xlarge|✓|✓|✓|✗|✓|✓|


Security specifications 307


-----

|Instance type|EBS encryptio n|Instance store encryptio n|Encryptio n in transit|AMD SEV-SNP|NitroTPM|Nitro Enclaves|
|---|---|---|---|---|---|---|
|i4i.24xlarge|✓|✓|✓|✗|✓|✓|
|i4i.32xlarge|✓|✓|✓|✗|✓|✓|
|i4i.metal|✓|✓|✓|✗|✗|✗|
|Im4gn|||||||
|im4gn.large|✓|✓|✓|✗|✗|✗|
|im4gn.xlarge|✓|✓|✓|✗|✗|✗|
|im4gn.2xlarge|✓|✓|✓|✗|✗|✗|
|im4gn.4xlarge|✓|✓|✓|✗|✗|✗|
|im4gn.8xlarge|✓|✓|✓|✗|✗|✗|
|im4gn.16xlarge|✓|✓|✓|✗|✗|✗|
|Is4gen|||||||
|is4gen.medium|✓|✓|✓|✗|✗|✗|
|is4gen.large|✓|✓|✓|✗|✗|✗|
|is4gen.xlarge|✓|✓|✓|✗|✗|✗|
|is4gen.2xlarge|✓|✓|✓|✗|✗|✗|
|is4gen.4xlarge|✓|✓|✓|✗|✗|✗|
|is4gen.8xlarge|✓|✓|✓|✗|✗|✗|


Security specifications 308


-----

### Specifications for Amazon EC2 accelerated computing instances

Accelerated computing instances use hardware accelerators, or co-processors, to perform
functions, such as floating point number calculations, graphics processing, or data pattern
matching, more efficiently than is possible in software running on CPUs.

For information on previous generation instance types of this category, such as G3 instances, see
Specifications for Amazon EC2 previous generation instances.

**Contents**

-  Available sizes

-  Platform summary

-  Performance specifications

-  Network specifications

-  Amazon EBS specifications

-  Instance store specifications

-  Security specifications

**Pricing**

[For pricing information, see Amazon EC2 On-Demand Pricing.](https://aws.amazon.com/ec2/pricing/on-demand/)

#### Available sizes

|Instance type|Available sizes|
|---|---|
|DL1|dl1.24xlarge|
|DL2q|dl2q.24xlarge|
|F1|f1.2xlarge | f1.4xlarge | f1.16xlarge|
|G4ad|g4ad.xlarge | g4ad.2xlarge | g4ad.4xlarge | g4ad.8xlarge | g4ad.16xlarge|



Accelerated computing 309


-----

|Instance type|Available sizes|
|---|---|
|G4dn|g4dn.xlarge | g4dn.2xlarge | g4dn.4xlarge | g4dn.8xlarge | g4dn.12xlarge | g4dn.16xlarge | g4dn.metal|
|G5|g5.xlarge | g5.2xlarge | g5.4xlarge | g5.8xlarge | g5.12xlarge | g5.16xlarge | g5.24xlarge | g5.48xlarge|
|G5g|g5g.xlarge | g5g.2xlarge | g5g.4xlarge | g5g.8xlarge | g5g.16xla rge | g5g.metal|
|G6|g6.xlarge | g6.2xlarge | g6.4xlarge | g6.8xlarge | g6.12xlarge | g6.16xlarge | g6.24xlarge | g6.48xlarge|
|Gr6|gr6.4xlarge | gr6.8xlarge|
|Inf1|inf1.xlarge | inf1.2xlarge | inf1.6xlarge | inf1.24xlarge|
|Inf2|inf2.xlarge | inf2.8xlarge | inf2.24xlarge | inf2.48xlarge|
|P2|p2.xlarge | p2.8xlarge | p2.16xlarge|
|P3|p3.2xlarge | p3.8xlarge | p3.16xlarge|
|P3dn|p3dn.24xlarge|
|P4d|p4d.24xlarge|
|P4de|p4de.24xlarge|
|P5|p5.48xlarge|
|Trn1|trn1.2xlarge | trn1.32xlarge|
|Trn1n|trn1n.32xlarge|
|VT1|vt1.3xlarge | vt1.6xlarge | vt1.24xlarge|


Available sizes 310


-----

#### Platform summary

|Instance type|Hypervi r|soP rocessor type (architec ture)|Metal instances available|Dedicate Hosts support|dS pot support|Hibernati on support|Support operatin systems|
|---|---|---|---|---|---|---|---|
|DL1|Nitro v3|Intel (x86_64)|✗|✓|✓|✗|Linux|
|DL2q|Nitro v3|Intel (x86_64)|✗|✓|✓|✗|Linux|
|F1|Xen|Intel (x86_64)|✗|✓|✓|✗|Linux|
|G4ad|Nitro v3|AMD (x86_64)|✗|✓|✓|✗|Window | Linux|
|G4dn|Nitro v3|Intel (x86_64)|✓|✓|✓|✗|Window | Linux|
|G5|Nitro v3|AMD (x86_64)|✗|✓|✓|✗|Window | Linux|
|G5g|Nitro v2|AWS Graviton (arm64)|✓|✓|✓|✗|Linux|
|G6|Nitro v4|AMD (x86_64)|✗|✓|✓|✗|Window | Linux|
|Gr6|Nitro v4|AMD (x86_64)|✗|✗|✓|✗|Window | Linux|
|Inf1|Nitro v3|Intel (x86_64)|✗|✓|✓|✗|Linux|



Platform summary 311


-----

**Instance**


**Hyperviso Processor**


**Metal**


**Dedicated Spot**


**Hibernati**


**Supported**

|type|r|type (architec ture)|instances available|Hosts support|support|on support|operatin systems|
|---|---|---|---|---|---|---|---|
|Inf2|Nitro v4|AMD (x86_64)|✗|✓|✓|✗|Linux|
|P2|Xen|Intel (x86_64)|✗|✓|✓|✗|Window | Linux|
|P3|Xen|Intel (x86_64)|✗|✓|✓|✗|Window | Linux|
|P3dn|Nitro v3|Intel (x86_64)|✗|✓|✓|✗|Window | Linux|
|P4d|Nitro v3|Intel (x86_64)|✗|✓|✓|✗|Linux|
|P4de|Nitro v3|Intel (x86_64)|✗|✓|✓|✗|Linux|
|P5|Nitro v4|AMD (x86_64)|✗|✗|✓|✗|Linux|
|Trn1|Nitro v4|Intel (x86_64)|✗|✓|✓|✗|Linux|
|Trn1n|Nitro v4|Intel (x86_64)|✗|✗|✓|✗|Linux|
|VT1|Nitro v3|Intel (x86_64)|✗|✓|✓|✗|Linux|


Platform summary 312


-----

#### Performance specifications

|Instance type|Burstabl|eMemor (GiB)|y Processor|vCPUs|CPU cores|Thread per core|s Accelerat ors|Acceler or memor|
|---|---|---|---|---|---|---|---|---|
|DL1|||||||||
|dl1.24xlarge|✗|768.00|Intel Xeon P-8275CL|96|48|2|8 x Habana Gaudi HL-205 GPU|256 GiB (8 x 32 GiB)|
|DL2q|||||||||
|dl2q.24xl arge|✗|768.00|Intel Xeon Cascade Lake|96|48|2|8 x Qualcomm Qualcomm AI100 inference accelerator|125 GiB (8 x 15 GiB)|
|F1|||||||||
|f1.2xlarge|✗|122.00|Intel Xeon E5-2686v4|8|4|2|1 x Xilinx Virtex UltraScal e (VU9P) FPGA|64 GiB (1 x 64 GiB)|
|f1.4xlarge|✗|244.00|Intel Xeon E5-2686v4|16|8|2|2 x Xilinx Virtex UltraScal e (VU9P) FPGA|128 GiB (2 x 64 GiB)|



Performance specifications 313


-----

**Instance**


**BurstableMemory**


**Processor** **vCPUs CPU**


**Threads Accelerat**


**Accelerat**

|type|Col2|(GiB)|Col4|Col5|cores|per core|ors|or memor|
|---|---|---|---|---|---|---|---|---|
|f1.16xlarge|✗|976.00|Intel Xeon E5-2686v4|64|32|2|8 x Xilinx Virtex UltraScal e (VU9P) FPGA|512 GiB (8 x 64 GiB)|
|G4ad|||||||||
|g4ad.xlarge|✗|16.00|2nd Gen AMD EPYC 7R32|4|2|2|1 x AMD Radeon Pro V520 GPU|8 GiB (1 x 8 GiB)|
|g4ad.2xla rge|✗|32.00|2nd Gen AMD EPYC 7R32|8|4|2|1 x AMD Radeon Pro V520 GPU|8 GiB (1 x 8 GiB)|
|g4ad.4xla rge|✗|64.00|2nd Gen AMD EPYC 7R32|16|8|2|1 x AMD Radeon Pro V520 GPU|8 GiB (1 x 8 GiB)|
|g4ad.8xla rge|✗|128.00|2nd Gen AMD EPYC 7R32|32|16|2|2 x AMD Radeon Pro V520 GPU|16 GiB (2 x 8 GiB)|
|g4ad.16xl arge|✗|256.00|2nd Gen AMD EPYC 7R32|64|32|2|4 x AMD Radeon Pro V520 GPU|32 GiB (4 x 8 GiB)|
|G4dn|||||||||


Performance specifications 314


-----

**Instance**


**BurstableMemory**


**Processor** **vCPUs CPU**


**Threads Accelerat**


**Accelerat**

|type|Col2|(GiB)|Col4|Col5|cores|per core|ors|or memor|
|---|---|---|---|---|---|---|---|---|
|g4dn.xlarge|✗|16.00|Intel Xeon P-8259L|4|2|2|1 x NVIDIA T4 GPU|16 GiB (1 x 16 GiB)|
|g4dn.2xla rge|✗|32.00|Intel Xeon P-8259L|8|4|2|1 x NVIDIA T4 GPU|16 GiB (1 x 16 GiB)|
|g4dn.4xla rge|✗|64.00|Intel Xeon P-8259L|16|8|2|1 x NVIDIA T4 GPU|16 GiB (1 x 16 GiB)|
|g4dn.8xla rge|✗|128.00|Intel Xeon P-8259L|32|16|2|1 x NVIDIA T4 GPU|16 GiB (1 x 16 GiB)|
|g4dn.12xl arge|✗|192.00|Intel Xeon P-8259L|48|24|2|4 x NVIDIA T4 GPU|64 GiB (4 x 16 GiB)|


Performance specifications 315


-----

**Instance**


**BurstableMemory**


**Processor** **vCPUs CPU**


**Threads Accelerat**


**Accelerat**

|type|Col2|(GiB)|Col4|Col5|cores|per core|ors|or memor|
|---|---|---|---|---|---|---|---|---|
|g4dn.16xl arge|✗|256.00|Intel Xeon P-8259L|64|32|2|1 x NVIDIA T4 GPU|16 GiB (1 x 16 GiB)|
|g4dn.metal|✗|384.00|Intel Xeon P-8259L|96|48|2|8 x NVIDIA T4 GPU|128 GiB (8 x 16 GiB)|
|G5|||||||||
|g5.xlarge|✗|16.00|2nd Gen AMD EPYC 7R32|4|2|2|1 x NVIDIA A10G GPU|24 GiB (1 x 24 GiB)|
|g5.2xlarge|✗|32.00|2nd Gen AMD EPYC 7R32|8|4|2|1 x NVIDIA A10G GPU|24 GiB (1 x 24 GiB)|
|g5.4xlarge|✗|64.00|2nd Gen AMD EPYC 7R32|16|8|2|1 x NVIDIA A10G GPU|24 GiB (1 x 24 GiB)|


Performance specifications 316


-----

**Instance**


**BurstableMemory**


**Processor** **vCPUs CPU**


**Threads Accelerat**


**Accelerat**

|type|Col2|(GiB)|Col4|Col5|cores|per core|ors|or memor|
|---|---|---|---|---|---|---|---|---|
|g5.8xlarge|✗|128.00|2nd Gen AMD EPYC 7R32|32|16|2|1 x NVIDIA A10G GPU|24 GiB (1 x 24 GiB)|
|g5.12xlarge|✗|192.00|2nd Gen AMD EPYC 7R32|48|24|2|4 x NVIDIA A10G GPU|96 GiB (4 x 24 GiB)|
|g5.16xlarge|✗|256.00|2nd Gen AMD EPYC 7R32|64|32|2|1 x NVIDIA A10G GPU|24 GiB (1 x 24 GiB)|
|g5.24xlarge|✗|384.00|2nd Gen AMD EPYC 7R32|96|48|2|4 x NVIDIA A10G GPU|96 GiB (4 x 24 GiB)|
|g5.48xlarge|✗|768.00|2nd Gen AMD EPYC 7R32|192|96|2|8 x NVIDIA A10G GPU|192 GiB (8 x 24 GiB)|
|G5g|||||||||


Performance specifications 317


-----

**Instance**


**BurstableMemory**


**Processor** **vCPUs CPU**


**Threads Accelerat**


**Accelerat**

|type|Col2|(GiB)|Col4|Col5|cores|per core|ors|or memor|
|---|---|---|---|---|---|---|---|---|
|g5g.xlarge|✗|8.00|AWS Graviton2 Processor|4|4|1|1 x NVIDIA T4g GPU|16 GiB (1 x 16 GiB)|
|g5g.2xlarge|✗|16.00|AWS Graviton2 Processor|8|8|1|1 x NVIDIA T4g GPU|16 GiB (1 x 16 GiB)|
|g5g.4xlarge|✗|32.00|AWS Graviton2 Processor|16|16|1|1 x NVIDIA T4g GPU|16 GiB (1 x 16 GiB)|
|g5g.8xlarge|✗|64.00|AWS Graviton2 Processor|32|32|1|1 x NVIDIA T4g GPU|16 GiB (1 x 16 GiB)|
|g5g.16xla rge|✗|128.00|AWS Graviton2 Processor|64|64|1|2 x NVIDIA T4g GPU|32 GiB (2 x 16 GiB)|


Performance specifications 318


-----

**Instance**


**BurstableMemory**


**Processor** **vCPUs CPU**


**Threads Accelerat**


**Accelerat**

|type|Col2|(GiB)|Col4|Col5|cores|per core|ors|or memor|
|---|---|---|---|---|---|---|---|---|
|g5g.metal|✗|128.00|AWS Graviton2 Processor|64|64|1|2 x NVIDIA T4g GPU|32 GiB (2 x 16 GiB)|
|G6|||||||||
|g6.xlarge|✗|16.00|AMD EPYC 7R13|4|2|2|1 x NVIDIA L4 GPU|22 GiB (1 x 22 GiB)|
|g6.2xlarge|✗|32.00|AMD EPYC 7R13|8|4|2|1 x NVIDIA L4 GPU|22 GiB (1 x 22 GiB)|
|g6.4xlarge|✗|64.00|AMD EPYC 7R13|16|8|2|1 x NVIDIA L4 GPU|22 GiB (1 x 22 GiB)|
|g6.8xlarge|✗|128.00|AMD EPYC 7R13|32|16|2|1 x NVIDIA L4 GPU|22 GiB (1 x 22 GiB)|


Performance specifications 319


-----

**Instance**


**BurstableMemory**


**Processor** **vCPUs CPU**


**Threads Accelerat**


**Accelerat**

|type|Col2|(GiB)|Col4|Col5|cores|per core|ors|or memor|
|---|---|---|---|---|---|---|---|---|
|g6.12xlarge|✗|192.00|AMD EPYC 7R13|48|24|2|4 x NVIDIA L4 GPU|357 GiB (4 x 89 GiB)|
|g6.16xlarge|✗|256.00|AMD EPYC 7R13|64|32|2|1 x NVIDIA L4 GPU|22 GiB (1 x 22 GiB)|
|g6.24xlarge|✗|384.00|AMD EPYC 7R13|96|48|2|4 x NVIDIA L4 GPU|357 GiB (4 x 89 GiB)|
|g6.48xlarge|✗|768.00|AMD EPYC 7R13|192|96|2|8 x NVIDIA L4 GPU|1430 GiB (8 x 178 GiB)|
|Gr6|||||||||
|gr6.4xlarge|✗|128.00|AMD EPYC 7R13|16|8|2|1 x NVIDIA L4 GPU|22 GiB (1 x 22 GiB)|


Performance specifications 320


-----

**Instance**


**BurstableMemory**


**Processor** **vCPUs CPU**


**Threads Accelerat**


**Accelerat**

|type|Col2|(GiB)|Col4|Col5|cores|per core|ors|or memor|
|---|---|---|---|---|---|---|---|---|
|gr6.8xlarge|✗|256.00|AMD EPYC 7R13|32|16|2|1 x NVIDIA L4 GPU|22 GiB (1 x 22 GiB)|
|Inf1|||||||||
|inf1.xlarge|✗|8.00|Intel Xeon P-8259L|4|2|2|1 x AWS Inferentia inference accelerator|8 GiB (1 x 8 GiB)|
|inf1.2xlarge|✗|16.00|Intel Xeon P-8259L|8|4|2|1 x AWS Inferentia inference accelerator|8 GiB (1 x 8 GiB)|
|inf1.6xlarge|✗|48.00|Intel Xeon P-8259L|24|12|2|4 x AWS Inferentia inference accelerator|32 GiB (4 x 8 GiB)|
|inf1.24xl arge|✗|192.00|Intel Xeon P-8259L|96|48|2|16 x AWS Inferentia inference accelerator|128 GiB (16 x 8 GiB)|
|Inf2|||||||||


Performance specifications 321


-----

**Instance**


**BurstableMemory**


**Processor** **vCPUs CPU**


**Threads Accelerat**


**Accelerat**

|type|Col2|(GiB)|Col4|Col5|cores|per core|ors|or memor|
|---|---|---|---|---|---|---|---|---|
|inf2.xlarge|✗|16.00|AMD EPYC 7R13|4|2|2|1 x AWS Inferentia inference accelerator|32 GiB (1 x 32 GiB)|
|inf2.8xlarge|✗|128.00|AMD EPYC 7R13|32|16|2|1 x AWS Inferentia inference accelerator|32 GiB (1 x 32 GiB)|
|inf2.24xl arge|✗|384.00|AMD EPYC 7R13|96|48|2|6 x AWS Inferentia inference accelerator|192 GiB (6 x 32 GiB)|
|inf2.48xl arge|✗|768.00|AMD EPYC 7R13|192|96|2|12 x AWS Inferentia inference accelerator|384 GiB (12 x 32 GiB)|
|P2|||||||||
|p2.xlarge|✗|61.00|Intel Xeon E5-2686v4|4|2|2|1 x NVIDIA K80 GPU|12 GiB (1 x 12 GiB)|


Performance specifications 322


-----

**Instance**


**BurstableMemory**


**Processor** **vCPUs CPU**


**Threads Accelerat**


**Accelerat**

|type|Col2|(GiB)|Col4|Col5|cores|per core|ors|or memor|
|---|---|---|---|---|---|---|---|---|
|p2.8xlarge|✗|488.00|Intel Xeon E5-2686v4|32|16|2|8 x NVIDIA K80 GPU|96 GiB (8 x 12 GiB)|
|p2.16xlarge|✗|732.00|Intel Xeon E5-2686 v4|64|32|2|16 x NVIDIA K80 GPU|192 GiB (16 x 12 GiB)|
|P3|||||||||
|p3.2xlarge|✗|61.00|Intel Xeon E5-2686 v4|8|4|2|1 x NVIDIA V100 GPU|16 GiB (1 x 16 GiB)|
|p3.8xlarge|✗|244.00|Intel Xeon E5-2686 v4|32|16|2|4 x NVIDIA V100 GPU|64 GiB (4 x 16 GiB)|
|p3.16xlarge|✗|488.00|Intel Xeon E5-2686 v4|64|32|2|8 x NVIDIA V100 GPU|128 GiB (8 x 16 GiB)|
|P3dn|||||||||


Performance specifications 323


-----

**Instance**


**BurstableMemory**


**Processor** **vCPUs CPU**


**Threads Accelerat**


**Accelerat**

|type|Col2|(GiB)|Col4|Col5|cores|per core|ors|or memor|
|---|---|---|---|---|---|---|---|---|
|p3dn.24xl arge|✗|768.00|Intel Xeon Platinum 8175|96|48|2|8 x NVIDIA V100 GPU|256 GiB (8 x 32 GiB)|
|P4d|||||||||
|p4d.24xla rge|✗|1152.00|Intel Xeon Platinum 8175|96|48|2|8 x NVIDIA A100 GPU|320 GiB (8 x 40 GiB)|
|P4de|||||||||
|p4de.24xl arge|✗|1152.00|Intel Xeon Platinum 8175|96|48|2|8 x NVIDIA A100 GPU|640 GiB (8 x 80 GiB)|
|P5|||||||||
|p5.48xlarge|✗|2048.00|AMD EPYC 7R13|192|96|2|8 x NVIDIA H100 GPU|640 GiB (8 x 80 GiB)|
|Trn1|||||||||


Performance specifications 324


-----

**Instance**


**BurstableMemory**


**Processor** **vCPUs CPU**


**Threads Accelerat**


**Accelerat**

|type|Col2|(GiB)|Col4|Col5|cores|per core|ors|or memor|
|---|---|---|---|---|---|---|---|---|
|trn1.2xlarge|✗|32.00|Intel Xeon Ice Lake 8375C|8|4|2|1 x AWS Trainium accelerat ors|32 GiB (1 x 32 GiB)|
|trn1.32xl arge|✗|512.00|Intel Xeon Ice Lake 8375C|128|64|2|16 x AWS Trainium accelerat ors|512 GiB (16 x 32 GiB)|
|Trn1n|||||||||
|trn1n.32x large|✗|512.00|Intel Xeon Ice Lake|128|64|2|16 x AWS Trainium accelerat ors|512 GiB (16 x 32 GiB)|
|VT1|||||||||
|vt1.3xlarge|✗|24.00|Intel Cascade Lake P-8259CL|12|6|2|1 x Xilinx U30 media accelerator|24 GiB (1 x 24 GiB)|
|vt1.6xlarge|✗|48.00|Intel Cascade Lake P-8259CL|24|12|2|2 x Xilinx U30 media accelerator|48 GiB (2 x 24 GiB)|


Performance specifications 325


-----

|vt1.24xlarge|✗|192.00|Intel Cascade Lake P-8259CL|96|48|2|8 x Xilinx U30 media accelerator|192 GiB (8 x 24 GiB)|
|---|---|---|---|---|---|---|---|---|


**Instance** **BurstableMemory Processor** **vCPUs CPU** **Threads Accelerat** **Accelerat**
**type** **(GiB)** **cores** **per** **ors** **or**

**core** **memory**

#### Network specifications

|Instance type|Baseline / Burst bandwidth (Gbps)|EFA|ENA|ENA Express|Network cards|Max. network interface s|IP addresse per interface|IPv6 s|
|---|---|---|---|---|---|---|---|---|
|DL1|||||||||
|dl1.24xlarge|4x 100 Gigabit|✓|✓|✗|4|60|50|✓|
|DL2q|||||||||
|dl2q.24xlarge|100 Gigabit|✓|✓|✗|1|15|50|✓|
|F1|||||||||
|1 f1.2xlarge|Up to 10 Gigabit|✗|✓|✗|1|4|15|✓|
|1 f1.4xlarge|Up to 10 Gigabit|✗|✓|✗|1|8|30|✓|
|f1.16xlarge|25 Gigabit|✗|✓|✗|1|8|50|✓|
|G4ad|||||||||



Network specifications 326


-----

|Col1|bandwidth (Gbps)|Col3|Col4|Col5|Col6|interface s|per interface|Col9|
|---|---|---|---|---|---|---|---|---|
|1 g4ad.xlarge|2.0 / 10.0|✗|✓|✗|1|2|4|✓|
|1 g4ad.2xlarge|4.167 / 10.0|✗|✓|✗|1|2|4|✓|
|1 g4ad.4xlarge|8.333 / 10.0|✗|✓|✗|1|3|10|✓|
|g4ad.8xlarge|15 Gigabit|✗|✓|✗|1|4|15|✓|
|g4ad.16xlarge|25 Gigabit|✗|✓|✗|1|8|30|✓|
|G4dn|||||||||
|1 g4dn.xlarge|5.0 / 25.0|✗|✓|✗|1|3|10|✓|
|g4dn.2xlarge 1|10.0 / 25.0|✗|✓|✗|1|3|10|✓|
|g4dn.4xlarge 1|20.0 / 25.0|✗|✓|✗|1|3|10|✓|
|g4dn.8xlarge|50 Gigabit|✓|✓|✗|1|4|15|✓|
|g4dn.12xlarge|50 Gigabit|✓|✓|✗|1|8|30|✓|
|g4dn.16xlarge|50 Gigabit|✓|✓|✗|1|4|15|✓|
|g4dn.metal|100 Gigabit|✓|✓|✗|1|15|50|✓|
|G5|||||||||
|1 g5.xlarge|2.5 / 10.0|✗|✓|✗|1|4|15|✓|
|1 g5.2xlarge|5.0 / 10.0|✗|✓|✗|1|4|15|✓|
|1 g5.4xlarge|10.0 / 25.0|✗|✓|✗|1|8|30|✓|


**Instance type** **Baseline /** **EFA** **ENA** **ENA** **Network** **Max.** **IP** **IPv6**
**Burst** **Express** **cards** **network** **addresses**
**bandwidth** **interface** **per**
**(Gbps)** **s** **interface**


Network specifications 327


-----

|Col1|bandwidth (Gbps)|Col3|Col4|Col5|Col6|interface s|per interface|Col9|
|---|---|---|---|---|---|---|---|---|
|g5.8xlarge|25 Gigabit|✓|✓|✗|1|8|30|✓|
|g5.12xlarge|40 Gigabit|✓|✓|✗|1|15|50|✓|
|g5.16xlarge|25 Gigabit|✓|✓|✗|1|8|30|✓|
|g5.24xlarge|50 Gigabit|✓|✓|✗|1|15|50|✓|
|g5.48xlarge|100 Gigabit|✓|✓|✗|1|7|50|✓|
|G5g|||||||||
|1 g5g.xlarge|1.25 / 10.0|✗|✓|✗|1|4|15|✓|
|1 g5g.2xlarge|2.5 / 10.0|✗|✓|✗|1|4|15|✓|
|1 g5g.4xlarge|5.0 / 10.0|✗|✓|✗|1|8|30|✓|
|g5g.8xlarge|12 Gigabit|✗|✓|✗|1|8|30|✓|
|g5g.16xlarge|25 Gigabit|✗|✓|✗|1|15|50|✓|
|g5g.metal|25 Gigabit|✗|✓|✗|1|15|50|✓|
|G6|||||||||
|1 g6.xlarge|2.5 / 10.0|✗|✓|✗|1|4|15|✓|
|1 g6.2xlarge|5.0 / 10.0|✗|✓|✗|1|4|15|✓|
|1 g6.4xlarge|10.0 / 25.0|✗|✓|✗|1|8|30|✓|
|g6.8xlarge|25 Gigabit|✓|✓|✗|1|8|30|✓|
|g6.12xlarge|40 Gigabit|✓|✓|✗|1|8|30|✓|
|g6.16xlarge|25 Gigabit|✓|✓|✗|1|15|50|✓|


**Instance type** **Baseline /** **EFA** **ENA** **ENA** **Network** **Max.** **IP** **IPv6**
**Burst** **Express** **cards** **network** **addresses**
**bandwidth** **interface** **per**
**(Gbps)** **s** **interface**


Network specifications 328


-----

|Col1|bandwidth (Gbps)|Col3|Col4|Col5|Col6|interface s|per interface|Col9|
|---|---|---|---|---|---|---|---|---|
|g6.24xlarge|50 Gigabit|✓|✓|✗|1|15|50|✓|
|g6.48xlarge|100 Gigabit|✓|✓|✓|1|15|50|✓|
|Gr6|||||||||
|1 gr6.4xlarge|10.0 / 25.0|✗|✓|✗|1|8|30|✓|
|gr6.8xlarge|25 Gigabit|✓|✓|✗|1|8|30|✓|
|Inf1|||||||||
|1 inf1.xlarge|5.0 / 25.0|✗|✓|✗|1|4|10|✓|
|1 inf1.2xlarge|5.0 / 25.0|✗|✓|✗|1|4|10|✓|
|inf1.6xlarge|25 Gigabit|✗|✓|✗|1|8|30|✓|
|inf1.24xlarge|100 Gigabit|✓|✓|✗|1|11|30|✓|
|Inf2|||||||||
|1 inf2.xlarge|2.083 / 15.0|✗|✓|✗|1|4|15|✓|
|1 inf2.8xlarge|16.667 / 25.0|✗|✓|✗|1|8|30|✓|
|inf2.24xlarge|50 Gigabit|✗|✓|✗|1|15|50|✓|
|inf2.48xlarge|100 Gigabit|✗|✓|✗|1|15|50|✓|
|P2|||||||||
|p2.xlarge|High|✗|✓|✗|1|4|15|✓|
|p2.8xlarge|10 Gigabit|✗|✓|✗|1|8|30|✓|
|p2.16xlarge|25 Gigabit|✗|✓|✗|1|8|30|✓|


**Instance type** **Baseline /** **EFA** **ENA** **ENA** **Network** **Max.** **IP** **IPv6**
**Burst** **Express** **cards** **network** **addresses**
**bandwidth** **interface** **per**
**(Gbps)** **s** **interface**


Network specifications 329


-----

|Instance type Baseline / Burst bandwidth (Gbps) EFA ENA ENA Express Network cards Max. network interface s IP addresses per interface IPv6|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
|P3|||||||||
|1 p3.2xlarge|Up to 10 Gigabit|✗|✓|✗|1|4|15|✓|
|p3.8xlarge|10 Gigabit|✗|✓|✗|1|8|30|✓|
|p3.16xlarge|25 Gigabit|✗|✓|✗|1|8|30|✓|
|P3dn|||||||||
|p3dn.24xlarge|100 Gigabit|✓|✓|✗|1|15|50|✓|
|P4d|||||||||
|p4d.24xlarge|4x 100 Gigabit|✓|✓|✗|4|60|50|✓|
|P4de|||||||||
|p4de.24xlarge|4x 100 Gigabit|✓|✓|✗|4|60|50|✓|
|P5|||||||||
|p5.48xlarge|3200 Gigabit|✓|✓|✗|32|64|50|✓|
|Trn1|||||||||
|1 trn1.2xlarge|3.125 / 12.5|✗|✓|✗|1|4|15|✓|
|trn1.32xlarge|8x 100 Gigabit|✓|✓|✗|8|40|50|✓|
|Trn1n|||||||||


Network specifications 330


-----

|Col1|bandwidth (Gbps)|Col3|Col4|Col5|Col6|interface s|per interface|Col9|
|---|---|---|---|---|---|---|---|---|
|trn1n.32x large|16x 100 Gigabit|✓|✓|✗|16|80|50|✓|
|VT1|||||||||
|vt1.3xlarge|3.12 Gigabit|✗|✓|✗|1|4|15|✓|
|vt1.6xlarge|6.25 Gigabit|✗|✓|✗|1|8|30|✓|
|vt1.24xlarge|25 Gigabit|✓|✓|✗|1|15|50|✓|


**Instance type** **Baseline /** **EFA** **ENA** **ENA** **Network** **Max.** **IP** **IPv6**
**Burst** **Express** **cards** **network** **addresses**
**bandwidth** **interface** **per**
**(Gbps)** **s** **interface**


**Note**

1
These instances have a baseline bandwidth and can use a network I/O credit mechanism
to burst beyond their baseline bandwidth on a best effort basis. Other instances types
[can sustain their maximum performance indefinitely. For more information, see instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-network-bandwidth.html)
[network bandwidth.](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-network-bandwidth.html)

#### Amazon EBS specifications

The following table indicates which instance types are Amazon EBS optimized by default and
which optionally support it. It also describes their EBS-optimized performance, including dedicated
bandwidth to Amazon EBS, the typical maximum aggregate throughput that can be achieved on
that dedicated connection with a streaming read workload and 128 KiB I/O size, and the maximum
IOPS the instance type can support when using a 16 KiB I/O size. Instance types not listed do not
support Amazon EBS optimization.

**Important**

An instance's EBS performance is bounded by the instance's performance limits, or
the aggregated performance of its attached volumes, whichever is smaller. To achieve
maximum EBS performance, an instance must have attached volumes that provide a

Amazon EBS specifications 331


-----

combined performance equal to or greater than the maximum instance performance. For

example, to achieve 80,000 IOPS for r6i.16xlarge, the instance must have at least 5
```
   gp3 volumes provisioned with 16,000 IOPS each (5 volumes x 16,000 IOPS = 80,000

```
IOPS).

We recommand that you choose an EBS–optimized instance type that provides more
dedicated Amazon EBS throughput than your application needs; otherwise, the connection
between Amazon EBS and Amazon EC2 can become a performance bottleneck.

|Instance type|Baseline / Maximum bandwidth (Mbps)|Baseline / Maximum throughput (MB/s, 128 KiB I/O)|Baseline / Maximum IOPS (16 KiB I/O)|NVMe|EBS optimization 2|
|---|---|---|---|---|---|
|DL1||||||
|dl1.24xlarge|19000.00|2375.00|80000.00|✓|default|
|DL2q||||||
|dl2q.24xl arge|19000.00|2375.00|80000.00|✓|default|
|F1||||||
|f1.2xlarge|1700.00|212.50|12000.00|✗|default|
|f1.4xlarge|3500.00|437.50|44000.00|✗|default|
|f1.16xlarge|14000.00|1750.00|75000.00|✗|default|
|G4ad||||||
|1 g4ad.xlarge|400.00 / 3170.00|50.00 / 396.25|1700.00 / 13333.00|✓|default|
|g4ad.2xlarge 1|800.00 / 3170.00|100.00 / 396.25|3400.00 / 13333.00|✓|default|



Amazon EBS specifications 332


-----

**Instance**


**Baseline /**


**Baseline /**


**Baseline /**


**NVMe** **EBS**

|type|Maximum bandwidth (Mbps)|Maximum throughput (MB/s, 128 KiB I/O)|Maximum IOPS (16 KiB I/O)|Col5|optimization 2|
|---|---|---|---|---|---|
|g4ad.4xlarge 1|1580.00 / 3170.00|197.50 / 396.25|6700.00 / 13333.00|✓|default|
|g4ad.8xlarge|3170.00|396.25|13333.00|✓|default|
|g4ad.16xl arge|6300.00|787.50|26667.00|✓|default|
|G4dn||||||
|1 g4dn.xlarge|950.00 / 3500.00|118.75 / 437.50|3000.00 / 20000.00|✓|default|
|g4dn.2xlarge 1|1150.00 / 3500.00|143.75 / 437.50|6000.00 / 20000.00|✓|default|
|g4dn.4xlarge|4750.00|593.75|20000.00|✓|default|
|g4dn.8xlarge|9500.00|1187.50|40000.00|✓|default|
|g4dn.12xl arge|9500.00|1187.50|40000.00|✓|default|
|g4dn.16xl arge|9500.00|1187.50|40000.00|✓|default|
|g4dn.metal|19000.00|2375.00|80000.00|✓|default|
|G5||||||
|1 g5.xlarge|700.00 / 3500.00|87.50 / 437.50|3000.00 / 15000.00|✓|default|


Amazon EBS specifications 333


-----

**Instance**


**Baseline /**


**Baseline /**


**Baseline /**


**NVMe** **EBS**

|type|Maximum bandwidth (Mbps)|Maximum throughput (MB/s, 128 KiB I/O)|Maximum IOPS (16 KiB I/O)|Col5|optimization 2|
|---|---|---|---|---|---|
|1 g5.2xlarge|850.00 / 3500.00|106.25 / 437.50|3500.00 / 15000.00|✓|default|
|g5.4xlarge|4750.00|593.75|20000.00|✓|default|
|g5.8xlarge|16000.00|2000.00|65000.00|✓|default|
|g5.12xlarge|16000.00|2000.00|65000.00|✓|default|
|g5.16xlarge|16000.00|2000.00|65000.00|✓|default|
|g5.24xlarge|19000.00|2375.00|80000.00|✓|default|
|g5.48xlarge|19000.00|2375.00|80000.00|✓|default|
|G5g||||||
|1 g5g.xlarge|1188.00 / 4750.00|148.50 / 593.75|6000.00 / 20000.00|✓|default|
|1 g5g.2xlarge|2375.00 / 4750.00|296.88 / 593.75|12000.00 / 20000.00|✓|default|
|g5g.4xlarge|4750.00|593.75|20000.00|✓|default|
|g5g.8xlarge|9500.00|1187.50|40000.00|✓|default|
|g5g.16xlarge|19000.00|2375.00|80000.00|✓|default|
|g5g.metal|19000.00|2375.00|80000.00|✓|default|
|G6||||||
|1 g6.xlarge|1000.00 / 5000.00|125.00 / 625.00|4000.00 / 20000.00|✓|default|


Amazon EBS specifications 334


-----

**Instance**


**Baseline /**


**Baseline /**


**Baseline /**


**NVMe** **EBS**

|type|Maximum bandwidth (Mbps)|Maximum throughput (MB/s, 128 KiB I/O)|Maximum IOPS (16 KiB I/O)|Col5|optimization 2|
|---|---|---|---|---|---|
|1 g6.2xlarge|2000.00 / 5000.00|250.00 / 625.00|8000.00 / 20000.00|✓|default|
|g6.4xlarge|8000.00|1000.00|32000.00|✓|default|
|g6.8xlarge|16000.00|2000.00|64000.00|✓|default|
|g6.12xlarge|20000.00|2500.00|80000.00|✓|default|
|g6.16xlarge|20000.00|2500.00|80000.00|✓|default|
|g6.24xlarge|30000.00|3750.00|120000.00|✓|default|
|g6.48xlarge|60000.00|7500.00|240000.00|✓|default|
|Gr6||||||
|gr6.4xlarge|8000.00|1000.00|32000.00|✓|default|
|gr6.8xlarge|16000.00|2000.00|64000.00|✓|default|
|Inf1||||||
|1 inf1.xlarge|1190.00 / 4750.00|148.75 / 593.75|4000.00 / 20000.00|✓|default|
|1 inf1.2xlarge|1190.00 / 4750.00|148.75 / 593.75|6000.00 / 20000.00|✓|default|
|inf1.6xlarge|4750.00|593.75|20000.00|✓|default|
|inf1.24xlarge|19000.00|2375.00|80000.00|✓|default|
|Inf2||||||


Amazon EBS specifications 335


-----

**Instance**


**Baseline /**


**Baseline /**


**Baseline /**


**NVMe** **EBS**

|type|Maximum bandwidth (Mbps)|Maximum throughput (MB/s, 128 KiB I/O)|Maximum IOPS (16 KiB I/O)|Col5|optimization 2|
|---|---|---|---|---|---|
|1 inf2.xlarge|1250.00 / 10000.00|156.25 / 1250.00|6000.00 / 40000.00|✓|default|
|inf2.8xlarge|10000.00|1250.00|40000.00|✓|default|
|inf2.24xlarge|30000.00|3750.00|120000.00|✓|default|
|inf2.48xlarge|60000.00|7500.00|240000.00|✓|default|
|P2||||||
|p2.xlarge|750.00|93.75|6000.00|✗|default|
|p2.8xlarge|5000.00|625.00|32500.00|✗|default|
|p2.16xlarge|10000.00|1250.00|65000.00|✗|default|
|P3||||||
|p3.2xlarge|1750.00|218.75|10000.00|✗|default|
|p3.8xlarge|7000.00|875.00|40000.00|✗|default|
|p3.16xlarge|14000.00|1750.00|80000.00|✗|default|
|P3dn||||||
|p3dn.24xl arge|19000.00|2375.00|80000.00|✓|default|
|P4d||||||
|p4d.24xlarge|19000.00|2375.00|80000.00|✓|default|
|P4de||||||


Amazon EBS specifications 336


-----

**Instance**

|type|Maximum bandwidth (Mbps)|Maximum throughput (MB/s, 128 KiB I/O)|Maximum IOPS (16 KiB I/O)|Col5|optimization 2|
|---|---|---|---|---|---|
|p4de.24xl arge|19000.00|2375.00|80000.00|✓|default|
|P5||||||
|p5.48xlarge|80000.00|10000.00|260000.00|✓|default|
|Trn1||||||
|trn1.2xlarge 1|5000.00 / 20000.00|625.00 / 2500.00|16250.00 / 65000.00|✓|default|
|trn1.32xlarge|80000.00|10000.00|260000.00|✓|default|
|Trn1n||||||
|trn1n.32x large|80000.00|10000.00|260000.00|✓|default|
|VT1||||||
|1 vt1.3xlarge|2375.00 / 4750.00|296.88 / 593.75|10000.00 / 20000.00|✓|default|
|vt1.6xlarge|4750.00|593.75|20000.00|✓|default|
|vt1.24xlarge|19000.00|2375.00|80000.00|✓|default|



**Note**


**Baseline /**
**Maximum**
**bandwidth**
**(Mbps)**


**Baseline /**
**Maximum**
**throughput**
**(MB/s, 128**
**KiB I/O)**


**Baseline /**
**Maximum**
**IOPS (16 KiB**
**I/O)**


**NVMe** **EBS**
**optimization**


1
These instances can support maximum performance for 30 minutes at least once every 24
hours, after which they revert to their baseline performance. Other instances can sustain

Amazon EBS specifications 337


-----

the maximum performance indefinitely. If your workload requires sustained maximum
performance for longer than 30 minutes, use one of these instances.
2
```
   default indicates that instances are enabled for EBS optimization by default.
   supported indicates that instances can optionally be enabled for EBS optimization For

```
[more information, see Amazon EBS–optimized instances.](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-optimized.html)

#### Instance store specifications

The following table shows the instance store volume configuration for supported instance types,
along with the aggregated IOPS performance with 4,096 byte block size at queue depth saturation.

|Instance type|Instance store volumes|Instance store type|100% random read IOPS / Write IOPS|Needs initializ 1 ation|TRIM support 2|
|---|---|---|---|---|---|
|DL1||||||
|dl1.24xlarge|4 x 1000 GB|NVMe SSD|1,000,000 / 800,000||✓|
|F1||||||
|f1.2xlarge|1 x 470 GB|NVMe SSD|||✓|
|f1.4xlarge|1 x 940 GB|NVMe SSD|||✓|
|f1.16xlarge|4 x 940 GB|NVMe SSD|||✓|
|G4ad||||||
|g4ad.xlarge|1 x 150 GB|NVMe SSD|10,417 / 8,333||✓|
|g4ad.2xlarge|1 x 300 GB|NVMe SSD|20,833 / 16,667||✓|



Instance store specifications 338


-----

|Instance type|Instance store volumes|Instance store type|100% random read IOPS / Write IOPS|Needs initializ ation 1|TRIM support 2|
|---|---|---|---|---|---|
|g4ad.4xlarge|1 x 600 GB|NVMe SSD|41,667 / 33,333||✓|
|g4ad.8xlarge|1 x 1200 GB|NVMe SSD|83,333 / 66,667||✓|
|g4ad.16xlarge|2 x 1200 GB|NVMe SSD|166,666 / 133,332||✓|
|G4dn||||||
|g4dn.xlarge|1 x 125 GB|NVMe SSD|42,500 / 32,500||✓|
|g4dn.2xlarge|1 x 225 GB|NVMe SSD|42,500 / 32,500||✓|
|g4dn.4xlarge|1 x 225 GB|NVMe SSD|85,000 / 65,000||✓|
|g4dn.8xlarge|1 x 900 GB|NVMe SSD|250,000 / 200,000||✓|
|g4dn.12xlarge|1 x 900 GB|NVMe SSD|250,000 / 200,000||✓|
|g4dn.16xlarge|1 x 900 GB|NVMe SSD|250,000 / 200,000||✓|
|g4dn.metal|2 x 900 GB|NVMe SSD|500,000 / 400,000||✓|
|G5||||||
|g5.xlarge|1 x 250 GB|NVMe SSD|40,625 / 20,313||✓|


Instance store specifications 339


-----

|Instance type|Instance store volumes|Instance store type|100% random read IOPS / Write IOPS|Needs initializ ation 1|TRIM support 2|
|---|---|---|---|---|---|
|g5.2xlarge|1 x 450 GB|NVMe SSD|40,625 / 20,313||✓|
|g5.4xlarge|1 x 600 GB|NVMe SSD|125,000 / 62,500||✓|
|g5.8xlarge|1 x 900 GB|NVMe SSD|250,000 / 125,000||✓|
|g5.12xlarge|1 x 3800 GB|NVMe SSD|312,500 / 156,250||✓|
|g5.16xlarge|1 x 1900 GB|NVMe SSD|250,000 / 125,000||✓|
|g5.24xlarge|1 x 3800 GB|NVMe SSD|312,500 / 156,250||✓|
|g5.48xlarge|2 x 3800 GB|NVMe SSD|625,000 / 312,500||✓|
|G6||||||
|g6.xlarge|1 x 250 GB|NVMe SSD|40,625 / 20,000||✓|
|g6.2xlarge|1 x 450 GB|NVMe SSD|40,625 / 20,000||✓|
|g6.4xlarge|1 x 600 GB|NVMe SSD|125,000 / 40,000||✓|
|g6.8xlarge|2 x 450 GB|NVMe SSD|250,000 / 80,000||✓|


Instance store specifications 340


-----

|Instance type|Instance store volumes|Instance store type|100% random read IOPS / Write IOPS|Needs initializ ation 1|TRIM support 2|
|---|---|---|---|---|---|
|g6.12xlarge|4 x 940 GB|NVMe SSD|312,500 / 125,000||✓|
|g6.16xlarge|2 x 940 GB|NVMe SSD|250,000 / 80,000||✓|
|g6.24xlarge|4 x 940 GB|NVMe SSD|312,500 / 156,248||✓|
|g6.48xlarge|8 x 940 GB|NVMe SSD|625,000 / 312,496||✓|
|Gr6||||||
|gr6.4xlarge|1 x 600 GB|NVMe SSD|125,000 / 40,000||✓|
|gr6.8xlarge|2 x 450 GB|NVMe SSD|250,000 / 80,000||✓|
|P3dn||||||
|p3dn.24xlarge|2 x 900 GB|NVMe SSD|700,000 / 340,000||✓|
|P4d||||||
|p4d.24xlarge|8 x 1000 GB|NVMe SSD|2,000,000 / 1,600,000||✓|
|P4de||||||
|p4de.24xlarge|8 x 1000 GB|NVMe SSD|2,000,000 / 1,600,000||✓|
|P5||||||


Instance store specifications 341


-----

|Instance type|Instance store volumes|Instance store type|100% random read IOPS / Write IOPS|Needs initializ ation 1|TRIM support 2|
|---|---|---|---|---|---|
|p5.48xlarge|8 x 3800 GB|NVMe SSD|4,400,000 / 2,200,000||✓|
|Trn1||||||
|trn1.2xlarge|1 x 474 GB|NVMe SSD|107,500 / 45,000||✓|
|trn1.32xlarge|4 x 1900 GB|NVMe SSD|1,720,000 / 720,000||✓|
|Trn1n||||||
|trn1n.32xlarge|4 x 1900 GB|NVMe SSD|1,720,000 / 720,000||✓|


1
Volumes attached to certain instances suffer a first-write penalty unless initialized. For more
[information, see Optimize disk performance for instance store volumes.](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/disk-performance.html)

2
[For more information, see Instance store volume TRIM support.](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ssd-instance-store.html#InstanceStoreTrimSupport)

#### Security specifications

|Instance type|EBS encryptio n|Instance store encryptio n|Encryptio n in transit|AMD SEV-SNP|NitroTPM|Nitro Enclaves|
|---|---|---|---|---|---|---|
|DL1|||||||
|dl1.24xlarge|✓|✓|✓|✗|✗|✓|
|DL2q|||||||



Security specifications 342


-----

|Instance type|EBS encryptio n|Instance store encryptio n|Encryptio n in transit|AMD SEV-SNP|NitroTPM|Nitro Enclaves|
|---|---|---|---|---|---|---|
|dl2q.24xlarge|✓|Instance store not supported|✓|✗|✗|✓|
|F1|||||||
|f1.2xlarge|✓|✓|✗|✗|✗|✗|
|f1.4xlarge|✓|✓|✗|✗|✗|✗|
|f1.16xlarge|✓|✓|✗|✗|✗|✗|
|G4ad|||||||
|g4ad.xlarge|✓|✓|✓|✗|✗|✗|
|g4ad.2xlarge|✓|✓|✓|✗|✗|✗|
|g4ad.4xlarge|✓|✓|✓|✗|✗|✗|
|g4ad.8xlarge|✓|✓|✓|✗|✗|✗|
|g4ad.16xlarge|✓|✓|✓|✗|✗|✗|
|G4dn|||||||
|g4dn.xlarge|✓|✓|✓|✗|✓|✓|
|g4dn.2xlarge|✓|✓|✓|✗|✓|✓|
|g4dn.4xlarge|✓|✓|✓|✗|✓|✓|
|g4dn.8xlarge|✓|✓|✓|✗|✓|✓|
|g4dn.12xlarge|✓|✓|✓|✗|✓|✓|


Security specifications 343


-----

|Instance type|EBS encryptio n|Instance store encryptio n|Encryptio n in transit|AMD SEV-SNP|NitroTPM|Nitro Enclaves|
|---|---|---|---|---|---|---|
|g4dn.16xlarge|✓|✓|✓|✗|✓|✓|
|g4dn.metal|✓|✓|✓|✗|✗|✗|
|G5|||||||
|g5.xlarge|✓|✓|✓|✗|✓|✓|
|g5.2xlarge|✓|✓|✓|✗|✓|✓|
|g5.4xlarge|✓|✓|✓|✗|✓|✓|
|g5.8xlarge|✓|✓|✓|✗|✓|✓|
|g5.12xlarge|✓|✓|✓|✗|✓|✓|
|g5.16xlarge|✓|✓|✓|✗|✓|✓|
|g5.24xlarge|✓|✓|✓|✗|✓|✓|
|g5.48xlarge|✓|✓|✓|✗|✓|✓|
|G5g|||||||
|g5g.xlarge|✓|Instance store not supported|✗|✗|✗|✗|
|g5g.2xlarge|✓|Instance store not supported|✗|✗|✗|✗|
|g5g.4xlarge|✓|Instance store not supported|✗|✗|✗|✗|


Security specifications 344


-----

|Instance type|EBS encryptio n|Instance store encryptio n|Encryptio n in transit|AMD SEV-SNP|NitroTPM|Nitro Enclaves|
|---|---|---|---|---|---|---|
|g5g.8xlarge|✓|Instance store not supported|✗|✗|✗|✗|
|g5g.16xlarge|✓|Instance store not supported|✗|✗|✗|✗|
|g5g.metal|✓|Instance store not supported|✗|✗|✗|✗|
|G6|||||||
|g6.xlarge|✓|✓|✓|✗|✓|✓|
|g6.2xlarge|✓|✓|✓|✗|✓|✓|
|g6.4xlarge|✓|✓|✓|✗|✓|✓|
|g6.8xlarge|✓|✓|✓|✗|✓|✓|
|g6.12xlarge|✓|✓|✓|✗|✓|✓|
|g6.16xlarge|✓|✓|✓|✗|✓|✓|
|g6.24xlarge|✓|✓|✓|✗|✓|✓|
|g6.48xlarge|✓|✓|✓|✗|✓|✓|
|Gr6|||||||
|gr6.4xlarge|✓|✓|✓|✗|✓|✓|
|gr6.8xlarge|✓|✓|✓|✗|✓|✓|


Security specifications 345


-----

|Instance type EBS encryptio n Instance store encryptio n Encryptio n in transit AMD SEV-SNP NitroTPM Nitro Enclaves|Col2|Col3|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
|Inf1|||||||
|inf1.xlarge|✓|Instance store not supported|✓|✗|✓|✓|
|inf1.2xlarge|✓|Instance store not supported|✓|✗|✓|✓|
|inf1.6xlarge|✓|Instance store not supported|✓|✗|✓|✓|
|inf1.24xlarge|✓|Instance store not supported|✓|✗|✓|✓|
|Inf2|||||||
|inf2.xlarge|✓|Instance store not supported|✓|✗|✓|✓|
|inf2.8xlarge|✓|Instance store not supported|✓|✗|✓|✓|
|inf2.24xlarge|✓|Instance store not supported|✓|✗|✓|✓|


Security specifications 346


-----

|Instance type|EBS encryptio n|Instance store encryptio n|Encryptio n in transit|AMD SEV-SNP|NitroTPM|Nitro Enclaves|
|---|---|---|---|---|---|---|
|inf2.48xlarge|✓|Instance store not supported|✓|✗|✓|✓|
|P2|||||||
|p2.xlarge|✓|Instance store not supported|✗|✗|✗|✗|
|p2.8xlarge|✓|Instance store not supported|✗|✗|✗|✗|
|p2.16xlarge|✓|Instance store not supported|✗|✗|✗|✗|
|P3|||||||
|p3.2xlarge|✓|Instance store not supported|✗|✗|✗|✗|
|p3.8xlarge|✓|Instance store not supported|✗|✗|✗|✗|
|p3.16xlarge|✓|Instance store not supported|✗|✗|✗|✗|
|P3dn|||||||


Security specifications 347


-----

|Instance type|EBS encryptio n|Instance store encryptio n|Encryptio n in transit|AMD SEV-SNP|NitroTPM|Nitro Enclaves|
|---|---|---|---|---|---|---|
|p3dn.24xlarge|✓|✓|✓|✗|✗|✓|
|P4d|||||||
|p4d.24xlarge|✓|✓|✓|✗|✗|✓|
|P4de|||||||
|p4de.24xlarge|✓|✓|✓|✗|✗|✓|
|P5|||||||
|p5.48xlarge|✓|✓|✓|✗|✗|✓|
|Trn1|||||||
|trn1.2xlarge|✓|✓|✓|✗|✗|✗|
|trn1.32xlarge|✓|✓|✓|✗|✗|✗|
|Trn1n|||||||
|trn1n.32xlarge|✓|✓|✓|✗|✗|✗|
|VT1|||||||
|vt1.3xlarge|✓|Instance store not supported|✓|✗|✗|✗|
|vt1.6xlarge|✓|Instance store not supported|✓|✗|✗|✗|


Security specifications 348


-----

|vt1.24xlarge|✓|Instance store not supported|✓|✗|✗|✗|
|---|---|---|---|---|---|---|


**Instance type** **EBS** **Instance** **Encryptio** **AMD** **NitroTPM** **Nitro**
**encryptio** **store** **n in** **SEV-SNP** **Enclaves**
**n** **encryptio** **transit**

**n**


### Specifications for Amazon EC2 high-performance computing instances

High-performance computing instances are purpose built to offer the best price performance
for running HPC workloads at scale on AWS. These instances are ideal for applications that
benefit from high-performance processors, such as large, complex simulations and deep learning
workloads.

**Contents**

-  Available sizes

-  Platform summary

-  Performance specifications

-  Network specifications

-  Amazon EBS specifications

-  Instance store specifications

-  Security specifications

**Pricing**

[For pricing information, see Amazon EC2 On-Demand Pricing.](https://aws.amazon.com/ec2/pricing/on-demand/)

High-performance computing 349


-----

#### Available sizes

|Instance type|Available sizes|
|---|---|
|Hpc6a|hpc6a.48xlarge|
|Hpc6id|hpc6id.32xlarge|
|Hpc7a|hpc7a.12xlarge | hpc7a.24xlarge | hpc7a.48xlarge | hpc7a.96x large|
|Hpc7g|hpc7g.4xlarge | hpc7g.8xlarge | hpc7g.16xlarge|


 Platform summary

|Instance type|Hypervi r|soP rocessor type (architec ture)|Metal instances available|Dedicate Hosts support|dS pot support|Hibernati on support|Support operatin systems|
|---|---|---|---|---|---|---|---|
|Hpc6a|Nitro v4|AMD (x86_64)|✗|✗|✗|✗|Linux|
|Hpc6id|Nitro v4|Intel (x86_64)|✗|✗|✗|✗|Window | Linux|
|Hpc7a|Nitro v4|AMD (x86_64)|✗|✗|✗|✗|Window | Linux|
|Hpc7g|Nitro v5|AWS Graviton (arm64)|✗|✗|✗|✗|Linux|



Available sizes 350


-----

#### Performance specifications

|Instance type|Burstabl|eMemor (GiB)|y Processor|vCPUs|CPU cores|Thread per core|s Accelerat ors|Acceler or memor|
|---|---|---|---|---|---|---|---|---|
|Hpc6a|||||||||
|hpc6a.48x large|✗|384.00|AMD EPYC 7R13|96|96|1|✗|✗|
|Hpc6id|||||||||
|hpc6id.32 xlarge|✗|1024.00|Intel Xeon Ice Lake|64|64|1|✗|✗|
|Hpc7a|||||||||
|hpc7a.12x large|✗|768.00|AMD EPYC 9R14|24|24|1|✗|✗|
|hpc7a.24x large|✗|768.00|AMD EPYC 9R14|48|48|1|✗|✗|
|hpc7a.48x large|✗|768.00|AMD EPYC 9R14|96|96|1|✗|✗|
|hpc7a.96x large|✗|768.00|AMD EPYC 9R14|192|192|1|✗|✗|
|Hpc7g|||||||||
|hpc7g.4xl arge|✗|128.00|AWS Graviton3E Processor|16|16|1|✗|✗|
|hpc7g.8xl arge|✗|128.00|AWS Graviton3E Processor|32|32|1|✗|✗|



Performance specifications 351


-----

|hpc7g.16x large|✗|128.00|AWS Graviton3E Processor|64|64|1|✗|✗|
|---|---|---|---|---|---|---|---|---|


**Instance** **BurstableMemory Processor** **vCPUs CPU** **Threads Accelerat** **Accelerat**
**type** **(GiB)** **cores** **per** **ors** **or**

**core** **memory**

#### Network specifications

|Instance type|Baseline / Burst bandwidth (Gbps)|EFA|ENA|ENA Express|Network cards|Max. network interface s|IP addresses per interface|IPv6|
|---|---|---|---|---|---|---|---|---|
|Hpc6a|||||||||
|hpc6a.48x large|100 Gigabit|✓|✓|✗|1|2|50|✓|
|Hpc6id|||||||||
|hpc6id.32 xlarge|200 Gigabit|✓|✓|✗|2|2|50|✓|
|Hpc7a|||||||||
|hpc7a.12x large|300 Gigabit|✓|✓|✗|2|4|50|✓|
|hpc7a.24x large|300 Gigabit|✓|✓|✗|2|4|50|✓|
|hpc7a.48x large|300 Gigabit|✓|✓|✗|2|4|50|✓|
|hpc7a.96x large|300 Gigabit|✓|✓|✗|2|4|50|✓|



Network specifications 352


-----

|Instance type Baseline / Burst bandwidth (Gbps) EFA ENA ENA Express Network cards Max. network interface s IP addresses per interface IPv6|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
|Hpc7g|||||||||
|hpc7g.4xlarge|200 Gigabit|✓|✓|✗|1|4|50|✓|
|hpc7g.8xlarge|200 Gigabit|✓|✓|✗|1|4|50|✓|
|hpc7g.16x large|200 Gigabit|✓|✓|✗|1|4|50|✓|


#### Amazon EBS specifications

The following table indicates which instance types are Amazon EBS optimized by default and
which optionally support it. It also describes their EBS-optimized performance, including dedicated
bandwidth to Amazon EBS, the typical maximum aggregate throughput that can be achieved on
that dedicated connection with a streaming read workload and 128 KiB I/O size, and the maximum
IOPS the instance type can support when using a 16 KiB I/O size. Instance types not listed do not
support Amazon EBS optimization.

**Important**

An instance's EBS performance is bounded by the instance's performance limits, or
the aggregated performance of its attached volumes, whichever is smaller. To achieve
maximum EBS performance, an instance must have attached volumes that provide a
combined performance equal to or greater than the maximum instance performance. For

example, to achieve 80,000 IOPS for r6i.16xlarge, the instance must have at least 5
```
   gp3 volumes provisioned with 16,000 IOPS each (5 volumes x 16,000 IOPS = 80,000

```
IOPS).
We recommand that you choose an EBS–optimized instance type that provides more
dedicated Amazon EBS throughput than your application needs; otherwise, the connection
between Amazon EBS and Amazon EC2 can become a performance bottleneck.

Amazon EBS specifications 353


-----

|Instance type|Baseline / Maximum bandwidth (Mbps)|Baseline / Maximum throughput (MB/s, 128 KiB I/O)|Baseline / Maximum IOPS (16 KiB I/O)|NVMe|EBS optimization 2|
|---|---|---|---|---|---|
|Hpc6a||||||
|hpc6a.48x 1 large|87.00 / 2085.00|10.88 / 260.62|500.00 / 11000.00|✓|default|
|Hpc6id||||||
|hpc6id.32 1 xlarge|87.00 / 2085.00|10.88 / 260.62|500.00 / 11000.00|✓|default|
|Hpc7a||||||
|hpc7a.12x 1 large|87.00 / 2085.00|10.88 / 260.62|500.00 / 11000.00|✓|default|
|hpc7a.24x 1 large|87.00 / 2085.00|10.88 / 260.62|500.00 / 11000.00|✓|default|
|hpc7a.48x 1 large|87.00 / 2085.00|10.88 / 260.62|500.00 / 11000.00|✓|default|
|hpc7a.96x 1 large|87.00 / 2085.00|10.88 / 260.62|500.00 / 11000.00|✓|default|
|Hpc7g||||||
|hpc7g.4xl 1 arge|87.00 / 2085.00|10.88 / 260.62|500.00 / 11000.00|✓|default|
|hpc7g.8xl 1 arge|87.00 / 2085.00|10.88 / 260.62|500.00 / 11000.00|✓|default|


Amazon EBS specifications 354


-----

|hpc7g.16x 1 large|87.00 / 2085.00|10.88 / 260.62|500.00 / 11000.00|✓|default|
|---|---|---|---|---|---|


**Instance** **Baseline /** **Baseline /** **Baseline /** **NVMe** **EBS**
**type** **Maximum** **Maximum** **Maximum** **optimization**

**2**

**bandwidth** **throughput** **IOPS (16 KiB**
**(Mbps)** **(MB/s, 128** **I/O)**

**KiB I/O)**


**Note**

1
These instances can support maximum performance for 30 minutes at least once every 24
hours, after which they revert to their baseline performance. Other instances can sustain
the maximum performance indefinitely. If your workload requires sustained maximum
performance for longer than 30 minutes, use one of these instances.
2
```
   default indicates that instances are enabled for EBS optimization by default.
   supported indicates that instances can optionally be enabled for EBS optimization For

```
[more information, see Amazon EBS–optimized instances.](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-optimized.html)

#### Instance store specifications

The following table shows the instance store volume configuration for supported instance types,
along with the aggregated IOPS performance with 4,096 byte block size at queue depth saturation.

|Instance type|Instance store volumes|Instance store type|100% random read IOPS / Write IOPS|Needs initializ 1 ation|TRIM support 2|
|---|---|---|---|---|---|
|Hpc6id||||||
|hpc6id.32xlarge|4 x 3800 GB|NVMe SSD|2,146,664 / 1,073,336||✓|



1
Volumes attached to certain instances suffer a first-write penalty unless initialized. For more
[information, see Optimize disk performance for instance store volumes.](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/disk-performance.html)

Instance store specifications 355


-----

2
[For more information, see Instance store volume TRIM support.](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ssd-instance-store.html#InstanceStoreTrimSupport)

#### Security specifications

|Instance type|EBS encryptio n|Instance store encryptio n|Encryptio n in transit|AMD SEV-SNP|NitroTPM|Nitro Enclaves|
|---|---|---|---|---|---|---|
|Hpc6a|||||||
|hpc6a.48xlarge|✓|Instance store not supported|✓|✗|✓|✗|
|Hpc6id|||||||
|hpc6id.32xlarge|✓|✓|✓|✗|✓|✗|
|Hpc7a|||||||
|hpc7a.12xlarge|✓|Instance store not supported|✓|✗|✗|✗|
|hpc7a.24xlarge|✓|Instance store not supported|✓|✗|✗|✗|
|hpc7a.48xlarge|✓|Instance store not supported|✓|✗|✗|✗|
|hpc7a.96xlarge|✓|Instance store not supported|✓|✗|✗|✗|
|Hpc7g|||||||



Security specifications 356


-----

|Instance type|EBS encryptio n|Instance store encryptio n|Encryptio n in transit|AMD SEV-SNP|NitroTPM|Nitro Enclaves|
|---|---|---|---|---|---|---|
|hpc7g.4xlarge|✓|Instance store not supported|✓|✗|✗|✗|
|hpc7g.8xlarge|✓|Instance store not supported|✓|✗|✗|✗|
|hpc7g.16xlarge|✓|Instance store not supported|✓|✗|✗|✗|


### Specifications for Amazon EC2 previous generation instances

AWS offers previous generation instance types for users who have optimized their applications
around them and have yet to upgrade. We encourage you to use current generation instance
types to get the best performance, but we continue to support the following previous generation
instance types.

**Contents**

-  Available sizes

-  Platform summary

-  Performance specifications

-  Network specifications

-  Amazon EBS specifications

-  Instance store specifications

-  Security specifications

**Pricing**

Previous generation 357


-----

[For pricing information, see Amazon EC2 On-Demand Pricing.](https://aws.amazon.com/ec2/pricing/on-demand/)

#### Available sizes

|Instance type|Available sizes|
|---|---|
|A1|a1.medium | a1.large | a1.xlarge | a1.2xlarge | a1.4xlarge | a1.metal|
|C1|c1.medium | c1.xlarge|
|C3|c3.large | c3.xlarge | c3.2xlarge | c3.4xlarge | c3.8xlarge|
|C4|c4.large | c4.xlarge | c4.2xlarge | c4.4xlarge | c4.8xlarge|
|G3|g3.4xlarge | g3.8xlarge | g3.16xlarge|
|I2|i2.xlarge | i2.2xlarge | i2.4xlarge | i2.8xlarge|
|M1|m1.small | m1.medium | m1.large | m1.xlarge|
|M2|m2.xlarge | m2.2xlarge | m2.4xlarge|
|M3|m3.medium | m3.large | m3.xlarge | m3.2xlarge|
|M4|m4.large | m4.xlarge | m4.2xlarge | m4.4xlarge | m4.10xlarge | m4.16xlarge|
|R3|r3.large | r3.xlarge | r3.2xlarge | r3.4xlarge | r3.8xlarge|
|R4|r4.large | r4.xlarge | r4.2xlarge | r4.4xlarge | r4.8xlarge | r4.16xlarge|
|T1|t1.micro|



Available sizes 358


-----

#### Platform summary

|Instance type|Hypervi r|soP rocessor type (architec ture)|Metal instances available|Dedicate Hosts support|dS pot support|Hibernati on support|Support operatin systems|
|---|---|---|---|---|---|---|---|
|A1|Nitro v2|AWS Graviton (arm64)|✓|✓|✓|✗|Linux|
|C1|Xen|Intel (x86_64)|✗|✗|✓|✗|Window | Linux|
|C3|Xen|Intel (x86_64)|✗|✓|✓|✓|Window | Linux|
|C4|Xen|Intel (x86_64)|✗|✓|✓|✓|Window | Linux|
|G3|Xen|Intel (x86_64)|✗|✓|✓|✗|Window | Linux|
|I2|Xen|Intel (x86_64)|✗|✓|✓|✗|Window | Linux|
|M1|Xen|Intel (x86_64)|✗|✗|✓|✗|Window | Linux|
|M2|Xen|Intel (x86_64)|✗|✗|✓|✗|Window | Linux|
|M3|Xen|Intel (x86_64)|✗|✓|✓|✓|Window | Linux|
|M4|Xen|Intel (x86_64)|✗|✓|✓|✓|Window | Linux|



Platform summary 359


-----

**Instance**


**Hyperviso Processor**


**Metal**


**Dedicated Spot**


**Hibernati**


**Supported**


|type|r|type (architec ture)|instances available|Hosts support|support|on support|operatin systems|
|---|---|---|---|---|---|---|---|
|R3|Xen|Intel (x86_64)|✗|✓|✓|✓|Window | Linux|
|R4|Xen|Intel (x86_64)|✗|✓|✓|✓|Window | Linux|
|T1|Xen|Intel (i386)|✗|✗|✓|✗|Window | Linux|


#### Performance specifications

|Instance type|Burstabl|eMemor (GiB)|y Processor|vCPUs|CPU cores|Thread per core|s Accelerat ors|Acceler or memor|
|---|---|---|---|---|---|---|---|---|
|A1|||||||||
|a1.medium|✗|2.00|AWS Graviton Processor|1|1|1|✗|✗|
|a1.large|✗|4.00|AWS Graviton Processor|2|2|1|✗|✗|
|a1.xlarge|✗|8.00|AWS Graviton Processor|4|4|1|✗|✗|
|a1.2xlarge|✗|16.00|AWS Graviton Processor|8|8|1|✗|✗|
|a1.4xlarge|✗|32.00|AWS Graviton Processor|16|16|1|✗|✗|



Performance specifications 360


-----

**Instance**


**BurstableMemory**


**Processor** **vCPUs CPU**


**Threads Accelerat**


**Accelerat**

|type|Col2|(GiB)|Col4|Col5|cores|per core|ors|or memor|
|---|---|---|---|---|---|---|---|---|
|a1.metal|✗|32.00|AWS Graviton Processor|16|16|1|✗|✗|
|C1|||||||||
|c1.medium|✗|1.70|Intel Xeon Family|2|2|1|✗|✗|
|c1.xlarge|✗|7.00|Intel Xeon Family|8|8|1|✗|✗|
|C3|||||||||
|c3.large|✗|3.75|Intel Xeon E5-2680v2|2|1|2|✗|✗|
|c3.xlarge|✗|7.50|Intel Xeon E5-2680v2|4|2|2|✗|✗|
|c3.2xlarge|✗|15.00|Intel Xeon E5-2680v2|8|4|2|✗|✗|
|c3.4xlarge|✗|30.00|Intel Xeon E5-2680v2|16|8|2|✗|✗|
|c3.8xlarge|✗|60.00|Intel Xeon E5-2680v2|32|16|2|✗|✗|
|C4|||||||||
|c4.large|✗|3.75|Intel Xeon E5-2666v3|2|1|2|✗|✗|
|c4.xlarge|✗|7.50|Intel Xeon E5-2666v3|4|2|2|✗|✗|


Performance specifications 361


-----

**Instance**


**BurstableMemory**


**Processor** **vCPUs CPU**


**Threads Accelerat**


**Accelerat**

|type|Col2|(GiB)|Col4|Col5|cores|per core|ors|or memor|
|---|---|---|---|---|---|---|---|---|
|c4.2xlarge|✗|15.00|Intel Xeon E5-2666v3|8|4|2|✗|✗|
|c4.4xlarge|✗|30.00|Intel Xeon E5-2666v3|16|8|2|✗|✗|
|c4.8xlarge|✗|60.00|Intel Xeon E5-2666v3|36|18|2|✗|✗|
|G3|||||||||
|g3.4xlarge|✗|122.00|Intel Xeon E5-2686 v4|16|8|2|1 x NVIDIA M60 GPU|8 GiB (1 x 8 GiB)|
|g3.8xlarge|✗|244.00|Intel Xeon E5-2686 v4|32|16|2|2 x NVIDIA M60 GPU|16 GiB (2 x 8 GiB)|
|g3.16xlarge|✗|488.00|Intel Xeon E5-2686 v4|64|32|2|4 x NVIDIA M60 GPU|32 GiB (4 x 8 GiB)|
|I2|||||||||
|i2.xlarge|✗|30.50|Intel Xeon E5-2670v2|4|2|2|✗|✗|
|i2.2xlarge|✗|61.00|Intel Xeon E5-2670v2|8|4|2|✗|✗|
|i2.4xlarge|✗|122.00|Intel Xeon E5-2670v2|16|8|2|✗|✗|


Performance specifications 362


-----

**Instance**


**BurstableMemory**


**Processor** **vCPUs CPU**


**Threads Accelerat**


**Accelerat**

|type|Col2|(GiB)|Col4|Col5|cores|per core|ors|or memor|
|---|---|---|---|---|---|---|---|---|
|i2.8xlarge|✗|244.00|Intel Xeon E5-2670v2|32|16|2|✗|✗|
|M1|||||||||
|m1.small|✗|1.70|Intel Xeon Family|1|1|1|✗|✗|
|m1.medium|✗|3.70|Intel Xeon Family|1|1|1|✗|✗|
|m1.large|✗|7.50|Intel Xeon Family|2|2|1|✗|✗|
|m1.xlarge|✗|15.00|Intel Xeon Family|4|4|1|✗|✗|
|M2|||||||||
|m2.xlarge|✗|17.10|Intel Xeon Family|2|2|1|✗|✗|
|m2.2xlarge|✗|34.20|Intel Xeon Family|4|4|1|✗|✗|
|m2.4xlarge|✗|68.40|Intel Xeon Family|8|8|1|✗|✗|
|M3|||||||||
|m3.medium|✗|3.75|Intel Xeon E5-2670v2|1|1|1|✗|✗|
|m3.large|✗|7.50|Intel Xeon E5-2670v2|2|1|2|✗|✗|


Performance specifications 363


-----

**Instance**


**BurstableMemory**


**Processor** **vCPUs CPU**


**Threads Accelerat**


**Accelerat**

|type|Col2|(GiB)|Col4|Col5|cores|per core|ors|or memor|
|---|---|---|---|---|---|---|---|---|
|m3.xlarge|✗|15.00|Intel Xeon E5-2670v2|4|2|2|✗|✗|
|m3.2xlarge|✗|30.00|Intel Xeon E5-2670v2|8|4|2|✗|✗|
|M4|||||||||
|m4.large|✗|8.00|Intel Xeon E5-2676v3|2|1|2|✗|✗|
|m4.xlarge|✗|16.00|Intel Xeon E5-2676v3|4|2|2|✗|✗|
|m4.2xlarge|✗|32.00|Intel Xeon E5-2676v3|8|4|2|✗|✗|
|m4.4xlarge|✗|64.00|Intel Xeon E5-2676v3|16|8|2|✗|✗|
|m4.10xlarge|✗|160.00|Intel Xeon E5-2676v3|40|20|2|✗|✗|
|m4.16xlarge|✗|256.00|Intel Xeon E5-2686v4|64|32|2|✗|✗|
|R3|||||||||
|r3.large|✗|15.00|Intel Xeon E5-2670v2|2|1|2|✗|✗|
|r3.xlarge|✗|30.50|Intel Xeon E5-2670v2|4|2|2|✗|✗|
|r3.2xlarge|✗|61.00|Intel Xeon E5-2670v2|8|4|2|✗|✗|


Performance specifications 364


-----

**Instance**


**BurstableMemory**


**Processor** **vCPUs CPU**


**Threads Accelerat**


**Accelerat**

|type|Col2|(GiB)|Col4|Col5|cores|per core|ors|or memor|
|---|---|---|---|---|---|---|---|---|
|r3.4xlarge|✗|122.00|Intel Xeon E5-2670v2|16|8|2|✗|✗|
|r3.8xlarge|✗|244.00|Intel Xeon E5-2670v2|32|16|2|✗|✗|
|R4|||||||||
|r4.large|✗|15.25|Intel Broadwell E5-2686v4|2|1|2|✗|✗|
|r4.xlarge|✗|30.50|Intel Broadwell E5-2686v4|4|2|2|✗|✗|
|r4.2xlarge|✗|61.00|Intel Broadwell E5-2686v4|8|4|2|✗|✗|
|r4.4xlarge|✗|122.00|Intel Broadwell E5-2686v4|16|8|2|✗|✗|
|r4.8xlarge|✗|244.00|Intel Broadwell E5-2686v4|32|16|2|✗|✗|
|r4.16xlarge|✗|488.00|Intel Broadwell E5-2686v4|64|32|2|✗|✗|
|T1|||||||||
|t1.micro|✗|0.61|Intel E5-2650|1|1|1|✗|✗|


Performance specifications 365


-----

#### Network specifications

|Instance type|Baseline / Burst bandwidth (Gbps)|EFA|ENA|ENA Express|Network cards|Max. network interface s|IP addresses per interface|IPv6|
|---|---|---|---|---|---|---|---|---|
|A1|||||||||
|1 a1.medium|0.5 / 10.0|✗|✓|✗|1|2|4|✓|
|1 a1.large|0.75 / 10.0|✗|✓|✗|1|3|10|✓|
|1 a1.xlarge|1.25 / 10.0|✗|✓|✗|1|4|15|✓|
|1 a1.2xlarge|2.5 / 10.0|✗|✓|✗|1|4|15|✓|
|1 a1.4xlarge|5.0 / 10.0|✗|✓|✗|1|8|30|✓|
|1 a1.metal|5.0 / 10.0|✗|✓|✗|1|8|30|✓|
|C1|||||||||
|c1.medium|Moderate|✗|✗|✗|1|2|6|✗|
|c1.xlarge|High|✗|✗|✗|1|4|15|✗|
|C3|||||||||
|c3.large|Moderate|✗|2 ✗|✗|1|3|10|✓|
|c3.xlarge|Moderate|✗|2 ✗|✗|1|4|15|✓|
|c3.2xlarge|High|✗|2 ✗|✗|1|4|15|✓|
|c3.4xlarge|High|✗|2 ✗|✗|1|8|30|✓|
|c3.8xlarge|10 Gigabit|✗|2 ✗|✗|1|8|30|✓|
|C4|||||||||



Network specifications 366


-----

|Col1|bandwidth (Gbps)|Col3|Col4|Col5|Col6|interface s|per interface|Col9|
|---|---|---|---|---|---|---|---|---|
|c4.large|Moderate|✗|2 ✗|✗|1|3|10|✓|
|c4.xlarge|High|✗|2 ✗|✗|1|4|15|✓|
|c4.2xlarge|High|✗|2 ✗|✗|1|4|15|✓|
|c4.4xlarge|High|✗|2 ✗|✗|1|8|30|✓|
|c4.8xlarge|10 Gigabit|✗|2 ✗|✗|1|8|30|✓|
|G3|||||||||
|1 g3.4xlarge|Up to 10 Gigabit|✗|✓|✗|1|8|30|✓|
|g3.8xlarge|10 Gigabit|✗|✓|✗|1|8|30|✓|
|g3.16xlarge|25 Gigabit|✗|✓|✗|1|15|50|✓|
|I2|||||||||
|i2.xlarge|Moderate|✗|2 ✗|✗|1|4|15|✓|
|i2.2xlarge|High|✗|2 ✗|✗|1|4|15|✓|
|i2.4xlarge|High|✗|2 ✗|✗|1|8|30|✓|
|i2.8xlarge|10 Gigabit|✗|2 ✗|✗|1|8|30|✓|
|M1|||||||||
|m1.small|Low|✗|✗|✗|1|2|4|✗|
|m1.medium|Moderate|✗|✗|✗|1|2|6|✗|
|m1.large|Moderate|✗|✗|✗|1|3|10|✗|


**Instance type** **Baseline /** **EFA** **ENA** **ENA** **Network** **Max.** **IP** **IPv6**
**Burst** **Express** **cards** **network** **addresses**
**bandwidth** **interface** **per**
**(Gbps)** **s** **interface**


Network specifications 367


-----

|Col1|bandwidth (Gbps)|Col3|Col4|Col5|Col6|interface s|per interface|Col9|
|---|---|---|---|---|---|---|---|---|
|m1.xlarge|High|✗|✗|✗|1|4|15|✗|
|M2|||||||||
|m2.xlarge|Moderate|✗|✗|✗|1|4|15|✗|
|m2.2xlarge|Moderate|✗|✗|✗|1|4|30|✗|
|m2.4xlarge|High|✗|✗|✗|1|8|30|✗|
|M3|||||||||
|m3.medium|Moderate|✗|✗|✗|1|2|6|✗|
|m3.large|Moderate|✗|✗|✗|1|3|10|✗|
|m3.xlarge|High|✗|✗|✗|1|4|15|✗|
|m3.2xlarge|High|✗|✗|✗|1|4|30|✗|
|M4|||||||||
|m4.large|Moderate|✗|2 ✗|✗|1|2|10|✓|
|m4.xlarge|High|✗|2 ✗|✗|1|4|15|✓|
|m4.2xlarge|High|✗|2 ✗|✗|1|4|15|✓|
|m4.4xlarge|High|✗|2 ✗|✗|1|8|30|✓|
|m4.10xlarge|10 Gigabit|✗|2 ✗|✗|1|8|30|✓|
|m4.16xlarge|25 Gigabit|✗|✓|✗|1|8|30|✓|
|R3|||||||||
|r3.large|Moderate|✗|2 ✗|✗|1|3|10|✓|


**Instance type** **Baseline /** **EFA** **ENA** **ENA** **Network** **Max.** **IP** **IPv6**
**Burst** **Express** **cards** **network** **addresses**
**bandwidth** **interface** **per**
**(Gbps)** **s** **interface**


Network specifications 368


-----

|Col1|bandwidth (Gbps)|Col3|Col4|Col5|Col6|interface s|per interface|Col9|
|---|---|---|---|---|---|---|---|---|
|r3.xlarge|Moderate|✗|2 ✗|✗|1|4|15|✓|
|r3.2xlarge|High|✗|2 ✗|✗|1|4|15|✓|
|r3.4xlarge|High|✗|2 ✗|✗|1|8|30|✓|
|r3.8xlarge|10 Gigabit|✗|2 ✗|✗|1|8|30|✓|
|R4|||||||||
|1 r4.large|0.75 / 10.0|✗|✓|✗|1|3|10|✓|
|1 r4.xlarge|1.25 / 10.0|✗|✓|✗|1|4|15|✓|
|1 r4.2xlarge|2.5 / 10.0|✗|✓|✗|1|4|15|✓|
|1 r4.4xlarge|5.0 / 10.0|✗|✓|✗|1|8|30|✓|
|r4.8xlarge|10 Gigabit|✗|✓|✗|1|8|30|✓|
|r4.16xlarge|25 Gigabit|✗|✓|✗|1|15|50|✓|
|T1|||||||||
|t1.micro|Very Low|✗|✗|✗|1|2|2|✗|


**Instance type** **Baseline /** **EFA** **ENA** **ENA** **Network** **Max.** **IP** **IPv6**
**Burst** **Express** **cards** **network** **addresses**
**bandwidth** **interface** **per**
**(Gbps)** **s** **interface**


**Note**

1
These instances have a baseline bandwidth and can use a network I/O credit mechanism
to burst beyond their baseline bandwidth on a best effort basis. Other instances types
[can sustain their maximum performance indefinitely. For more information, see instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-network-bandwidth.html)
[network bandwidth.](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-network-bandwidth.html)
2
These instances support enhanced networking using the Intel 82599 VF interface.

Network specifications 369


-----

#### Amazon EBS specifications

The following table indicates which instance types are Amazon EBS optimized by default and
which optionally support it. It also describes their EBS-optimized performance, including dedicated
bandwidth to Amazon EBS, the typical maximum aggregate throughput that can be achieved on
that dedicated connection with a streaming read workload and 128 KiB I/O size, and the maximum
IOPS the instance type can support when using a 16 KiB I/O size. Instance types not listed do not
support Amazon EBS optimization.

**Important**

An instance's EBS performance is bounded by the instance's performance limits, or
the aggregated performance of its attached volumes, whichever is smaller. To achieve
maximum EBS performance, an instance must have attached volumes that provide a

combined performance equal to or greater than the maximum instance performance. For

example, to achieve 80,000 IOPS for r6i.16xlarge, the instance must have at least 5
```
   gp3 volumes provisioned with 16,000 IOPS each (5 volumes x 16,000 IOPS = 80,000

```
IOPS).
We recommand that you choose an EBS–optimized instance type that provides more
dedicated Amazon EBS throughput than your application needs; otherwise, the connection
between Amazon EBS and Amazon EC2 can become a performance bottleneck.

|Instance type|Baseline / Maximum bandwidth (Mbps)|Baseline / Maximum throughput (MB/s, 128 KiB I/O)|Baseline / Maximum IOPS (16 KiB I/O)|NVMe|EBS optimization 2|
|---|---|---|---|---|---|
|A1||||||
|1 a1.medium|300.00 / 3500.00|37.50 / 437.50|2500.00 / 20000.00|✓|default|
|1 a1.large|525.00 / 3500.00|65.62 / 437.50|4000.00 / 20000.00|✓|default|



Amazon EBS specifications 370


-----

**Instance**


**Baseline /**


**Baseline /**


**Baseline /**


**NVMe** **EBS**

|type|Maximum bandwidth (Mbps)|Maximum throughput (MB/s, 128 KiB I/O)|Maximum IOPS (16 KiB I/O)|Col5|optimization 2|
|---|---|---|---|---|---|
|1 a1.xlarge|800.00 / 3500.00|100.00 / 437.50|6000.00 / 20000.00|✓|default|
|1 a1.2xlarge|1750.00 / 3500.00|218.75 / 437.50|10000.00 / 20000.00|✓|default|
|a1.4xlarge|3500.00|437.50|20000.00|✓|default|
|a1.metal|3500.00|437.50|20000.00|✓|default|
|C1||||||
|c1.xlarge|1000.00|125.00|8000.00|✗|supported|
|C3||||||
|c3.xlarge|500.00|62.50|4000.00|✗|supported|
|c3.2xlarge|1000.00|125.00|8000.00|✗|supported|
|c3.4xlarge|2000.00|250.00|16000.00|✗|supported|
|C4||||||
|c4.large|500.00|62.50|4000.00|✗|default|
|c4.xlarge|750.00|93.75|6000.00|✗|default|
|c4.2xlarge|1000.00|125.00|8000.00|✗|default|
|c4.4xlarge|2000.00|250.00|16000.00|✗|default|
|c4.8xlarge|4000.00|500.00|32000.00|✗|default|
|G3||||||


Amazon EBS specifications 371


-----

**Instance**


**Baseline /**


**Baseline /**


**Baseline /**


**NVMe** **EBS**

|type|Maximum bandwidth (Mbps)|Maximum throughput (MB/s, 128 KiB I/O)|Maximum IOPS (16 KiB I/O)|Col5|optimization 2|
|---|---|---|---|---|---|
|g3.4xlarge|3500.00|437.50|20000.00|✗|default|
|g3.8xlarge|7000.00|875.00|40000.00|✗|default|
|g3.16xlarge|14000.00|1750.00|80000.00|✗|default|
|I2||||||
|i2.xlarge|500.00|62.50|4000.00|✗|supported|
|i2.2xlarge|1000.00|125.00|8000.00|✗|supported|
|i2.4xlarge|2000.00|250.00|16000.00|✗|supported|
|M1||||||
|m1.large|500.00|62.50|4000.00|✗|supported|
|m1.xlarge|1000.00|125.00|8000.00|✗|supported|
|M2||||||
|m2.2xlarge|500.00|62.50|4000.00|✗|supported|
|m2.4xlarge|1000.00|125.00|8000.00|✗|supported|
|M3||||||
|m3.xlarge|500.00|62.50|4000.00|✗|supported|
|m3.2xlarge|1000.00|125.00|8000.00|✗|supported|
|M4||||||
|m4.large|450.00|56.25|3600.00|✗|default|


Amazon EBS specifications 372


-----

**Instance**


**Baseline /**


**Baseline /**


**Baseline /**


**NVMe** **EBS**

|type|Maximum bandwidth (Mbps)|Maximum throughput (MB/s, 128 KiB I/O)|Maximum IOPS (16 KiB I/O)|Col5|optimization 2|
|---|---|---|---|---|---|
|m4.xlarge|750.00|93.75|6000.00|✗|default|
|m4.2xlarge|1000.00|125.00|8000.00|✗|default|
|m4.4xlarge|2000.00|250.00|16000.00|✗|default|
|m4.10xlarge|4000.00|500.00|32000.00|✗|default|
|m4.16xlarge|10000.00|1250.00|65000.00|✗|default|
|R3||||||
|r3.xlarge|500.00|62.50|4000.00|✗|supported|
|r3.2xlarge|1000.00|125.00|8000.00|✗|supported|
|r3.4xlarge|2000.00|250.00|16000.00|✗|supported|
|R4||||||
|r4.large|425.00|53.12|3000.00|✗|default|
|r4.xlarge|850.00|106.25|6000.00|✗|default|
|r4.2xlarge|1700.00|212.50|12000.00|✗|default|
|r4.4xlarge|3500.00|437.50|18750.00|✗|default|
|r4.8xlarge|7000.00|875.00|37500.00|✗|default|
|r4.16xlarge|14000.00|1750.00|75000.00|✗|default|
|T1||||||


Amazon EBS specifications 373


-----

**Note**

1
These instances can support maximum performance for 30 minutes at least once every 24
hours, after which they revert to their baseline performance. Other instances can sustain
the maximum performance indefinitely. If your workload requires sustained maximum
performance for longer than 30 minutes, use one of these instances.
2
```
   default indicates that instances are enabled for EBS optimization by default.
   supported indicates that instances can optionally be enabled for EBS optimization For

```
[more information, see Amazon EBS–optimized instances.](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-optimized.html)

#### Instance store specifications

|Instance type|Instance store volumes|Instance store type|100% random read IOPS / Write IOPS|Needs initializ 1 ation|TRIM support 2|
|---|---|---|---|---|---|
|C1||||||
|c1.medium|1 x 350 GB|HDD||✓||
|c1.xlarge|4 x 420 GB|HDD||✓||
|C3||||||
|c3.large|2 x 16 GB|SSD||✓||
|c3.xlarge|2 x 40 GB|SSD||✓||
|c3.2xlarge|2 x 80 GB|SSD||✓||
|c3.4xlarge|2 x 160 GB|SSD||✓||
|c3.8xlarge|2 x 320 GB|SSD||✓||
|I2||||||
|i2.xlarge|1 x 800 GB|SSD||✓||



Instance store specifications 374


-----

|Instance type|Instance store volumes|Instance store type|100% random read IOPS / Write IOPS|Needs initializ ation 1|TRIM support 2|
|---|---|---|---|---|---|
|i2.2xlarge|2 x 800 GB|SSD||✓||
|i2.4xlarge|4 x 800 GB|SSD||✓||
|i2.8xlarge|8 x 800 GB|SSD||✓||
|M1||||||
|m1.small|1 x 160 GB|HDD||✓||
|m1.medium|1 x 410 GB|HDD||✓||
|m1.large|2 x 420 GB|HDD||✓||
|m1.xlarge|4 x 420 GB|HDD||✓||
|M2||||||
|m2.xlarge|1 x 420 GB|HDD||✓||
|m2.2xlarge|1 x 850 GB|HDD||✓||
|m2.4xlarge|2 x 840 GB|HDD||✓||
|M3||||||
|m3.medium|1 x 4 GB|SSD||✓||
|m3.large|1 x 32 GB|SSD||✓||
|m3.xlarge|2 x 40 GB|SSD||✓||
|m3.2xlarge|2 x 80 GB|SSD||✓||
|R3||||||
|r3.large|1 x 32 GB|SSD||✓||


Instance store specifications 375


-----

|Instance type|Instance store volumes|Instance store type|100% random read IOPS / Write IOPS|Needs initializ ation 1|TRIM support 2|
|---|---|---|---|---|---|
|r3.xlarge|1 x 80 GB|SSD||✓||
|r3.2xlarge|1 x 160 GB|SSD||✓||
|r3.4xlarge|1 x 320 GB|SSD||✓||
|r3.8xlarge|2 x 320 GB|SSD||✓||


1
Volumes attached to certain instances suffer a first-write penalty unless initialized. For more
[information, see Optimize disk performance for instance store volumes.](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/disk-performance.html)

2
[For more information, see Instance store volume TRIM support.](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ssd-instance-store.html#InstanceStoreTrimSupport)

#### Security specifications

|Instance type|EBS encryptio n|Instance store encryptio n|Encryptio n in transit|AMD SEV-SNP|NitroTPM|Nitro Enclaves|
|---|---|---|---|---|---|---|
|A1|||||||
|a1.medium|✓|Instance store not supported|✗|✗|✗|✗|
|a1.large|✓|Instance store not supported|✗|✗|✗|✗|
|a1.xlarge|✓|Instance store not supported|✗|✗|✗|✗|



Security specifications 376


-----

|Instance type|EBS encryptio n|Instance store encryptio n|Encryptio n in transit|AMD SEV-SNP|NitroTPM|Nitro Enclaves|
|---|---|---|---|---|---|---|
|a1.2xlarge|✓|Instance store not supported|✗|✗|✗|✗|
|a1.4xlarge|✓|Instance store not supported|✗|✗|✗|✗|
|a1.metal|✓|Instance store not supported|✗|✗|✗|✗|
|C1|||||||
|c1.medium|✓|✗|✗|✗|✗|✗|
|c1.xlarge|✓|✗|✗|✗|✗|✗|
|C3|||||||
|c3.large|✓|✗|✗|✗|✗|✗|
|c3.xlarge|✓|✗|✗|✗|✗|✗|
|c3.2xlarge|✓|✗|✗|✗|✗|✗|
|c3.4xlarge|✓|✗|✗|✗|✗|✗|
|c3.8xlarge|✓|✗|✗|✗|✗|✗|
|C4|||||||
|c4.large|✓|Instance store not supported|✗|✗|✗|✗|


Security specifications 377


-----

|Instance type|EBS encryptio n|Instance store encryptio n|Encryptio n in transit|AMD SEV-SNP|NitroTPM|Nitro Enclaves|
|---|---|---|---|---|---|---|
|c4.xlarge|✓|Instance store not supported|✗|✗|✗|✗|
|c4.2xlarge|✓|Instance store not supported|✗|✗|✗|✗|
|c4.4xlarge|✓|Instance store not supported|✗|✗|✗|✗|
|c4.8xlarge|✓|Instance store not supported|✗|✗|✗|✗|
|G3|||||||
|g3.4xlarge|✓|Instance store not supported|✗|✗|✗|✗|
|g3.8xlarge|✓|Instance store not supported|✗|✗|✗|✗|
|g3.16xlarge|✓|Instance store not supported|✗|✗|✗|✗|
|I2|||||||
|i2.xlarge|✓|✗|✗|✗|✗|✗|


Security specifications 378


-----

|Instance type|EBS encryptio n|Instance store encryptio n|Encryptio n in transit|AMD SEV-SNP|NitroTPM|Nitro Enclaves|
|---|---|---|---|---|---|---|
|i2.2xlarge|✓|✗|✗|✗|✗|✗|
|i2.4xlarge|✓|✗|✗|✗|✗|✗|
|i2.8xlarge|✓|✗|✗|✗|✗|✗|
|M1|||||||
|m1.small|✓|✗|✗|✗|✗|✗|
|m1.medium|✓|✗|✗|✗|✗|✗|
|m1.large|✓|✗|✗|✗|✗|✗|
|m1.xlarge|✓|✗|✗|✗|✗|✗|
|M2|||||||
|m2.xlarge|✓|✗|✗|✗|✗|✗|
|m2.2xlarge|✓|✗|✗|✗|✗|✗|
|m2.4xlarge|✓|✗|✗|✗|✗|✗|
|M3|||||||
|m3.medium|✓|✗|✗|✗|✗|✗|
|m3.large|✓|✗|✗|✗|✗|✗|
|m3.xlarge|✓|✗|✗|✗|✗|✗|
|m3.2xlarge|✓|✗|✗|✗|✗|✗|
|M4|||||||


Security specifications 379


-----

|Instance type|EBS encryptio n|Instance store encryptio n|Encryptio n in transit|AMD SEV-SNP|NitroTPM|Nitro Enclaves|
|---|---|---|---|---|---|---|
|m4.large|✓|Instance store not supported|✗|✗|✗|✗|
|m4.xlarge|✓|Instance store not supported|✗|✗|✗|✗|
|m4.2xlarge|✓|Instance store not supported|✗|✗|✗|✗|
|m4.4xlarge|✓|Instance store not supported|✗|✗|✗|✗|
|m4.10xlarge|✓|Instance store not supported|✗|✗|✗|✗|
|m4.16xlarge|✓|Instance store not supported|✗|✗|✗|✗|
|R3|||||||
|r3.large|✓|✗|✗|✗|✗|✗|
|r3.xlarge|✓|✗|✗|✗|✗|✗|
|r3.2xlarge|✓|✗|✗|✗|✗|✗|
|r3.4xlarge|✓|✗|✗|✗|✗|✗|


Security specifications 380


-----

|Instance type|EBS encryptio n|Instance store encryptio n|Encryptio n in transit|AMD SEV-SNP|NitroTPM|Nitro Enclaves|
|---|---|---|---|---|---|---|
|r3.8xlarge|✓|✗|✗|✗|✗|✗|
|R4|||||||
|r4.large|✓|Instance store not supported|✗|✗|✗|✗|
|r4.xlarge|✓|Instance store not supported|✗|✗|✗|✗|
|r4.2xlarge|✓|Instance store not supported|✗|✗|✗|✗|
|r4.4xlarge|✓|Instance store not supported|✗|✗|✗|✗|
|r4.8xlarge|✓|Instance store not supported|✗|✗|✗|✗|
|r4.16xlarge|✓|Instance store not supported|✗|✗|✗|✗|
|T1|||||||
|t1.micro|✓|Instance store not supported|✗|✗|✗|✗|


Security specifications 381


-----

## Amazon EC2 instance types by Region

An Amazon EC2 instance is tied to the zone in which it was launched. The ID of an instance is tied
to the Region for the instance, and can only be used in this Region.

When you create your AWS account, we set default quotas on these resources on a per-Region
basis. We monitor your usage within each Region and raise your quotas automatically based on
your use of Amazon EC2. For more information, see Quotas.

Each Region supports a subset of the available instance types.

### US East (Ohio) — us-east-2

The following instance types are available in US East (Ohio).

-  General Purpose: A1 | M4 | M5 | M5a | M5ad | M5d | M5dn | M5n | M5zn | M6a | M6g | M6gd | M6i

| M6id | M6idn | M6in | M7a | M7g | M7gd | M7i | M7i-flex | Mac1 | Mac2 | Mac2-m2 | Mac2-m2pro
| T2 | T3 | T3a | T4g

-  Compute Optimized: C4 | C5 | C5a | C5ad | C5d | C5n | C6a | C6g | C6gd | C6gn | C6i | C6id | C6in |

C7a | C7g | C7gd | C7gn | C7i | C7i-flex

-  Memory Optimized: R3 | R4 | R5 | R5a | R5ad | R5b | R5d | R5dn | R5n | R6a | R6g | R6gd | R6i |

R6idn | R6in | R6id | R7a | R7g | R7gd | R7i | R7iz | R8g | U-3tb1 | U-6tb1 | U-9tb1 | U-12tb1 | X1 |
X2gd | X2idn | X2iedn | X1e | z1d

-  Storage Optimized: D2 | D3 | H1 | I2 | I3 | I3en | I4g | I4i | Im4gn | Is4gen

-  Accelerated Computing: G3 | G4ad | G4dn | G5 | G6 | Gr6 | Inf1 | Inf2 | P2 | P3 | P4d | P5 | Trn1 |

Trn1n

-  High Performance Computing: Hpc6a | Hpc6id | Hpc7a

-  Previous Generation: A1 | C4 | G3 | I2 | M4 | R3 | R4

### US East (N. Virginia) — us-east-1

The following instance types are available in US East (N. Virginia).

-  General Purpose: A1 | M1 | M2 | M3 | M4 | M5 | M5a | M5ad | M5d | M5dn | M5n | M5zn | M6a |

M6g | M6gd | M6i | M6id | M6idn | M6in | M7a | M7g | M7gd | M7i | M7i-flex | Mac1 | Mac2 | Mac2m1ultra | Mac2-m2 | Mac2-m2pro | T1 | T2 | T3 | T3a | T4g

US East (Ohio) 382


-----

-  Compute Optimized: C1 | C3 | C4 | C5 | C5a | C5ad | C5d | C5n | C6a | C6g | C6gd | C6gn | C6i |

C6id | C6in | C7a | C7g | C7gd | C7gn | C7i

-  Memory Optimized: R3 | R4 | R5 | R5a | R5ad | R5b | R5d | R5dn | R5n | R6a | R6g | R6gd | R6i

| R6idn | R6in | R6id | R7a | R7g | R7gd | R7i | R7iz | R8g | U-3tb1 | U-6tb1 | U-9tb1 | U-12tb1 |
U-18tb1 | U-24tb1 | U7i-12tb | U7in-16tb | U7in-24tb | U7in-32tb | X1 | X2gd | X2idn | X2iedn |
X2iezn | X1e | z1d

-  Storage Optimized: D2 | D3 | D3en | H1 | I2 | I3 | I3en | I4g | I4i | Im4gn | Is4gen

-  Accelerated Computing: DL1 | F1 | G3 | G4ad | G4dn | G5 | G5g | G6 | Gr6 | Inf1 | Inf2 | P2 | P3 |

P3dn | P4d | P5 | Trn1 | Trn1n | VT1

-  High Performance Computing: Hpc7g

-  Previous Generation: A1 | C1 | C3 | C4 | G3 | I2 | M1 | M2 | M3 | M4 | R3 | R4 | T1

### US West (N. California) — us-west-1

The following instance types are available in US West (N. California).

-  General Purpose: M1 | M2 | M3 | M4 | M5 | M5a | M5ad | M5d | M5zn | M6a | M6g | M6gd | M6i |

M6idn | M6in | M7g | M7gd | M7i | M7i-flex | T1 | T2 | T3 | T3a | T4g

-  Compute Optimized: C1 | C3 | C4 | C5 | C5a | C5d | C5n | C6a | C6g | C6gd | C6gn | C6i | C6in |

C7g | C7gd | C7i | C7i-flex

-  Memory Optimized: R3 | R4 | R5 | R5a | R5ad | R5d | R5n | R6a | R6g | R6gd | R6i | R7g | R7gd |

R7i | X2idn | X2iedn | z1d

-  Storage Optimized: D2 | I2 | I3 | I3en | I4i

-  Accelerated Computing: G3 | G4dn | Inf1

-  Previous Generation: C1 | C3 | C4 | G3 | I2 | M1 | M2 | M3 | M4 | R3 | R4 | T1

### US West (Oregon) — us-west-2

The following instance types are available in US West (Oregon).

-  General Purpose: A1 | M1 | M2 | M3 | M4 | M5 | M5a | M5ad | M5d | M5dn | M5n | M5zn | M6a |

M6g | M6gd | M6i | M6id | M6idn | M6in | M7a | M7g | M7gd | M7i | M7i-flex | Mac1 | Mac2 | Mac2m1ultra | Mac2-m2 | Mac2-m2pro | T1 | T2 | T3 | T3a | T4g

US West (N. California) 383


-----

-  Compute Optimized: C1 | C3 | C4 | C5 | C5a | C5ad | C5d | C5n | C6a | C6g | C6gd | C6gn | C6i |

C6id | C6in | C7a | C7g | C7gd | C7gn | C7i

-  Memory Optimized: R3 | R4 | R5 | R5a | R5ad | R5b | R5d | R5dn | R5n | R6a | R6g | R6gd | R6i

| R6idn | R6in | R6id | R7a | R7g | R7gd | R7i | R7iz | R8g | U-3tb1 | U-6tb1 | U-9tb1 | U-12tb1 |

U-18tb1 | U-24tb1 | U7i-12tb | U7in-16tb | U7in-24tb | U7in-32tb | X1 | X2gd | X2idn | X2iedn |
X2iezn | X1e | z1d

-  Storage Optimized: D2 | D3 | D3en | H1 | I2 | I3 | I3en | I4g | I4i | Im4gn | Is4gen

-  Accelerated Computing: DL1 | DL2q | F1 | G3 | G4ad | G4dn | G5 | G5g | G6 | Gr6 | Inf1 | Inf2 | P2

| P3 | P3dn | P4d | P5 | Trn1 | Trn1n | VT1

-  Previous Generation: A1 | C1 | C3 | C4 | G3 | I2 | M1 | M2 | M3 | M4 | R3 | R4 | T1

### Africa (Cape Town) — af-south-1

The following instance types are available in Africa (Cape Town).

-  General Purpose: M5 | M5d | M6g | M6gd | M6i | T3 | T4g

-  Compute Optimized: C5 | C5a | C5ad | C5d | C5n | C6g | C6i | C6in

-  Memory Optimized: R5 | R5d | R5dn | R5n | R6g | R6i | X1 | X2idn | X2iedn | X1e

-  Storage Optimized: D2 | I3 | I3en | I4i

-  Accelerated Computing: G4dn | Inf1

### Asia Pacific (Hong Kong) — ap-east-1

The following instance types are available in Asia Pacific (Hong Kong).

-  General Purpose: M5 | M5d | M6g | M6gd | M6i | T3 | T4g

-  Compute Optimized: C5 | C5a | C5d | C5n | C6a | C6g | C6gn | C6i | C6in | C7g

-  Memory Optimized: R5 | R5d | R5n | R6g | R6i | R7g | U-3tb1 | X1

-  Storage Optimized: D2 | I3 | I3en | I4i

-  Accelerated Computing: G4dn | Inf1

### Asia Pacific (Hyderabad) — ap-south-2

The following instance types are available in Asia Pacific (Hyderabad).

Africa (Cape Town) 384


-----

-  General Purpose: M5 | M5d | M6a | M6g | M6gd | M6i | M7g | T3 | T4g

-  Compute Optimized: C5 | C5d | C6g | C6i | C6in | C7g

-  Memory Optimized: R5 | R5d | R6g | R6i | R7g | U-9tb1 | X2idn | X2iedn

-  Storage Optimized: I3 | I3en | I4i

### Asia Pacific (Jakarta) — ap-southeast-3

The following instance types are available in Asia Pacific (Jakarta).

-  General Purpose: M5 | M5d | M6g | M6gd | M6i | T3 | T4g

-  Compute Optimized: C5 | C5d | C5n | C6g | C6gd | C6gn | C6in

-  Memory Optimized: R5 | R5d | R6g | R6gd | R7i | U-6tb1 | X2idn | X2iedn

-  Storage Optimized: I3 | I3en | I4i

-  Accelerated Computing: G5

### Asia Pacific (Melbourne) — ap-southeast-4

The following instance types are available in Asia Pacific (Melbourne).

-  General Purpose: M5 | M5d | M6g | M6gd | T3 | T4g

-  Compute Optimized: C5 | C5d | C6g | C6in

-  Memory Optimized: R5 | R5d | R6g

-  Storage Optimized: I3 | I3en | I4i

### Asia Pacific (Mumbai) — ap-south-1

The following instance types are available in Asia Pacific (Mumbai).

-  General Purpose: A1 | M4 | M5 | M5a | M5ad | M5d | M6a | M6g | M6gd | M6i | M6id | M6idn |

M6in | M7g | M7gd | M7i | M7i-flex | Mac1 | T2 | T3 | T3a | T4g

-  Compute Optimized: C4 | C5 | C5a | C5d | C5n | C6a | C6g | C6gd | C6gn | C6i | C6in | C7g | C7gd |

C7i | C7i-flex

-  Memory Optimized: R3 | R4 | R5 | R5a | R5ad | R5d | R5n | R6a | R6g | R6gd | R6i | R6id | R7g |

R7gd | R7i | U-6tb1 | U-12tb1 | X1 | X2idn | X2iedn | X1e | z1d

Asia Pacific (Jakarta) 385


-----

-  Storage Optimized: D2 | D3 | I2 | I3 | I3en | I4i | Is4gen

-  Accelerated Computing: G4dn | G5 | Inf1 | Inf2 | P2

-  Previous Generation: A1 | C4 | I2 | M4 | R3 | R4

### Asia Pacific (Osaka) — ap-northeast-3

The following instance types are available in Asia Pacific (Osaka).

-  General Purpose: M4 | M5 | M5d | M6g | M6gd | M6i | T2 | T3 | T4g

-  Compute Optimized: C4 | C5 | C5d | C5n | C6g | C6gd | C6gn | C6i

-  Memory Optimized: R4 | R5 | R5d | R6g | R6gd | R6i | X1 | X2idn | X2iedn | X1e

-  Storage Optimized: D2 | I3 | I3en | I4i

-  Accelerated Computing: G4dn

-  Previous Generation: C4 | M4 | R4

### Asia Pacific (Seoul) — ap-northeast-2

The following instance types are available in Asia Pacific (Seoul).

-  General Purpose: M4 | M5 | M5a | M5ad | M5d | M5zn | M6g | M6gd | M6i | M6id | M7g | M7i |

M7i-flex | Mac1 | T2 | T3 | T3a | T4g

-  Compute Optimized: C4 | C5 | C5a | C5d | C5n | C6g | C6gd | C6gn | C6i | C6id | C6in | C7g | C7i

-  Memory Optimized: R3 | R4 | R5 | R5a | R5ad | R5b | R5d | R5dn | R5n | R6g | R6gd | R6i | R6id |

R7g | R7i | U-6tb1 | U-9tb1 | U-12tb1 | U-24tb1 | U7in-16tb | X1 | X2idn | X2iedn | X1e | z1d

-  Storage Optimized: D2 | I2 | I3 | I3en | I4i

-  Accelerated Computing: G3 | G4dn | G5 | G5g | Inf1 | P2 | P3 | P4d

-  Previous Generation: C4 | G3 | I2 | M4 | R3 | R4

### Asia Pacific (Singapore) — ap-southeast-1

The following instance types are available in Asia Pacific (Singapore).

Asia Pacific (Osaka) 386


-----

-  General Purpose: A1 | M1 | M2 | M3 | M4 | M5 | M5a | M5ad | M5d | M5dn | M5n | M5zn | M6a |

M6g | M6gd | M6i | M6id | M6idn | M6in | M7g | M7gd | M7i | M7i-flex | Mac1 | Mac2 | T1 | T2 | T3 |
T3a | T4g

-  Compute Optimized: C1 | C3 | C4 | C5 | C5a | C5ad | C5d | C5n | C6a | C6g | C6gd | C6gn | C6i |

C6id | C6in | C7g | C7gd | C7i | C7i-flex

-  Memory Optimized: R3 | R4 | R5 | R5a | R5ad | R5b | R5d | R5dn | R5n | R6a | R6g | R6gd | R6i |

R6idn | R6in | R6id | R7g | R7gd | R7i | U-3tb1 | U-6tb1 | U-9tb1 | U-12tb1 | X1 | X2idn | X2iedn |
X1e | z1d

-  Storage Optimized: D2 | D3 | D3en | I2 | I3 | I3en | I4g | I4i | Im4gn | Is4gen

-  Accelerated Computing: G3 | G4dn | G5g | Inf1 | Inf2 | P2 | P3

-  High Performance Computing: Hpc6a

-  Previous Generation: A1 | C1 | C3 | C4 | G3 | I2 | M1 | M2 | M3 | M4 | R3 | R4 | T1

### Asia Pacific (Sydney) — ap-southeast-2

The following instance types are available in Asia Pacific (Sydney).

-  General Purpose: A1 | M1 | M2 | M3 | M4 | M5 | M5a | M5ad | M5d | M5zn | M6a | M6g | M6gd |

M6i | M6id | M6idn | M6in | M7g | M7gd | M7i | M7i-flex | Mac1 | Mac2-m2 | Mac2-m2pro | T1 | T2
| T3 | T3a | T4g

-  Compute Optimized: C1 | C3 | C4 | C5 | C5a | C5ad | C5d | C5n | C6a | C6g | C6gd | C6gn | C6i |

C6id | C6in | C7g | C7gd | C7i | C7i-flex

-  Memory Optimized: R3 | R4 | R5 | R5a | R5ad | R5b | R5d | R5dn | R5n | R6a | R6g | R6gd | R6i |

R6id | R7g | R7gd | R7i | U-3tb1 | U-6tb1 | U-12tb1 | U7in-16tb | X1 | X2idn | X2iedn | X1e | z1d

-  Storage Optimized: D2 | D3 | I2 | I3 | I3en | I4i | Im4gn | Is4gen

-  Accelerated Computing: F1 | G3 | G4dn | G5 | Inf1 | Inf2 | P2 | P3

-  High Performance Computing: Hpc6a

-  Previous Generation: A1 | C1 | C3 | C4 | G3 | I2 | M1 | M2 | M3 | M4 | R3 | R4 | T1

### Asia Pacific (Tokyo) — ap-northeast-1

The following instance types are available in Asia Pacific (Tokyo).

Asia Pacific (Sydney) 387


-----

-  General Purpose: A1 | M1 | M2 | M3 | M4 | M5 | M5a | M5ad | M5d | M5dn | M5n | M5zn | M6a |

M6g | M6gd | M6i | M6id | M6idn | M6in | M7a | M7g | M7gd | M7i | M7i-flex | Mac1 | T1 | T2 | T3 |
T3a | T4g

-  Compute Optimized: C1 | C3 | C4 | C5 | C5a | C5d | C5n | C6a | C6g | C6gd | C6gn | C6i | C6id |

C6in | C7a | C7g | C7gd | C7gn | C7i | C7i-flex

-  Memory Optimized: R3 | R4 | R5 | R5a | R5ad | R5b | R5d | R5dn | R5n | R6a | R6g | R6gd | R6i |

R6idn | R6in | R6id | R7a | R7g | R7gd | R7i | R7iz | U-3tb1 | U-6tb1 | U-9tb1 | U-12tb1 | X1 | X2idn
| X2iedn | X2iezn | X1e | z1d

-  Storage Optimized: D2 | D3 | D3en | I2 | I3 | I3en | I4i | Im4gn | Is4gen

-  Accelerated Computing: G3 | G4ad | G4dn | G5 | G5g | Inf1 | Inf2 | P2 | P3 | P3dn | P4d | VT1

-  High Performance Computing: Hpc7g

-  Previous Generation: A1 | C1 | C3 | C4 | G3 | I2 | M1 | M2 | M3 | M4 | R3 | R4 | T1

### Canada (Central) — ca-central-1

The following instance types are available in Canada (Central).

-  General Purpose: M4 | M5 | M5a | M5ad | M5d | M6a | M6g | M6gd | M6i | M6id | M6idn | M6in |

M7g | M7i | M7i-flex | T2 | T3 | T3a | T4g

-  Compute Optimized: C4 | C5 | C5a | C5d | C5n | C6a | C6g | C6gd | C6gn | C6i | C6id | C6in | C7g |

C7i | C7i-flex

-  Memory Optimized: R4 | R5 | R5a | R5ad | R5b | R5d | R5n | R6g | R6gd | R6i | R7g | R7i | U-3tb1 |

U-6tb1 | X1 | X2idn | X2iedn | X1e

-  Storage Optimized: D2 | D3 | I3 | I3en | I4g | I4i | Im4gn | Is4gen

-  Accelerated Computing: G3 | G4ad | G4dn | G5 | Inf1 | P3

-  Previous Generation: C4 | G3 | M4 | R4

### Canada West (Calgary) — ca-west-1

The following instance types are available in Canada West (Calgary).

-  General Purpose: M5 | M5d | M6g | M6gd | M6i | M6id | T3 | T4g

-  Compute Optimized: C5 | C6g | C6gn | C6i | C6id

-  Memory Optimized: R5 | R6g | R6i | R6id

Canada (Central) 388


-----

-  Storage Optimized: I3en | I4i

### Europe (Frankfurt) — eu-central-1

The following instance types are available in Europe (Frankfurt).

-  General Purpose: A1 | M3 | M4 | M5 | M5a | M5ad | M5d | M5dn | M5n | M5zn | M6a | M6g | M6gd

| M6i | M6id | M6idn | M6in | M7a | M7g | M7gd | M7i | M7i-flex | Mac1 | Mac2-m2 | T2 | T3 | T3a |
T4g

-  Compute Optimized: C3 | C4 | C5 | C5a | C5ad | C5d | C5n | C6a | C6g | C6gd | C6gn | C6i | C6id |

C6in | C7a | C7g | C7gd | C7i

-  Memory Optimized: R3 | R4 | R5 | R5a | R5ad | R5b | R5d | R5dn | R5n | R6a | R6g | R6gd | R6i |

R6idn | R6in | R6id | R7a | R7g | R7gd | R7i | R7iz | R8g | U-3tb1 | U-6tb1 | U-9tb1 | U-12tb1 | X1 |
X2idn | X2iedn | X1e | z1d

-  Storage Optimized: D2 | D3 | D3en | I2 | I3 | I3en | I4i | Im4gn | Is4gen

-  Accelerated Computing: DL2q | F1 | G3 | G4ad | G4dn | G5 | G5g | Inf1 | Inf2 | P2 | P3 | P4d

-  Previous Generation: A1 | C3 | C4 | G3 | I2 | M3 | M4 | R3 | R4

### Europe (Ireland) — eu-west-1

The following instance types are available in Europe (Ireland).

-  General Purpose: A1 | M1 | M2 | M3 | M4 | M5 | M5a | M5ad | M5d | M5dn | M5n | M5zn | M6a |

M6g | M6gd | M6i | M6id | M6idn | M6in | M7a | M7g | M7gd | M7i | M7i-flex | Mac1 | Mac2 | T1 |
T2 | T3 | T3a | T4g

-  Compute Optimized: C1 | C3 | C4 | C5 | C5a | C5ad | C5d | C5n | C6a | C6g | C6gd | C6gn | C6i |

C6id | C6in | C7a | C7g | C7gd | C7gn | C7i | C7i-flex

-  Memory Optimized: R3 | R4 | R5 | R5a | R5ad | R5b | R5d | R5dn | R5n | R6a | R6g | R6gd | R6i |

R6idn | R6in | R6id | R7a | R7g | R7gd | R7i | R7iz | U-3tb1 | U-6tb1 | U-9tb1 | U-12tb1 | U-18tb1 |
X1 | X2gd | X2idn | X2iedn | X2iezn | X1e | z1d

-  Storage Optimized: D2 | D3 | D3en | H1 | I2 | I3 | I3en | I4g | I4i | Im4gn | Is4gen

-  Accelerated Computing: F1 | G3 | G4ad | G4dn | G5 | Inf1 | Inf2 | P2 | P3 | P3dn | P4d | VT1

-  High Performance Computing: Hpc7a | Hpc7g

-  Previous Generation: A1 | C1 | C3 | C4 | G3 | I2 | M1 | M2 | M3 | M4 | R3 | R4 | T1

Europe (Frankfurt) 389


-----

### Europe (London) — eu-west-2

The following instance types are available in Europe (London).

-  General Purpose: M4 | M5 | M5a | M5ad | M5d | M6a | M6g | M6gd | M6i | M6id | M7g | M7i | M7i
flex | Mac1 | T2 | T3 | T3a | T4g

-  Compute Optimized: C4 | C5 | C5a | C5d | C5n | C6a | C6g | C6gd | C6gn | C6i | C6id | C6in | C7g |

C7i | C7i-flex

-  Memory Optimized: R4 | R5 | R5a | R5ad | R5b | R5d | R5n | R6g | R6gd | R6i | R6id | R7g | R7i |

U-6tb1 | U-9tb1 | X1 | X2idn | X2iedn | z1d

-  Storage Optimized: D2 | D3 | I3 | I3en | I4i | Im4gn | Is4gen

-  Accelerated Computing: F1 | G3 | G4ad | G4dn | G5 | Inf1 | Inf2 | P3

-  Previous Generation: C4 | G3 | M4 | R4

### Europe (Milan) — eu-south-1

The following instance types are available in Europe (Milan).

-  General Purpose: M5 | M5a | M5d | M6a | M6g | M6gd | M6i | T3 | T3a | T4g

-  Compute Optimized: C5 | C5a | C5ad | C5d | C5n | C6g | C6gn | C6i | C6in | C7g

-  Memory Optimized: R5 | R5a | R5b | R5d | R5dn | R5n | R6g | R6i | R7g | U-3tb1 | U-6tb1 |

U-12tb1 | X2idn | X2iedn

-  Storage Optimized: D2 | I3 | I3en | I4i

-  Accelerated Computing: G4dn | Inf1

### Europe (Paris) — eu-west-3

The following instance types are available in Europe (Paris).

-  General Purpose: M5 | M5a | M5ad | M5d | M6g | M6gd | M6i | M7g | M7gd | M7i | M7i-flex | T2 |

T3 | T3a | T4g

-  Compute Optimized: C5 | C5a | C5d | C5n | C6g | C6gd | C6gn | C6i | C6in | C7i | C7i-flex

-  Memory Optimized: R4 | R5 | R5a | R5ad | R5d | R5dn | R5n | R6g | R6gd | R6i | R7i | U-6tb1 | X1 |

X2idn | X2iedn

Europe (London) 390


-----

-  Storage Optimized: D2 | D3 | I3 | I3en | I4i | Im4gn | Is4gen

-  Accelerated Computing: G4dn | Inf1 | Inf2

-  Previous Generation: R4

### Europe (Spain) — eu-south-2

The following instance types are available in Europe (Spain).

-  General Purpose: M5 | M5d | M6g | M6gd | M6idn | M6in | M7a | M7g | M7gd | M7i | M7i-flex | T3

| T4g

-  Compute Optimized: C5 | C5d | C6g | C6in | C7a | C7g | C7gd | C7i | C7i-flex

-  Memory Optimized: R5 | R5d | R6g | R7a | R7g | R7gd | R7i | U-6tb1 | X2idn | X2iedn

-  Storage Optimized: I3 | I3en

-  Accelerated Computing: G5g

### Europe (Stockholm) — eu-north-1

The following instance types are available in Europe (Stockholm).

-  General Purpose: M5 | M5d | M6g | M6gd | M6i | M6idn | M6in | M7a | M7g | M7gd | M7i | M7i-flex

| Mac1 | T3 | T4g

-  Compute Optimized: C5 | C5a | C5d | C5n | C6g | C6gd | C6gn | C6i | C6in | C7a | C7g | C7gd | C7i |

C7i-flex

-  Memory Optimized: R5 | R5b | R5d | R5dn | R5n | R6g | R6gd | R6i | R6idn | R6in | R7a | R7g |

R7gd | R7i | U-6tb1 | U-9tb1 | X2idn | X2iedn

-  Storage Optimized: D2 | I3 | I3en | I4i

-  Accelerated Computing: G4dn | G5 | Inf1 | Inf2 | P5

-  High Performance Computing: Hpc6a | Hpc6id | Hpc7a

### Europe (Zurich) — eu-central-2

The following instance types are available in Europe (Zurich).

-  General Purpose: M5 | M5d | M6g | M6gd | M6i | M6id | T3 | T4g

Europe (Spain) 391


-----

-  Compute Optimized: C5 | C5d | C6g | C6gd | C6in

-  Memory Optimized: R5 | R5d | R6g | R6gd | R6i | U-6tb1 | X2idn

-  Storage Optimized: D3 | I3 | I3en | I4i

### Israel (Tel Aviv) — il-central-1

The following instance types are available in Israel (Tel Aviv).

-  General Purpose: M5 | M5d | M6g | M6gd | M6i | M6id | T3 | T3a | T4g

-  Compute Optimized: C5 | C5d | C6g | C6gn | C6i | C6id | C6in

-  Memory Optimized: R5 | R5d | R6g | R6i | R6id

-  Storage Optimized: D3 | I3 | I3en | I4i

-  Accelerated Computing: G5 | P4de

### Middle East (Bahrain) — me-south-1

The following instance types are available in Middle East (Bahrain).

-  General Purpose: M5 | M5d | M6g | M6gd | M6i | M7g | T3 | T4g

-  Compute Optimized: C5 | C5a | C5ad | C5d | C5n | C6g | C6gn | C6i | C6in

-  Memory Optimized: R5 | R5d | R6g | R6i

-  Storage Optimized: D2 | I3 | I3en | I4i

-  Accelerated Computing: G4dn | Inf1

### Middle East (UAE) — me-central-1

The following instance types are available in Middle East (UAE).

-  General Purpose: M5 | M5d | M6g | M6gd | M6i | T3 | T4g

-  Compute Optimized: C5 | C5d | C6g | C6in

-  Memory Optimized: R5 | R5d | R6g | R6i | X2idn

-  Storage Optimized: I3 | I3en | I4i

-  Accelerated Computing: G5

Israel (Tel Aviv) 392


-----

### South America (São Paulo) — sa-east-1

The following instance types are available in South America (São Paulo).

-  General Purpose: M1 | M2 | M3 | M4 | M5 | M5a | M5ad | M5d | M5zn | M6a | M6g | M6gd | M6i |

M6id | M7g | M7gd | M7i | M7i-flex | T1 | T2 | T3 | T3a | T4g

-  Compute Optimized: C1 | C3 | C4 | C5 | C5a | C5ad | C5d | C5n | C6a | C6g | C6gd | C6gn | C6i |

C6id | C6in | C7g | C7i | C7i-flex

-  Memory Optimized: R3 | R4 | R5 | R5a | R5ad | R5b | R5d | R5n | R6g | R6gd | R6i | R7g | R7i |

U-3tb1 | U-6tb1 | U-12tb1 | X1 | X2idn | X2iedn | X1e

-  Storage Optimized: I3 | I3en | I4i

-  Accelerated Computing: G4dn | G5 | Inf1 | Inf2

-  Previous Generation: C1 | C3 | C4 | M1 | M2 | M3 | M4 | R3 | R4 | T1

### AWS GovCloud (US-East) — us-gov-east-1

The following instance types are available in AWS GovCloud (US-East).

-  General Purpose: M5 | M5a | M5d | M5dn | M5n | M6g | M6gd | M6i | T3 | T3a | T4g

-  Compute Optimized: C5 | C5a | C5d | C5n | C6g | C6gd | C6gn | C6i | C6in

-  Memory Optimized: R5 | R5a | R5d | R5dn | R5n | R6g | R6gd | R6i | R7i | U-6tb1 | U-9tb1 |

U-24tb1 | X1 | X2idn | X2iedn

-  Storage Optimized: I3 | I3en | I4i

-  Accelerated Computing: G4dn | Inf1 | P3dn

### AWS GovCloud (US-West) — us-gov-west-1

The following instance types are available in AWS GovCloud (US-West).

-  General Purpose: M5 | M5a | M5ad | M5d | M5dn | M5n | M6g | M6gd | M6i | M6id | M6idn | M6in |

T2 | T3 | T3a | T4g

-  Compute Optimized: C5 | C5a | C5d | C5n | C6g | C6gd | C6gn | C6i | C6id | C6in

-  Memory Optimized: R5 | R5a | R5ad | R5d | R5dn | R5n | R6g | R6gd | R6i | R6id | R6idn | R6in |

R7i | U-3tb1 | U-6tb1 | U-9tb1 | U-12tb1 | U-24tb1 | X1 | X1e | X2idn | X2iedn

South America (São Paulo) 393


-----

-  Storage Optimized: D3 | I3 | I3en | I4i

-  Accelerated Computing: F1 | G4dn | Inf1 | P2 | P3 | P3dn | P4d

-  High Performance Computing: Hpc6a | Hpc6id | Hpc7a | Hpc7g

-  Previous Generation: C4 | G3 | M4 | R4

AWS GovCloud (US-West) 394


-----

## Instances built on the AWS Nitro System

The Nitro System is a collection of hardware and software components built by AWS that enable
high performance, high availability, and high security.

The Nitro System provides bare metal capabilities that eliminate virtualization overhead and
support workloads that require full access to host hardware. Bare metal instances are well suited
for the following:

-  Workloads that require access to low-level hardware features (for example, Intel VT) that are not

available or fully supported in virtualized environments

-  Applications that require a non-virtualized environment for licensing or support

### Nitro components

The following components are part of the Nitro System:

-  Nitro card

-  Local NVMe storage volumes

-  Networking hardware support

-  Management

-  Monitoring

-  Security

-  Nitro security chip, integrated into the motherboard

-  Nitro hypervisor - A lightweight hypervisor that manages memory and CPU allocation and

delivers performance that is indistinguishable from bare metal for most workloads.

[For more information, see AWS Nitro System.](https://aws.amazon.com/ec2/nitro/)

### Network feature support

The following content summarizes key networking capabilities for each version of the Nitro
System. Versions are shown in descending version release order. If you know the instance type
family that your instance belongs to, you can expand the Specifications section and select your

Nitro components 395


-----

instance family. The Platform summary table for your instance family shows the Nitro version for
your instance type in the Hypervisor column.

If you're not sure which instance family applies, see the Naming conventions section.

**Note**

Features are cumulative, meaning that newer versions of the Nitro system support the
features that are listed in all prior versions, except where explicitly stated otherwise.
See the Nitro instance requirements section for the minimum ENA driver and Linux kernel
versions for optimal performance of Nitro v4 and later instance types.

**Nitro v5**

-  Traffic Mirroring is not supported for this version.

-  Up to 200 Gbps[*] per network card.

**Nitro v4**

-  Traffic Mirroring is not supported for this version.

-  GPU accelerated and Trainium based instance types support up to 100 Gbps[*] per network card

for consistency. Other instance types support up to 170 Gbps[*] per network card.

-  Remote direct memory access (RDMA) write is available with EFA for p5.48xlarge instances.

-  Supports ENA Express. For more information about ENA Express, including what specific instance

[types support it see Improve network performance with ENA Express on your EC2 instances in](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ena-express.html)
the Amazon EC2 User Guide.

**Nitro v3**

-  Up to 100 Gbps[*] per network card.

-  Supports RDMA read with EFA for p4d(e).24xlarge instances.

-  Encryption in transit.

**Nitro v2**

-  Enhanced networking with Elastic Network Adapter (ENA).

Network feature support 396


-----

-  Traffic Mirroring.

- 
_Your instance type might support a lower maximum bandwidth. For more information, refer to the_
_network specifications for your instance type in the instance family pages._

### Virtualized instances

The following virtualized instances are built on the Nitro System:

Nitro v5

-  Compute Optimized: C7gn

-  Memory Optimized: R8g

-  High Performance Computing: Hpc7g

Nitro v4

-  General Purpose: M6a | M6i | M6id | M6idn | M6in | M7a | M7g | M7gd | M7i | M7i-flex

-  Compute Optimized: C6a | C6gn | C6i | C6id | C6in | C7a | C7g | C7gd | C7i | C7i-flex

-  Memory Optimized: R6a | R6i | R6idn | R6in | R6id | R7a | R7g | R7gd | R7i | R7iz | U7i-12tb |

U7in-16tb | U7in-24tb | U7in-32tb | X2idn | X2iedn

-  Storage Optimized: I4g | I4i | Im4gn | Is4gen

-  Accelerated Computing: G6 | Gr6 | Inf2 | P5 | Trn1 | Trn1n

-  High Performance Computing: Hpc6a | Hpc6id | Hpc7a

Nitro v3

-  General Purpose: M5dn | M5n | M5zn

-  Compute Optimized: C5n

-  Memory Optimized: R5dn | R5n | U-3tb1 | U-6tb1 | U-9tb1 | U-12tb1 | U-18tb1 | U-24tb1 |

X2iezn

-  Storage Optimized: D3 | D3en | I3en

-  Accelerated Computing: DL1 | DL2q | G4ad | G4dn | G5 | Inf1 | P3dn | P4d | P4de | VT1

Virtualized instances 397


-----

Nitro v2

-  General Purpose: M5 | M5a | M5ad | M5d | M6g | M6gd | T3 | T3a | T4g | A1

-  Compute Optimized: C5 | C5a | C5ad | C5d | C6g | C6gd

-  Memory Optimized: R5 | R5a | R5ad | R5b | R5d | R6g | R6gd | X2gd | z1d

-  Accelerated Computing: G5g

-  Previous Generation: A1

### Bare metal instances

The following bare metal instances are built on the Nitro System:

Nitro v5

-  Compute Optimized: C7gn

-  Memory Optimized: R8g

Nitro v4

-  General Purpose: M6a | M6i | M6id | M6idn | M6in | M7a | M7g | M7gd | M7i

-  Compute Optimized: C6a | C6i | C6id | C6in | C7a | C7g | C7gd | C7i

-  Memory Optimized: R6a | R6i | R6idn | R6in | R6id | R7a | R7g | R7gd | R7i | R7iz | X2idn |

X2iedn

-  Storage Optimized: I4i

Nitro v3

-  General Purpose: M5dn | M5n | M5zn

-  Compute Optimized: C5n

-  Memory Optimized: R5dn | R5n | U-6tb1 | U-9tb1 | U-12tb1 | U-18tb1 | U-24tb1 | X2iezn

-  Storage Optimized: I3en

-  Accelerated Computing: G4dn

Bare metal instances 398


-----

Nitro v2

-  General Purpose: M5 | M5d | M6g | M6gd | Mac1 | Mac2 | Mac2-m1ultra | Mac2-m2 | Mac2
m2pro | A1

-  Compute Optimized: C5 | C5d | C6g | C6gd

-  Memory Optimized: R5 | R5b | R5d | R6g | R6gd | X2gd | z1d

-  Storage Optimized: I3

-  Accelerated Computing: G5g

-  Previous Generation: A1

In most cases, when you launch a bare metal instance, the underlying server goes through its boot
process, during which it verifies all hardware and firmware components. This means that it can
take up to 20 minutes or more from the time the instance enters the running state until it becomes

available over the network.

### Nitro instance requirements

Instances built on the AWS Nitro System use ENA for enhanced networking, and storage volumes
[exposed as NVMe block devices. For more information about NVMe drivers, see Install or upgrade](https://docs.aws.amazon.com/ebs/latest/userguide/nvme-ebs-volumes.html#install-nvme-driver)
[the NVMe driver in the Amazon EBS User Guide for Linux instances, or AWS NVMe drivers for](https://docs.aws.amazon.com/ebs/latest/userguide/nvme-ebs-volumes.html#install-nvme-driver)
[Windows instances in the Amazon EC2 User Guide. For more information about ENA drivers, see](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/aws-nvme-drivers.html)
[Requirements for enhanced networking with ENA in the Amazon EC2 User Guide.](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/enhanced-networking-ena.html#ena-requirements)

The following tabs show details about which driver or kernel versions are recommended for your
operating system.

Linux

The ENA Linux kernel driver version 2.2.9g or later, from the Amazon Drivers GitHub repository
is recommended for Nitro v4 instance types and required for Nitro v5 instance types for Linux
distributions that expose the version information. ENA drivers for Linux are available on GitHub.
[For more information, see Linux kernel driver for Elastic Network Adapter (ENA) family. For](https://github.com/amzn/amzn-drivers/blob/master/kernel/linux/ena/README.rst)
[release notes, see ENA Linux Kernel Driver Release notes.](https://github.com/amzn/amzn-drivers/blob/master/kernel/linux/ena/RELEASENOTES.md)

Linux distributions can also incorporate ENA driver features within the kernel. However, the
timing may vary for implementation within the different distributions. The Amazon Linux 2023

Nitro instance requirements 399


-----

and Bottlerocket Linux distributions support ENA features for Nitro v4 and newer instance types
by default.

Some Linux distributions might require a minimum kernel version to prevent suboptimal
performance of ENA driver features on Nitro v4 and newer instance types. If your Linux
distribution appears in the following table, you can verify the kernel version for your instance
with the uname command as follows:

|Linux distribution|Minimum kernel version|
|---|---|
|Linux upstream|Kernel version 5.9|
|Amazon Linux 2|Kernel 4.14.186|
|Red Hat Enterprise Linux (RHEL)|RHEL 8.3 kernel 4.18.0-240.1.1.el8_3.ARCH|
|SUSE Linux Enterprise Server (SLES)|• SLE 12 SP4 kernel 4.12.14-95.99.3 • SLE 12 SP5 kernel 4.12.14-122.116.1 • SLE 15 kernel 4.12.14-150000.150.92.2 • SLE 15 SP1 kernel 4.12.14-150100.197 .114.2 • SLE 15 SP2 kernel 5.3.18-24.15.1|
|Linux Ubuntu|20.04 kernel 5.4.0-1025-aws|
|DPDK|v20.11|

```
 uname -r

```

Nitro instance requirements 400


-----

**Note**

The following ENA Linux driver versions are not supported, and will result in elastic
network interface attachment failures:

-  ENA Linux

-  Nitro v5 – Earlier than 2.2.9

-  All Nitro versions prior to v5 – Earlier than v1.2.0

-  ENA DPDK

-  Nitro v5 – Earlier than 20.11

-  All Nitro versions prior to v5 – Earlier than v1.1.1


Windows

ENA Windows driver version: 2.2.3 or later for Windows instances.

**Note**

The following ENA Windows drivers are not supported:

- ENA Windows: v2.2.0 or earlier


All of the current AWS Windows AMIs meet these requirements. For more information about
[AMI versions and release notes, see the AWS Windows AMI reference.](https://docs.aws.amazon.com/ec2/latest/windows-ami-reference/windows-amis.html)

FreeBSD

ENA FreeBSD driver version: 2.3.1 or later for FreeBSD instances.

**Note**

ENA FreeBSD driver versions earlier than v2.3.1 are not supported, and will result in
elastic network interface attachment failures.


Nitro instance requirements 401


-----

#### Linux instances with AWS Graviton processors

Linux instances with AWS Graviton processors have the following additional requirements:

-  An AMI with 64-bit ARM architecture.

-  Support for UEFI boot with ACPI tables and ACPI hot-plug of PCI devices.

**Note**

AWS Graviton processors only support Linux operating systems.

Linux instances with AWS Graviton processors 402


-----

## Amazon EC2 instance type quotas

Your AWS account has quotas that affect the number of instances that you can run in each Region.
These quotas are grouped by purchasing option.

**Quotas**

-  On-Demand Instance quotas

-  Spot Instance quotas

-  Dedicated Host quotas

### On-Demand Instance quotas

The following table shows the maximum number of vCPUs that you can provision for On-Demand
Instances. Amazon EC2 automatically increases your On-Demand Instance quotas based on your
[usage. You can also request a quota increase. For more information, see On-Demand Instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-on-demand-instances.html#ec2-on-demand-instances-limits)
[quotas in the Amazon EC2 User Guide.](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-on-demand-instances.html#ec2-on-demand-instances-limits)

|Name|Default|Adjustable|
|---|---|---|
|Running On-Demand DL instances|0|Yes|
|Running On-Demand F instances|0|Yes|
|Running On-Demand G and VT instances|0|Yes|
|Running On-Demand HPC instances|0|Yes|
|Running On-Demand High Memory instances|0|Yes|
|Running On-Demand Inf instances|0|Yes|
|Running On-Demand P instances|0|Yes|
|Running On-Demand Standard (A, C, D, H, I, M, R, T, Z) instances|5|Yes|
|Running On-Demand Trn instances|0|Yes|



On-Demand Instance quotas 403


-----

|Running On-Demand X instances|0|Yes|
|---|---|---|


**Name** **Default** **Adjustable**


### Spot Instance quotas

The following table shows the maximum number of vCPUs that you can provision for Spot
Instances. Amazon EC2 automatically increases your Spot Instance quotas based on your usage.
[You can also request a quota increase. For more information, see Spot Instance quotas in the](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-spot-limits.html)
_Amazon EC2 User Guide._

|Name|Default|Adjustable|
|---|---|---|
|All DL Spot Instance Requests|0|Yes|
|All F Spot Instance Requests|0|Yes|
|All G and VT Spot Instance Requests|0|Yes|
|All Inf Spot Instance Requests|0|Yes|
|All P4, P3 and P2 Spot Instance Requests|0|Yes|
|All P5 Spot Instance Requests|0|Yes|
|All Standard (A, C, D, H, I, M, R, T, Z) Spot Instance Requests|5|Yes|
|All Trn Spot Instance Requests|0|Yes|
|All X Spot Instance Requests|0|Yes|



### Dedicated Host quotas

The following table shows the maximum number of running Dedicated Hosts that you can allocate.

Spot Instance quotas 404


-----

|Name|Default|Adjustable|
|---|---|---|
|Running Dedicated a1 Hosts|0|Yes|
|Running Dedicated c3 Hosts|0|Yes|
|Running Dedicated c4 Hosts|0|Yes|
|Running Dedicated c5 Hosts|0|Yes|
|Running Dedicated c5a Hosts|0|Yes|
|Running Dedicated c5d Hosts|0|Yes|
|Running Dedicated c5n Hosts|0|Yes|
|Running Dedicated c6a Hosts|0|Yes|
|Running Dedicated c6g Hosts|0|Yes|
|Running Dedicated c6gd Hosts|0|Yes|
|Running Dedicated c6gn Hosts|0|Yes|
|Running Dedicated c6i Hosts|0|Yes|
|Running Dedicated c6id Hosts|0|Yes|
|Running Dedicated c6in Hosts|0|Yes|
|Running Dedicated c7a Hosts|0|Yes|
|Running Dedicated c7g Hosts|0|Yes|
|Running Dedicated c7gd Hosts|0|Yes|
|Running Dedicated c7gn Hosts|0|Yes|
|Running Dedicated c7i Hosts|0|Yes|
|Running Dedicated d2 Hosts|0|Yes|


Dedicated Host quotas 405


-----

|Name|Default|Adjustable|
|---|---|---|
|Running Dedicated dl1 Hosts|0|Yes|
|Running Dedicated f1 Hosts|0|Yes|
|Running Dedicated g3 Hosts|0|Yes|
|Running Dedicated g3s Hosts|0|Yes|
|Running Dedicated g4ad Hosts|0|Yes|
|Running Dedicated g4dn Hosts|0|Yes|
|Running Dedicated g5 Hosts|0|Yes|
|Running Dedicated g5g Hosts|0|Yes|
|Running Dedicated g6 Hosts|0|Yes|
|Running Dedicated gr6 Hosts|0|Yes|
|Running Dedicated h1 Hosts|0|Yes|
|Running Dedicated i2 Hosts|0|Yes|
|Running Dedicated i3 Hosts|0|Yes|
|Running Dedicated i3en Hosts|0|Yes|
|Running Dedicated i4g Hosts|0|Yes|
|Running Dedicated i4i Hosts|0|Yes|
|Running Dedicated im4gn Hosts|0|Yes|
|Running Dedicated inf Hosts|0|Yes|
|Running Dedicated inf2 Hosts|0|Yes|
|Running Dedicated is4gen Hosts|0|Yes|


Dedicated Host quotas 406


-----

|Name|Default|Adjustable|
|---|---|---|
|Running Dedicated m3 Hosts|0|Yes|
|Running Dedicated m4 Hosts|0|Yes|
|Running Dedicated m5 Hosts|0|Yes|
|Running Dedicated m5a Hosts|0|Yes|
|Running Dedicated m5ad Hosts|0|Yes|
|Running Dedicated m5d Hosts|0|Yes|
|Running Dedicated m5dn Hosts|0|Yes|
|Running Dedicated m5n Hosts|0|Yes|
|Running Dedicated m5zn Hosts|0|Yes|
|Running Dedicated m6a Hosts|0|Yes|
|Running Dedicated m6g Hosts|0|Yes|
|Running Dedicated m6gd Hosts|0|Yes|
|Running Dedicated m6i Hosts|0|Yes|
|Running Dedicated m6id Hosts|0|Yes|
|Running Dedicated m6idn Hosts|0|Yes|
|Running Dedicated m6in Hosts|0|Yes|
|Running Dedicated m7a Hosts|0|Yes|
|Running Dedicated m7g Hosts|0|Yes|
|Running Dedicated m7gd Hosts|0|Yes|
|Running Dedicated m7i Hosts|0|Yes|


Dedicated Host quotas 407


-----

|Name|Default|Adjustable|
|---|---|---|
|Running Dedicated mac1 Hosts|0|Yes|
|Running Dedicated mac2 Hosts|0|Yes|
|Running Dedicated mac2-m1ultra Hosts|0|Yes|
|Running Dedicated mac2-m2 Hosts|0|Yes|
|Running Dedicated mac2-m2pro Hosts|0|Yes|
|Running Dedicated p2 Hosts|0|Yes|
|Running Dedicated p3 Hosts|0|Yes|
|Running Dedicated p3dn Hosts|0|Yes|
|Running Dedicated p4d Hosts|0|Yes|
|Running Dedicated p5 Hosts|0|Yes|
|Running Dedicated r3 Hosts|0|Yes|
|Running Dedicated r4 Hosts|0|Yes|
|Running Dedicated r5 Hosts|0|Yes|
|Running Dedicated r5a Hosts|0|Yes|
|Running Dedicated r5ad Hosts|0|Yes|
|Running Dedicated r5b Hosts|0|Yes|
|Running Dedicated r5d Hosts|0|Yes|
|Running Dedicated r5dn Hosts|0|Yes|
|Running Dedicated r5n Hosts|0|Yes|
|Running Dedicated r6a Hosts|0|Yes|


Dedicated Host quotas 408


-----

|Name|Default|Adjustable|
|---|---|---|
|Running Dedicated r6g Hosts|0|Yes|
|Running Dedicated r6gd Hosts|0|Yes|
|Running Dedicated r6i Hosts|0|Yes|
|Running Dedicated r6id Hosts|0|Yes|
|Running Dedicated r6idn Hosts|0|Yes|
|Running Dedicated r6in Hosts|0|Yes|
|Running Dedicated r7a Hosts|0|Yes|
|Running Dedicated r7g Hosts|0|Yes|
|Running Dedicated r7gd Hosts|0|Yes|
|Running Dedicated r7i Hosts|0|Yes|
|Running Dedicated r7iz Hosts|0|Yes|
|Running Dedicated r8g Hosts|0|Yes|
|Running Dedicated t3 Hosts|0|Yes|
|Running Dedicated trn1 Hosts|0|Yes|
|Running Dedicated trn1n Hosts|0|Yes|
|Running Dedicated u-12tb1 Hosts|0|Yes|
|Running Dedicated u-18tb1 Hosts|0|Yes|
|Running Dedicated u-24tb1 Hosts|0|Yes|
|Running Dedicated u-3tb1 Hosts|0|Yes|
|Running Dedicated u-6tb1 Hosts|0|Yes|


Dedicated Host quotas 409


-----

|Name|Default|Adjustable|
|---|---|---|
|Running Dedicated u-9tb1 Hosts|0|Yes|
|Running Dedicated u7i-12tb Hosts|0|Yes|
|Running Dedicated u7in-16tb Hosts|0|Yes|
|Running Dedicated u7in-24tb Hosts|0|Yes|
|Running Dedicated u7in-32tb Hosts|0|Yes|
|Running Dedicated vt1 Hosts|0|Yes|
|Running Dedicated x1 Hosts|0|Yes|
|Running Dedicated x1e Hosts|0|Yes|
|Running Dedicated x2gd Hosts|0|Yes|
|Running Dedicated x2idn Hosts|0|Yes|
|Running Dedicated x2iedn Hosts|0|Yes|
|Running Dedicated x2iezn Hosts|0|Yes|
|Running Dedicated z1d Hosts|0|Yes|


Dedicated Host quotas 410


-----

## Document history for the Amazon EC2 Instance Types Guide

The following table describes the instance type releases for Amazon EC2.

Change Description Date


Nitro version features Updated Nitro page to include
features and instance types
by Nitro version. Added Nitro
version to the Hyperviso
r column in the Platform
summary tables also.

R8g instances New memory optimized
instances powered by AWS
Graviton4 processors and up
to 1.5 TiB memory.

Mac2-m1ultra instances New general purpose instance
type that features Apple M1
Ultra processors.


July 22, 2024

July 9, 2024

June 17, 2024

May 28, 2024

May 14, 2024


U7i-12tb, U7in-16tb,
U7in-24tb, and U7in-32tb
instances


New high memory instance
types that feature 4th
generation Intel Xeon
Scalable processors.


C7i-flex instances New compute optimized
instances featuring Intel Xeon
Scalable processors (Sapphire
Rapids). They deliver a
baseline CPU performance of
40 percent with the ability to
deliver up to 100 percent CPU
performance for 95 percent


411


-----

of the time over a 24-hour
period.

g6 and gr6 instances New high performance GPUbased instance types for
deep learning inference and
graphics-intensive applicati
ons.

C7gn bare metal instances New c7gn.metal bare
metal instance type powered
by the latest generation AWS
Graviton3E processors and
the new AWS Nitro cards.


April 4, 2024

March 26, 2024


C7gd, M7gd, and R7gd bare
metal instances


New bare metal instances. March 6, 2024


DL2q instances New instances that use
Qualcomm AI100 inference
accelerators, which feature
7th generation Qualcomm
Edge AI cores. These instances
can be used to cost-efficiently
deploy deep learning (DL)
workloads in the cloud or
validate performance and
accuracy of DL workloads
that will be deployed on
Qualcomm edge devices.

Mac2-m2 instances New general purpose instance
type that features Apple M2
processors.


November 15, 2023

October 25, 2023


412


-----

R7i instances New memory optimized
instance types that feature
4th generation Intel Xeon
Scalable processors.

C7a instances New compute optimized
instances powered by 4th
generation AMD EPYC
processors.

Mac2-m2pro instances New general purpose instance
type that features Apple M2
Pro processors.

C7i instances New compute optimized
instance types that feature
4th generation Intel Xeon
Scalable processors.

R7a instances New memory optimized
instance types featuring 4th
generation AMD EPYC 9R14
processors and up to 1536
GiB of system memory.

R7iz instances New high-frequency and high
memory instances powered
by 4th generation Intel Xeon
processors.

Hpc7a instances New compute optimized
instance types that feature
4th generation AMD EPYC
processors. These instances
support up to 300 Gbps
networking bandwidth, and
up to 192 CPU cores with up
to 768 GB of system memory.


October 16, 2023

October 4, 2023

September 18, 2023

September 14, 2023

September 11, 2023

September 7, 2023

August 17, 2023


413


-----

M7a instances New general purpose
instances powered by 4th
generation AMD EPYC
processors.

M7i-flex instances New general purpose
instances that offer a balance
of compute, memory, and
network resources for a broad
spectrum of general purpose
applications. They deliver a
baseline CPU performance of
40 percent with the ability to
deliver up to 100 percent CPU
performance for 95 percent
of the time over a 24-hour
period.

M7i instances New general purpose
instance types that feature
4th generation Intel Xeon
Scalable processors.

R7gd instances New memory optimized
instances featuring the latest
AWS Graviton3 processors.

M7gd instances New general purpose
instances featuring the latest
AWS Graviton3 processors.

C7gd instances New compute optimized
instances featuring the latest
AWS Graviton3 processors.


August 15, 2023

August 2, 2023

August 2, 2023

July 28, 2023

July 28, 2023

July 28, 2023


414


-----

P5 instances New accelerated computing
instances that feature 8
NVIDIA H100 GPUs with 640
GB high-bandwidth GPU
memory, 3rd generation AMD
EPYC processors, and 2 TB
system memory.

Hpc7g instances New high-performance
computing instances powered
by AWS Graviton3E processor
s that provide up to 35
percent higher vectorinstruction processing
performance than Graviton3
processors.

C7gn instances New compute optimized
instances powered by the
latest generation AWS
Graviton3E processors and
the new AWS Nitro cards.
These instances offer up to
200 Gbps network bandwidth.

I4g instances New storage optimized
instances that features the
AWS Graviton2 processor and
AWS Nitro SSDs.

Trn1n instances New accelerated computing
instances optimized for
machine learning training
powered by AWS Trainium
accelerators.


July 26, 2023

June 20, 2023

June 20, 2023

May 9, 2023

April 13, 2023


415


-----

Inf2 instances New instances featuring AWS
Inferentia2 accelerators, the
latest machine learning chip
designed by AWS.

Hpc6id instance New memory optimized
instance featuring 3rd
generation Intel Xeon
Scalable processors (Ice Lake).

R6in and R6idn instances New memory optimized
instances for network-i
ntensive workloads.

M6in and M6idn instances New general computing
instances types.

C6in instances New compute optimized
instances ideal for running
high performance computing.

Trn1 instances New accelerated computing
instances optimized for deep
learning powered by AWS
Trainium chips.

R6a instances New memory optimized
instances featuring 3rd
generation AMD EPYC
processors.

R6id instances New memory optimized
instances featuring 3rd
generation Intel Xeon
Scalable processors (Ice Lake).


April 13, 2023

November 29, 2022

November 28, 2022

November 28, 2022

November 28, 2022

October 10, 2022

July 19, 2022

June 9, 2022


416


-----

M6id instances New general purpose
instances featuring 3rd
generation Intel Xeon
Scalable processors (Ice Lake).

C6id instances New compute optimized
instances featuring 3rd
generation Intel Xeon
Scalable processors (Ice Lake).

C7g instances New compute optimized
instances featuring AWS
Graviton3 processors.

I4i instances New storage optimized
instances featuring 3rd
generation Intel Xeon
Scalable processors (Ice Lake).

X2idn and X2iedn instances New memory optimized
instances featuring Intel Xeon
Scalable processors (Ice Lake).

C6a instances New compute optimized
instances featuring 3rd
generation AMD EPYC
processors (Milan).

X2iezn instances New memory optimized
instances featuring Intel Xeon
Platinum processors (Cascade
Lake).

Hpc6a instances New compute optimized
instances featuring AMD EPYC
processors.


May 26, 2022

May 26, 2022

May 23, 2022

April 27, 2022

March 10, 2022

February 14, 2022

January 26, 2022

January 10, 2022


417


-----

Im4gn and Is4gen instances New storage optimized
instances.

M6a instances New general purpose
instances powered by
AMD 3rd Generation EPYC
processors.

G5g instances New accelerated computing
instances featuring AWS
Graviton2 processors based
on 64-bit Arm architecture.

R6i instances New memory optimized
instances.

G5 instances New accelerated computing
instances featuring up to
8 NVIDIA A10G GPUs and
second generation AMD EPY
processors.

C6i instances New compute optimized
instances featuring Intel Xeon
Scalable processors (Ice Lake).

DL1 instances New accelerated computing
instances featuring Habana
Gaudi accelerators and Intel
Xeon Platinum processors
(Cascade Lake).

VT1 instances New accelerated computing
instances that use Xilinx Alveo
U30 media accelerators and
are designed for live video
transcoding workloads.


November 30, 2021

November 29, 2021

November 29, 2021

November 22, 2021

November 11, 2021

October 28, 2021

October 26, 2021

September 13, 2021


418


-----

M6i instances New general purpose
instances featuring third
generation Intel Xeon
Scalable processors (Ice Lake).


August 16, 2021

May 11, 2021

March 16, 2021

December 18, 2020

December 9, 2020

December 1, 2020

November 30, 2020


High memory virtualized
instances


Virtualized high memory
instances purpose-built
to run large in-memory
databases. The new types are
u-6tb1.56xlarge, u-6tb1.11
2xlarge, u-9tb1.112xlarge,
and u-12tb1.112xlarge.


X2gd instances New memory optimized
instances featuring an AWS
Graviton2 processor based on
64-bit Arm architecture.

C6gn instances New computed optimized
instances featuring an AWS
Graviton2 processor based
on 64-bit Arm architecture.
These instances can utilize
up to 100 Gbps of network
bandwidth.

G4ad instances New instances powered by
AMD Radeon Pro V520 GPUs
and AMD 2nd Generation
EPYC processors.


D3, D3en, M5zn, and R5b
instances


New instance types built on
the Nitro System.


Mac1 instances New instances built on Apple
Mac mini computers that
support running macOS
workloads on Amazon EC2.


419


-----

P4d instances New accelerated computing
instances that provide a highperformance platform for
machine learning and HPC
workloads.

T4g instances New general purpose
instances powered by AWS
Graviton2 processors, which
are based on 64-bit Arm
Neoverse cores and custom
silicon designed by AWS for
optimized performance and
cost.

C5ad instances New compute optimized
instances featuring second-ge
neration AMD EPYC processor
s.


November 2, 2020

September 14, 2020

August 13, 2020

July 27, 2020

June 10, 2020


C6gd, M6gd, and R6gd
instances


New general purpose
instances powered by AWS
Graviton2 processors, which
are based on 64-bit Arm
Neoverse cores and custom
silicon designed by AWS for
optimized performance and
cost.


C6g and R6g instances New general purpose
instances powered by AWS
Graviton2 processors, which
are based on 64-bit Arm
Neoverse cores and custom
silicon designed by AWS for
optimized performance and
cost.


420


-----

C5a instances New compute optimized
instances featuring second-ge
neration AMD EPYC processor
s.

M6g instances New general purpose
instances powered by AWS
Graviton2 processors, which
are based on 64-bit Arm
Neoverse cores and custom
silicon designed by AWS for
optimized performance and
cost.

Inf1 instances New instances featuring AWS
Inferentia, a machine learning
inference chip designed to
deliver high performance at a
low cost.

G4dn instances New instances featuring
NVIDIA Tesla GPUs.

I3en instances New I3en instances can utilize
up to 100 Gbps of network
bandwidth.

T3a instances New instances featuring AMD
EPYC processors.

M5ad and R5ad instances New instances featuring AMD
EPYC processors.

p3dn.24xlarge instances New instances that provide
100 Gbps of network
bandwidth.


June 4, 2020

May 11, 2020

December 3, 2019

September 19, 2019

May 8, 2019

April 24, 2019

March 27, 2019

December 7, 2018


421


-----

C5n instances New instances that provide
up to 100 Gbps of network
bandwidth.

A1 instances New instances featuring Armbased processors.

R5a instances New instances featuring AMD
EPYC processors.

M5a instances New instances featuring AMD
EPYC processors.

T3 instances New instances featuring AMD
EPYC processors.

z1d instances New memory optimized
instances.

R5 and R5d instances New memory optimized
instances.

X1e instances New memory optimized
instances.

M5 instances New general purpose
instances.

H1 instances New storage optimized
instances.

C5 instances New compute optimized
instances.

P3 instances New accelerated computing
instances.

G3 instances New accelerated computing
instances.


November 26, 2018

November 26, 2018

November 6, 2018

November 6, 2018

August 21, 2018

July 25, 2018

July 25, 2018

November 28, 2017

November 28, 2017

November 28, 2017

November 6, 2017

October 25, 2017

July 13, 2017


422


-----

F1 instances New accelerated computing
instances.

I3 instances New storage optimized
instances.

R4 instances New memory optimized
instances.

P2 instances New accelerated computing
instances.

X1 instances New memory optimized
instances.

M4 instances New general purpose
instances.

D2 instances New storage optimized
instances.

C4 instances New compute optimized
instances.

T2 instances New general purpose
instances.


April 19, 2017

February 23, 2017

November 30, 2016

September 29, 2016

May 18, 2016

June 11, 2015

March 24, 2015

January 11, 2015

June 30, 2014


423


-----

