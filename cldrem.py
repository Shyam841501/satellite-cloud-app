{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": []
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "code",
      "source": [
        "!git clone https://github.com/ameraner/dsen2-cr.git"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "-QOKsf-oOUfJ",
        "outputId": "55049c50-33ef-4471-e2f4-1d9924b4d42a"
      },
      "execution_count": 6,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Cloning into 'dsen2-cr'...\n",
            "remote: Enumerating objects: 94, done.\u001b[K\n",
            "remote: Counting objects: 100% (38/38), done.\u001b[K\n",
            "remote: Compressing objects: 100% (28/28), done.\u001b[K\n",
            "remote: Total 94 (delta 20), reused 10 (delta 10), pack-reused 56 (from 1)\u001b[K\n",
            "Receiving objects: 100% (94/94), 683.99 KiB | 15.54 MiB/s, done.\n",
            "Resolving deltas: 100% (39/39), done.\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "%cd dsen2-cr/"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "hZItRVr6PJvl",
        "outputId": "2a789534-efad-4b1a-e1e3-ca28193d0188"
      },
      "execution_count": 7,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "/content/dsen2-cr\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!pip install tensorflow keras numpy scipy rasterio pydot graphviz h5py"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "M_3gOV2AQd7k",
        "outputId": "ca8c46e1-7251-4fbe-9190-f5ad1944f952"
      },
      "execution_count": 11,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Requirement already satisfied: tensorflow in /usr/local/lib/python3.12/dist-packages (2.20.0)\n",
            "Requirement already satisfied: keras in /usr/local/lib/python3.12/dist-packages (3.13.2)\n",
            "Requirement already satisfied: numpy in /usr/local/lib/python3.12/dist-packages (2.0.2)\n",
            "Requirement already satisfied: scipy in /usr/local/lib/python3.12/dist-packages (1.16.3)\n",
            "Requirement already satisfied: rasterio in /usr/local/lib/python3.12/dist-packages (1.5.0)\n",
            "Requirement already satisfied: pydot in /usr/local/lib/python3.12/dist-packages (4.0.1)\n",
            "Requirement already satisfied: graphviz in /usr/local/lib/python3.12/dist-packages (0.21)\n",
            "Requirement already satisfied: h5py in /usr/local/lib/python3.12/dist-packages (3.16.0)\n",
            "Requirement already satisfied: absl-py>=1.0.0 in /usr/local/lib/python3.12/dist-packages (from tensorflow) (1.4.0)\n",
            "Requirement already satisfied: astunparse>=1.6.0 in /usr/local/lib/python3.12/dist-packages (from tensorflow) (1.6.3)\n",
            "Requirement already satisfied: flatbuffers>=24.3.25 in /usr/local/lib/python3.12/dist-packages (from tensorflow) (25.12.19)\n",
            "Requirement already satisfied: gast!=0.5.0,!=0.5.1,!=0.5.2,>=0.2.1 in /usr/local/lib/python3.12/dist-packages (from tensorflow) (0.7.0)\n",
            "Requirement already satisfied: google_pasta>=0.1.1 in /usr/local/lib/python3.12/dist-packages (from tensorflow) (0.2.0)\n",
            "Requirement already satisfied: libclang>=13.0.0 in /usr/local/lib/python3.12/dist-packages (from tensorflow) (18.1.1)\n",
            "Requirement already satisfied: opt_einsum>=2.3.2 in /usr/local/lib/python3.12/dist-packages (from tensorflow) (3.4.0)\n",
            "Requirement already satisfied: packaging in /usr/local/lib/python3.12/dist-packages (from tensorflow) (26.2)\n",
            "Requirement already satisfied: protobuf>=5.28.0 in /usr/local/lib/python3.12/dist-packages (from tensorflow) (5.29.6)\n",
            "Requirement already satisfied: requests<3,>=2.21.0 in /usr/local/lib/python3.12/dist-packages (from tensorflow) (2.32.4)\n",
            "Requirement already satisfied: setuptools in /usr/local/lib/python3.12/dist-packages (from tensorflow) (75.2.0)\n",
            "Requirement already satisfied: six>=1.12.0 in /usr/local/lib/python3.12/dist-packages (from tensorflow) (1.17.0)\n",
            "Requirement already satisfied: termcolor>=1.1.0 in /usr/local/lib/python3.12/dist-packages (from tensorflow) (3.3.0)\n",
            "Requirement already satisfied: typing_extensions>=3.6.6 in /usr/local/lib/python3.12/dist-packages (from tensorflow) (4.15.0)\n",
            "Requirement already satisfied: wrapt>=1.11.0 in /usr/local/lib/python3.12/dist-packages (from tensorflow) (2.2.1)\n",
            "Requirement already satisfied: grpcio<2.0,>=1.24.3 in /usr/local/lib/python3.12/dist-packages (from tensorflow) (1.81.1)\n",
            "Requirement already satisfied: tensorboard~=2.20.0 in /usr/local/lib/python3.12/dist-packages (from tensorflow) (2.20.0)\n",
            "Requirement already satisfied: ml_dtypes<1.0.0,>=0.5.1 in /usr/local/lib/python3.12/dist-packages (from tensorflow) (0.5.4)\n",
            "Requirement already satisfied: rich in /usr/local/lib/python3.12/dist-packages (from keras) (13.9.4)\n",
            "Requirement already satisfied: namex in /usr/local/lib/python3.12/dist-packages (from keras) (0.1.0)\n",
            "Requirement already satisfied: optree in /usr/local/lib/python3.12/dist-packages (from keras) (0.19.1)\n",
            "Requirement already satisfied: affine in /usr/local/lib/python3.12/dist-packages (from rasterio) (2.4.0)\n",
            "Requirement already satisfied: attrs in /usr/local/lib/python3.12/dist-packages (from rasterio) (26.1.0)\n",
            "Requirement already satisfied: certifi in /usr/local/lib/python3.12/dist-packages (from rasterio) (2026.5.20)\n",
            "Requirement already satisfied: click!=8.2.*,>=4.0 in /usr/local/lib/python3.12/dist-packages (from rasterio) (8.4.1)\n",
            "Requirement already satisfied: cligj>=0.5 in /usr/local/lib/python3.12/dist-packages (from rasterio) (0.7.2)\n",
            "Requirement already satisfied: pyparsing in /usr/local/lib/python3.12/dist-packages (from rasterio) (3.3.2)\n",
            "Requirement already satisfied: wheel<1.0,>=0.23.0 in /usr/local/lib/python3.12/dist-packages (from astunparse>=1.6.0->tensorflow) (0.47.0)\n",
            "Requirement already satisfied: charset_normalizer<4,>=2 in /usr/local/lib/python3.12/dist-packages (from requests<3,>=2.21.0->tensorflow) (3.4.7)\n",
            "Requirement already satisfied: idna<4,>=2.5 in /usr/local/lib/python3.12/dist-packages (from requests<3,>=2.21.0->tensorflow) (3.18)\n",
            "Requirement already satisfied: urllib3<3,>=1.21.1 in /usr/local/lib/python3.12/dist-packages (from requests<3,>=2.21.0->tensorflow) (2.5.0)\n",
            "Requirement already satisfied: markdown>=2.6.8 in /usr/local/lib/python3.12/dist-packages (from tensorboard~=2.20.0->tensorflow) (3.10.2)\n",
            "Requirement already satisfied: pillow in /usr/local/lib/python3.12/dist-packages (from tensorboard~=2.20.0->tensorflow) (11.3.0)\n",
            "Requirement already satisfied: tensorboard-data-server<0.8.0,>=0.7.0 in /usr/local/lib/python3.12/dist-packages (from tensorboard~=2.20.0->tensorflow) (0.7.2)\n",
            "Requirement already satisfied: werkzeug>=1.0.1 in /usr/local/lib/python3.12/dist-packages (from tensorboard~=2.20.0->tensorflow) (3.1.8)\n",
            "Requirement already satisfied: markdown-it-py>=2.2.0 in /usr/local/lib/python3.12/dist-packages (from rich->keras) (4.2.0)\n",
            "Requirement already satisfied: pygments<3.0.0,>=2.13.0 in /usr/local/lib/python3.12/dist-packages (from rich->keras) (2.20.0)\n",
            "Requirement already satisfied: mdurl~=0.1 in /usr/local/lib/python3.12/dist-packages (from markdown-it-py>=2.2.0->rich->keras) (0.1.2)\n",
            "Requirement already satisfied: markupsafe>=2.1.1 in /usr/local/lib/python3.12/dist-packages (from werkzeug>=1.0.1->tensorboard~=2.20.0->tensorflow) (3.0.3)\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import tensorflow as tf\n",
        "if tf.__version__.startswith('2'):\n",
        "    import tensorflow.compat.v1 as tf1\n",
        "    tf1.disable_v2_behavior()\n",
        "    print(\"TensorFlow 1.x compatibility mode successfully activated!\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "mXZglkcVQqcs",
        "outputId": "4291fd01-bd5e-444b-c905-85e07114574a"
      },
      "execution_count": 12,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "WARNING:tensorflow:From /usr/local/lib/python3.12/dist-packages/tensorflow/python/compat/v2_compat.py:98: disable_resource_variables (from tensorflow.python.ops.resource_variables_toggle) is deprecated and will be removed in a future version.\n",
            "Instructions for updating:\n",
            "non-resource variables are not supported in the long term\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "TensorFlow 1.x compatibility mode successfully activated!\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!ls -la"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "2M4YP0TJQ7fJ",
        "outputId": "55308451-0e61-44b8-fdbc-4e8c05fb0dee"
      },
      "execution_count": 14,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "total 76\n",
            "drwxr-xr-x 7 root root  4096 Jun 29 16:35 .\n",
            "drwxr-xr-x 1 root root  4096 Jun 29 16:35 ..\n",
            "drwxr-xr-x 3 root root  4096 Jun 29 16:35 Code\n",
            "drwxr-xr-x 2 root root  4096 Jun 29 16:35 Data\n",
            "drwxr-xr-x 2 root root  4096 Jun 29 16:35 doc\n",
            "drwxr-xr-x 2 root root  4096 Jun 29 16:35 Docker\n",
            "drwxr-xr-x 8 root root  4096 Jun 29 16:35 .git\n",
            "-rw-r--r-- 1 root root 35149 Jun 29 16:35 LICENSE\n",
            "-rw-r--r-- 1 root root  9045 Jun 29 16:35 README.md\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!ls -la Code/"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "oqgTmAvQRcpc",
        "outputId": "862eb312-f972-4ba0-9ae5-af0f818ea602"
      },
      "execution_count": 15,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "total 48\n",
            "drwxr-xr-x 3 root root 4096 Jun 29 16:35 .\n",
            "drwxr-xr-x 7 root root 4096 Jun 29 16:35 ..\n",
            "-rw-r--r-- 1 root root 8179 Jun 29 16:35 dsen2cr_main.py\n",
            "-rw-r--r-- 1 root root 2316 Jun 29 16:35 dsen2cr_network.py\n",
            "-rw-r--r-- 1 root root 8217 Jun 29 16:35 dsen2cr_pytorch_model.py\n",
            "-rw-r--r-- 1 root root 8200 Jun 29 16:35 dsen2cr_tools.py\n",
            "drwxr-xr-x 2 root root 4096 Jun 29 16:35 tools\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!python Code/dsen2cr_main.py --help"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Ynq0cIf1Rudy",
        "outputId": "a0afcbb3-5716-4fe0-f5c2-84c357196a4e"
      },
      "execution_count": 16,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Traceback (most recent call last):\n",
            "  File \"/content/dsen2-cr/Code/dsen2cr_main.py\", line 10, in <module>\n",
            "    from dsen2cr_network import DSen2CR_model\n",
            "  File \"/content/dsen2-cr/Code/dsen2cr_network.py\", line 4, in <module>\n",
            "    from keras.models import Model, Input\n",
            "ImportError: cannot import name 'Input' from 'keras.models' (/usr/local/lib/python3.12/dist-packages/keras/models/__init__.py)\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!ls -la Data/"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "NErcbQ_RR7F_",
        "outputId": "6fbc4097-956a-4926-bc10-a55cb3c3bf3a"
      },
      "execution_count": 17,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "total 28\n",
            "drwxr-xr-x 2 root root  4096 Jun 29 16:35 .\n",
            "drwxr-xr-x 7 root root  4096 Jun 29 16:35 ..\n",
            "-rw-r--r-- 1 root root   488 Jun 29 16:35 datasetfilelist.csv\n",
            "-rw-r--r-- 1 root root 14728 Jun 29 16:35 unpack_dataset.ipynb\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!sed -i \"s/from keras.models import Model, Input/from keras.models import Model\\nfrom keras.layers import Input/g\" Code/dsen2cr_network.py"
      ],
      "metadata": {
        "id": "nV4KkSJaStgB"
      },
      "execution_count": 21,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "!sed -i \"s/from keras.utils import multi_gpu_model/# from keras.utils import multi_gpu_model/g\" Code/dsen2cr_main.py"
      ],
      "metadata": {
        "id": "UsjO9zk0TVED"
      },
      "execution_count": 23,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "!python Code/dsen2cr_main.py --help"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "RCU6Uy0LTdOp",
        "outputId": "12d01509-12b1-4b2e-df74-11645cbe67ed"
      },
      "execution_count": 24,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "usage: dsen2cr_main.py [-h] [--predict PREDICT_FILE] [--resume RESUME_FILE]\n",
            "\n",
            "DSen2-CR model code\n",
            "\n",
            "options:\n",
            "  -h, --help            show this help message and exit\n",
            "  --predict PREDICT_FILE\n",
            "                        Predict from model checkpoint.\n",
            "  --resume RESUME_FILE  Resume training from model checkpoint.\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!sed -i \"s/optimizer = Nadam(lr=lr, beta_1=0.9, beta_2=0.999, epsilon=1e-8, schedule_decay=0.004)/optimizer = Nadam(learning_rate=lr, beta_1=0.9, beta_2=0.999, epsilon=1e-8)/g\" Code/dsen2cr_main.py"
      ],
      "metadata": {
        "id": "4y6pyYe4UUt1"
      },
      "execution_count": 26,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "!sed -i '1s/^/import tensorflow as tf\\nif tf._version_.startswith(\"2\"):\\n    import tensorflow.compat.v1 as tf1\\n    tf1.disable_v2_behavior()\\n    tf.ConfigProto = tf1.ConfigProto\\n/' Code/dsen2cr_main.py"
      ],
      "metadata": {
        "id": "p0Hg5bKCVJAe"
      },
      "execution_count": 28,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "file_path = \"Code/dsen2cr_main.py\"\n",
        "\n",
        "with open(file_path, \"r\") as f:\n",
        "    lines = f.readlines()\n",
        "\n",
        "# Find and remove the problematic line\n",
        "future_line = \"from __future__ import division\\n\"\n",
        "cleaned_lines = [line for line in lines if \"__future__\" not in line]\n",
        "\n",
        "# Re-insert it at the absolute top (index 0)\n",
        "fixed_lines = [future_line] + cleaned_lines\n",
        "\n",
        "with open(file_path, \"w\") as f:\n",
        "    f.writelines(fixed_lines)\n",
        "\n",
        "print(\"File successfully fixed!\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ucgtDSDYXVRp",
        "outputId": "9f54e059-e13d-4036-ddea-f5d30301ad06"
      },
      "execution_count": 30,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "File successfully fixed!\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!python Code/dsen2cr_main.py --predict your_image_name.tif"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "f5d9grN_YeA7",
        "outputId": "75382b3e-df92-488e-d728-65319e4a87e7"
      },
      "execution_count": 31,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Traceback (most recent call last):\n",
            "  File \"/content/dsen2-cr/Code/dsen2cr_main.py\", line 3, in <module>\n",
            "    if tf._version_.startswith(\"2\"):\n",
            "       ^^^^^^^^^^^^\n",
            "AttributeError: module 'tensorflow' has no attribute '_version_'. Did you mean: '__version__'?\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!sed -i 's/_version_/__version__/g' /content/dsen2-cr/Code/dsen2cr_main.py"
      ],
      "metadata": {
        "id": "42GfBcMzbzbJ"
      },
      "execution_count": 40,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "!python Code/dsen2cr_main.py --predict your_image_name.tif"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "fCF0GGvPb2tv",
        "outputId": "8c19012f-8e19-48bc-cdf5-b0368d04202d"
      },
      "execution_count": 41,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "  File \"/content/dsen2-cr/Code/dsen2cr_main.py\", line 18\n",
            "    parser.add_argument('--predict', action='store', dest='predict_file', help='Predict from model checkpoint.')\n",
            "IndentationError: unexpected indent\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# 1. Reset the broken script back to the original GitHub state\n",
        "!git -C /content/dsen2-cr/ checkout Code/dsen2cr_main.py\n",
        "\n",
        "# 2. Safely fix the version typo without breaking the indentation\n",
        "!sed -i 's/_version_/__version__/g' /content/dsen2-cr/Code/dsen2cr_main.py\n",
        "\n",
        "# 3. Permanently switch your notebook directory to the Code folder\n",
        "# (Using %cd ensures the script can find its relative datasets)\n",
        "%cd /content/dsen2-cr/Code/\n",
        "\n",
        "# 4. Run your prediction script again\n",
        "!python dsen2cr_main.py --predict your_image_name.tif"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "q-he210mcOqw",
        "outputId": "7d3fe9ae-a941-4a58-8ae6-c55d8cf7780b"
      },
      "execution_count": 42,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Updated 1 path from the index\n",
            "/content/dsen2-cr/Code\n",
            "Traceback (most recent call last):\n",
            "  File \"/content/dsen2-cr/Code/dsen2cr_main.py\", line 13, in <module>\n",
            "    from keras.utils import multi_gpu_model\n",
            "ImportError: cannot import name 'multi_gpu_model' from 'keras.utils' (/usr/local/lib/python3.12/dist-packages/keras/utils/__init__.py)\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# 1. Read the main script file\n",
        "with open('/content/dsen2-cr/Code/dsen2cr_main.py', 'r') as f:\n",
        "    lines = f.readlines()\n",
        "\n",
        "# 2. Inject a mock function at the very top to safely trick Keras\n",
        "mock_keras_gpu = \"\"\"import keras.utils\n",
        "if not hasattr(keras.utils, 'multi_gpu_model'):\n",
        "    keras.utils.multi_gpu_model = lambda model, gpus: model\n",
        "\"\"\"\n",
        "lines.insert(0, mock_keras_gpu)\n",
        "\n",
        "# 3. Save the modified script\n",
        "with open('/content/dsen2-cr/Code/dsen2cr_main.py', 'w') as f:\n",
        "    f.writelines(lines)\n",
        "\n",
        "print(\"Keras patch applied successfully!\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "rugYjUPKcgjm",
        "outputId": "8c9a7b20-adca-48b2-b779-52b04b5eb4f0"
      },
      "execution_count": 43,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Keras patch applied successfully!\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "%cd /content/dsen2-cr/Code/\n",
        "!python dsen2cr_main.py --predict your_image_name.tif"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Yu60g2MwcqQA",
        "outputId": "c4069ed7-f395-4a05-f8c4-222b107ded77"
      },
      "execution_count": 44,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "/content/dsen2-cr/Code\n",
            "  File \"/content/dsen2-cr/Code/dsen2cr_main.py\", line 4\n",
            "    from __future__ import division\n",
            "    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n",
            "SyntaxError: from __future__ imports must occur at the beginning of the file\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# 1. Reset the script to its original clean state from GitHub\n",
        "!git -C /content/dsen2-cr/ checkout Code/dsen2cr_main.py\n",
        "\n",
        "# 2. Fix the original version typo safely\n",
        "!sed -i 's/_version_/__version__/g' /content/dsen2-cr/Code/dsen2cr_main.py\n",
        "\n",
        "# 3. Swap the broken multi_gpu_model import line with a dummy function directly\n",
        "!sed -i 's/from keras.utils import multi_gpu_model/multi_gpu_model = lambda model, gpus: model/g' /content/dsen2-cr/Code/dsen2cr_main.py\n",
        "\n",
        "# 4. Switch directory to Code\n",
        "%cd /content/dsen2-cr/Code/\n",
        "\n",
        "# 5. Re-run your prediction command\n",
        "!python dsen2cr_main.py --predict your_image_name.tif"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "upGM8Z4uc5XA",
        "outputId": "3bbf6aac-09c8-44b8-f4fe-0e0a196d51a2"
      },
      "execution_count": 45,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Updated 1 path from the index\n",
            "/content/dsen2-cr/Code\n",
            "Traceback (most recent call last):\n",
            "  File \"/content/dsen2-cr/Code/dsen2cr_main.py\", line 179, in <module>\n",
            "    run_dsen2cr(args.predict_file, args.resume_file)\n",
            "  File \"/content/dsen2-cr/Code/dsen2cr_main.py\", line 80, in run_dsen2cr\n",
            "    optimizer = Nadam(lr=lr, beta_1=0.9, beta_2=0.999, epsilon=1e-8, schedule_decay=0.004)\n",
            "                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n",
            "  File \"/usr/local/lib/python3.12/dist-packages/keras/src/optimizers/nadam.py\", line 57, in __init__\n",
            "    super().__init__(\n",
            "  File \"/usr/local/lib/python3.12/dist-packages/keras/src/backend/tensorflow/optimizer.py\", line 21, in __init__\n",
            "    super().__init__(*args, **kwargs)\n",
            "  File \"/usr/local/lib/python3.12/dist-packages/keras/src/optimizers/base_optimizer.py\", line 90, in __init__\n",
            "    raise ValueError(f\"Argument(s) not recognized: {kwargs}\")\n",
            "ValueError: Argument(s) not recognized: {'lr': 7e-05, 'schedule_decay': 0.004}\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# 1. Read the script file\n",
        "file_path = '/content/dsen2-cr/Code/dsen2cr_main.py'\n",
        "with open(file_path, 'r') as f:\n",
        "    lines = f.readlines()\n",
        "\n",
        "# 2. Modify the Nadam optimizer configuration to match modern Keras syntax\n",
        "for i, line in enumerate(lines):\n",
        "    if \"optimizer = Nadam(\" in line:\n",
        "        lines[i] = \"    optimizer = Nadam(learning_rate=lr, beta_1=0.9, beta_2=0.999, epsilon=1e-8)\\n\"\n",
        "        print(f\"Fixed optimizer on line {i+1}\")\n",
        "        break\n",
        "\n",
        "# 3. Save the changes back to the script\n",
        "with open(file_path, 'w') as f:\n",
        "    f.writelines(lines)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "-OiefzbEdKS6",
        "outputId": "8a95c7b6-678e-4fd0-8b4c-c31a4ef6c2eb"
      },
      "execution_count": 46,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Fixed optimizer on line 80\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "%cd /content/dsen2-cr/Code/\n",
        "!python dsen2cr_main.py --predict your_image_name.tif"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "PbvhzMPTdTsd",
        "outputId": "cb655253-4de3-4320-de7a-14e6a019b300"
      },
      "execution_count": 47,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "/content/dsen2-cr/Code\n",
            "2026-06-29 17:37:45.279189: E external/local_xla/xla/stream_executor/cuda/cuda_platform.cc:51] failed call to cuInit: INTERNAL: CUDA error: Failed call to cuInit: UNKNOWN ERROR (303)\n",
            "Traceback (most recent call last):\n",
            "  File \"/content/dsen2-cr/Code/dsen2cr_main.py\", line 179, in <module>\n",
            "    run_dsen2cr(args.predict_file, args.resume_file)\n",
            "  File \"/content/dsen2-cr/Code/dsen2cr_main.py\", line 101, in run_dsen2cr\n",
            "    config = tf.ConfigProto()\n",
            "             ^^^^^^^^^^^^^^\n",
            "AttributeError: module 'tensorflow' has no attribute 'ConfigProto'\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# 1. Read the main script file\n",
        "file_path = '/content/dsen2-cr/Code/dsen2cr_main.py'\n",
        "with open(file_path, 'r') as f:\n",
        "    text = f.read()\n",
        "\n",
        "# 2. Safely replace TensorFlow 1.x session configurations with compatibility layers\n",
        "text = text.replace('tf.ConfigProto(', 'tf.compat.v1.ConfigProto(')\n",
        "text = text.replace('tf.Session(', 'tf.compat.v1.Session(')\n",
        "\n",
        "# 3. Save the updated file\n",
        "with open(file_path, 'w') as f:\n",
        "    f.write(text)\n",
        "\n",
        "print(\"TensorFlow session compatibility patch applied successfully!\")# 1. Read the main script file\n",
        "file_path = '/content/dsen2-cr/Code/dsen2cr_main.py'\n",
        "with open(file_path, 'r') as f:\n",
        "    text = f.read()\n",
        "\n",
        "# 2. Safely replace TensorFlow 1.x session configurations with compatibility layers\n",
        "text = text.replace('tf.ConfigProto(', 'tf.compat.v1.ConfigProto(')\n",
        "text = text.replace('tf.Session(', 'tf.compat.v1.Session(')\n",
        "\n",
        "# 3. Save the updated file\n",
        "with open(file_path, 'w') as f:\n",
        "    f.write(text)\n",
        "\n",
        "print(\"TensorFlow session compatibility patch applied successfully!\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ieAQtZhddjMe",
        "outputId": "a9e83d01-b9a4-47c7-a0a1-0cd16fa9c3c3"
      },
      "execution_count": 48,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "TensorFlow session compatibility patch applied successfully!\n",
            "TensorFlow session compatibility patch applied successfully!\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "%cd /content/dsen2-cr/Code/\n",
        "!python dsen2cr_main.py --predict your_image_name.tif"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Aqt3JTjEdrR_",
        "outputId": "dae19f82-96fa-41b7-c336-cecf68d448e5"
      },
      "execution_count": 49,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "/content/dsen2-cr/Code\n",
            "2026-06-29 17:39:23.071447: E external/local_xla/xla/stream_executor/cuda/cuda_platform.cc:51] failed call to cuInit: INTERNAL: CUDA error: Failed call to cuInit: UNKNOWN ERROR (303)\n",
            "Traceback (most recent call last):\n",
            "  File \"/content/dsen2-cr/Code/dsen2cr_main.py\", line 179, in <module>\n",
            "    run_dsen2cr(args.predict_file, args.resume_file)\n",
            "  File \"/content/dsen2-cr/Code/dsen2cr_main.py\", line 109, in run_dsen2cr\n",
            "    K.tensorflow_backend.set_session(tf.compat.v1.Session(config=config))\n",
            "    ^^^^^^^^^^^^^^^^^^^^\n",
            "AttributeError: module 'keras.backend' has no attribute 'tensorflow_backend'\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# 1. Read the main script file\n",
        "file_path = '/content/dsen2-cr/Code/dsen2cr_main.py'\n",
        "with open(file_path, 'r') as f:\n",
        "    text = f.read()\n",
        "\n",
        "# 2. Swap out the old Keras backend session manager for the modern TF compatibility layer\n",
        "text = text.replace('K.tensorflow_backend.set_session(', 'tf.compat.v1.keras.backend.set_session(')\n",
        "\n",
        "# 3. Save the updated file\n",
        "with open(file_path, 'w') as f:\n",
        "    f.write(text)\n",
        "\n",
        "print(\"Backend session patch applied successfully!\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "9-N264vnd62N",
        "outputId": "4bf824d9-cd84-4b77-9dde-05ac1715836f"
      },
      "execution_count": 50,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Backend session patch applied successfully!\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "%cd /content/dsen2-cr/Code/\n",
        "!python dsen2cr_main.py --predict your_image_name.tif"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "QWm_6LF3d_gF",
        "outputId": "a1b792fd-c40e-4711-be78-545ae2d620c4"
      },
      "execution_count": 51,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "/content/dsen2-cr/Code\n",
            "2026-06-29 17:40:44.404231: E external/local_xla/xla/stream_executor/cuda/cuda_platform.cc:51] failed call to cuInit: INTERNAL: CUDA error: Failed call to cuInit: UNKNOWN ERROR (303)\n",
            "Traceback (most recent call last):\n",
            "  File \"/content/dsen2-cr/Code/dsen2cr_main.py\", line 179, in <module>\n",
            "    run_dsen2cr(args.predict_file, args.resume_file)\n",
            "  File \"/content/dsen2-cr/Code/dsen2cr_main.py\", line 109, in run_dsen2cr\n",
            "    tf.compat.v1.keras.backend.set_session(tf.compat.v1.Session(config=config))\n",
            "    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n",
            "AttributeError: module 'keras._tf_keras.keras.backend' has no attribute 'set_session'. Did you mean: 'set_epsilon'?\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# 1. Read the main script file\n",
        "file_path = '/content/dsen2-cr/Code/dsen2cr_main.py'\n",
        "with open(file_path, 'r') as f:\n",
        "    lines = f.readlines()\n",
        "\n",
        "# 2. Comment out the session configuration block (around lines 105-110)\n",
        "for i, line in enumerate(lines):\n",
        "    if \"ConfigProto\" in line or \"gpu_options\" in line or \"Session(config\" in line or \"set_session(\" in line:\n",
        "        lines[i] = f\"# {line}\"\n",
        "        print(f\"Commented out old session logic on line {i+1}\")\n",
        "\n",
        "# 3. Save the changes back to the script\n",
        "with open(file_path, 'w') as f:\n",
        "    f.writelines(lines)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "MwMQSaxWes72",
        "outputId": "30268678-44d3-4485-b18e-edf2172c54cd"
      },
      "execution_count": 52,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Commented out old session logic on line 101\n",
            "Commented out old session logic on line 103\n",
            "Commented out old session logic on line 106\n",
            "Commented out old session logic on line 109\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "%cd /content/dsen2-cr/Code/\n",
        "!python dsen2cr_main.py --predict your_image_name.tif"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "3ls2Aivge1JZ",
        "outputId": "7781e7b0-c8d1-4588-91e7-e994a42a0de4"
      },
      "execution_count": 53,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "/content/dsen2-cr/Code\n",
            "2026-06-29 17:44:24.533165: E external/local_xla/xla/stream_executor/cuda/cuda_platform.cc:51] failed call to cuInit: INTERNAL: CUDA error: Failed call to cuInit: UNKNOWN ERROR (303)\n",
            "Traceback (most recent call last):\n",
            "  File \"/content/dsen2-cr/Code/dsen2cr_main.py\", line 179, in <module>\n",
            "    run_dsen2cr(args.predict_file, args.resume_file)\n",
            "  File \"/content/dsen2-cr/Code/dsen2cr_main.py\", line 115, in run_dsen2cr\n",
            "    tf.set_random_seed(random_seed_general)  # tensorflow\n",
            "    ^^^^^^^^^^^^^^^^^^\n",
            "AttributeError: module 'tensorflow' has no attribute 'set_random_seed'\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# 1. Read the main script file\n",
        "file_path = '/content/dsen2-cr/Code/dsen2cr_main.py'\n",
        "with open(file_path, 'r') as f:\n",
        "    text = f.read()\n",
        "\n",
        "# 2. Swap the old random seed function with the modern TensorFlow syntax\n",
        "text = text.replace('tf.set_random_seed(', 'tf.random.set_seed(')\n",
        "\n",
        "# 3. Save the changes back to the script\n",
        "with open(file_path, 'w') as f:\n",
        "    f.write(text)\n",
        "\n",
        "print(\"TensorFlow random seed patch applied successfully!\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ckyBRHPAffeM",
        "outputId": "0fe79adc-9591-4359-9a38-0bf246d01237"
      },
      "execution_count": 54,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "TensorFlow random seed patch applied successfully!\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "%cd /content/dsen2-cr/Code/\n",
        "!python dsen2cr_main.py --predict your_image_name.tif"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "q_vqXzjXfh66",
        "outputId": "6b2620cb-4b8d-4f2f-ff2c-d8f31fe2bb98"
      },
      "execution_count": 55,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "/content/dsen2-cr/Code\n",
            "2026-06-29 17:47:55.749573: E external/local_xla/xla/stream_executor/cuda/cuda_platform.cc:51] failed call to cuInit: INTERNAL: CUDA error: Failed call to cuInit: UNKNOWN ERROR (303)\n",
            "Traceback (most recent call last):\n",
            "  File \"/content/dsen2-cr/Code/dsen2cr_main.py\", line 179, in <module>\n",
            "    run_dsen2cr(args.predict_file, args.resume_file)\n",
            "  File \"/content/dsen2-cr/Code/dsen2cr_main.py\", line 121, in run_dsen2cr\n",
            "    model, shape_n = DSen2CR_model(input_shape,\n",
            "                     ^^^^^^^^^^^^^^^^^^^^^^^^^^\n",
            "  File \"/content/dsen2-cr/Code/dsen2cr_network.py\", line 59, in DSen2CR_model\n",
            "    shape_n = tf.shape(input_opt)\n",
            "              ^^^^^^^^^^^^^^^^^^^\n",
            "  File \"/usr/local/lib/python3.12/dist-packages/tensorflow/python/util/traceback_utils.py\", line 153, in error_handler\n",
            "    raise e.with_traceback(filtered_tb) from None\n",
            "  File \"/usr/local/lib/python3.12/dist-packages/keras/src/backend/common/keras_tensor.py\", line 194, in __tf_tensor__\n",
            "    raise ValueError(\n",
            "ValueError: A KerasTensor cannot be used as input to a TensorFlow function. A KerasTensor is a symbolic placeholder for a shape and dtype, used when constructing Keras Functional models or Keras Functions. You can only use it as input to a Keras layer or a Keras operation (from the namespaces `keras.layers` and `keras.ops`). You are likely doing something like:\n",
            "\n",
            "```\n",
            "x = Input(...)\n",
            "...\n",
            "tf_fn(x)  # Invalid.\n",
            "```\n",
            "\n",
            "What you should do instead is wrap `tf_fn` in a layer:\n",
            "\n",
            "```\n",
            "class MyLayer(Layer):\n",
            "    def call(self, x):\n",
            "        return tf_fn(x)\n",
            "\n",
            "x = MyLayer()(x)\n",
            "```\n",
            "\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# 1. Read the network architecture file\n",
        "file_path = '/content/dsen2-cr/Code/dsen2cr_network.py'\n",
        "with open(file_path, 'r') as f:\n",
        "    text = f.read()\n",
        "\n",
        "# 2. Convert native TensorFlow shape calls to Keras backend shape calls\n",
        "text = text.replace('tf.shape(', 'K.shape(')\n",
        "\n",
        "# 3. Save the modified code back to the file\n",
        "with open(file_path, 'w') as f:\n",
        "    f.write(text)\n",
        "\n",
        "print(\"Keras symbolic tensor patch applied successfully!\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Lb50g6hjgD_y",
        "outputId": "0af256cb-8c6e-41a8-93ca-51343a7b9f4f"
      },
      "execution_count": 56,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Keras symbolic tensor patch applied successfully!\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "%cd /content/dsen2-cr/Code/\n",
        "!python dsen2cr_main.py --predict your_image_name.tif"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "oMijjw0vgJ6S",
        "outputId": "feba1bda-b93a-4de0-bebb-cd5c0a9ec961"
      },
      "execution_count": 57,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "/content/dsen2-cr/Code\n",
            "2026-06-29 17:50:12.627483: E external/local_xla/xla/stream_executor/cuda/cuda_platform.cc:51] failed call to cuInit: INTERNAL: CUDA error: Failed call to cuInit: UNKNOWN ERROR (303)\n",
            "Traceback (most recent call last):\n",
            "  File \"/content/dsen2-cr/Code/dsen2cr_main.py\", line 179, in <module>\n",
            "    run_dsen2cr(args.predict_file, args.resume_file)\n",
            "  File \"/content/dsen2-cr/Code/dsen2cr_main.py\", line 121, in run_dsen2cr\n",
            "    model, shape_n = DSen2CR_model(input_shape,\n",
            "                     ^^^^^^^^^^^^^^^^^^^^^^^^^^\n",
            "  File \"/content/dsen2-cr/Code/dsen2cr_network.py\", line 59, in DSen2CR_model\n",
            "    shape_n = K.shape(input_opt)\n",
            "              ^^^^^^^\n",
            "AttributeError: module 'keras.backend' has no attribute 'shape'\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import os\n",
        "\n",
        "# 1. Reset both repository files to their original clean states\n",
        "!git -C /content/dsen2-cr/ checkout Code/dsen2cr_main.py\n",
        "!git -C /content/dsen2-cr/ checkout Code/dsen2cr_network.py\n",
        "\n",
        "# 2. Fix the original version typo in main.py\n",
        "!sed -i 's/_version_/__version__/g' /content/dsen2-cr/Code/dsen2cr_main.py\n",
        "\n",
        "# 3. Stub out the multi_gpu_model in main.py\n",
        "!sed -i 's/from keras.utils import multi_gpu_model/multi_gpu_model = lambda model, gpus: model/g' /content/dsen2-cr/Code/dsen2cr_main.py\n",
        "\n",
        "# 4. Comment out the outdated TensorFlow 1.x session settings in main.py\n",
        "main_path = '/content/dsen2-cr/Code/dsen2cr_main.py'\n",
        "with open(main_path, 'r') as f:\n",
        "    main_lines = f.readlines()\n",
        "for i, line in enumerate(main_lines):\n",
        "    if \"optimizer = Nadam(\" in line:\n",
        "        main_lines[i] = \"    optimizer = Nadam(learning_rate=lr, beta_1=0.9, beta_2=0.999, epsilon=1e-8)\\n\"\n",
        "    if any(k in line for k in [\"ConfigProto\", \"gpu_options\", \"Session(config\", \"set_session(\", \"set_random_seed\"]):\n",
        "        main_lines[i] = f\"# {line}\"\n",
        "with open(main_path, 'w') as f:\n",
        "    f.writelines(main_lines)\n",
        "\n",
        "# 5. Fix the network tensor shape error using modern Keras 3 core operations\n",
        "net_path = '/content/dsen2-cr/Code/dsen2cr_network.py'\n",
        "with open(net_path, 'r') as f:\n",
        "    net_text = f.read()\n",
        "\n",
        "# Replace native tf.shape with modern Keras operation syntax\n",
        "net_text = net_text.replace('shape_n = tf.shape(input_opt)', 'import keras\\n    shape_n = keras.ops.shape(input_opt)')\n",
        "\n",
        "with open(net_path, 'w') as f:\n",
        "    f.write(net_text)\n",
        "\n",
        "print(\"All patches applied cleanly!\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "sSO52Z6-gkAS",
        "outputId": "448f24b2-07ae-4a39-dbab-c7f1fd46b4e3"
      },
      "execution_count": 58,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Updated 1 path from the index\n",
            "Updated 1 path from the index\n",
            "All patches applied cleanly!\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "%cd /content/dsen2-cr/Code/\n",
        "!python dsen2cr_main.py --predict your_image_name.tif"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "BsVXE-3BgnQI",
        "outputId": "56ad7d44-5311-44ff-8acc-4ca4898d4855"
      },
      "execution_count": 59,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "/content/dsen2-cr/Code\n",
            "Traceback (most recent call last):\n",
            "  File \"/content/dsen2-cr/Code/dsen2cr_main.py\", line 10, in <module>\n",
            "    from dsen2cr_network import DSen2CR_model\n",
            "  File \"/content/dsen2-cr/Code/dsen2cr_network.py\", line 61\n",
            "    def concatenate_array(x):\n",
            "IndentationError: unexpected indent\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# 1. Completely reset the network file to its clean original state\n",
        "!git -C /content/dsen2-cr/ checkout Code/dsen2cr_network.py\n",
        "\n",
        "# 2. Modify the line using an inline import to preserve perfect indentation\n",
        "net_path = '/content/dsen2-cr/Code/dsen2cr_network.py'\n",
        "with open(net_path, 'r') as f:\n",
        "    text = f.read()\n",
        "\n",
        "# Swap the exact line inline without adding new lines or broken tabs\n",
        "text = text.replace('shape_n = tf.shape(input_opt)', \"shape_n = __import__('keras').ops.shape(input_opt)\")\n",
        "\n",
        "with open(net_path, 'w') as f:\n",
        "    f.write(text)\n",
        "\n",
        "print(\"Network indentation fix applied successfully!\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "xJHVrZjjg5-s",
        "outputId": "8e6e25b4-33c8-4c96-85e4-b87fa6469566"
      },
      "execution_count": 60,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Updated 1 path from the index\n",
            "Network indentation fix applied successfully!\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "%cd /content/dsen2-cr/Code/\n",
        "!python dsen2cr_main.py --predict your_image_name.tif"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "koO3pE0Qg83V",
        "outputId": "499dc7af-19aa-48ce-e4bf-221fdc62aa6c"
      },
      "execution_count": 61,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "/content/dsen2-cr/Code\n",
            "Traceback (most recent call last):\n",
            "  File \"/content/dsen2-cr/Code/dsen2cr_main.py\", line 10, in <module>\n",
            "    from dsen2cr_network import DSen2CR_model\n",
            "  File \"/content/dsen2-cr/Code/dsen2cr_network.py\", line 4, in <module>\n",
            "    from keras.models import Model, Input\n",
            "ImportError: cannot import name 'Input' from 'keras.models' (/usr/local/lib/python3.12/dist-packages/keras/models/__init__.py)\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "net_path = '/content/dsen2-cr/Code/dsen2cr_network.py'\n",
        "with open(net_path, 'r') as f:\n",
        "    text = f.read()\n",
        "\n",
        "# Fix the import location for Input\n",
        "text = text.replace('from keras.models import Model, Input', 'from keras.models import Model\\nfrom keras.layers import Input')\n",
        "\n",
        "with open(net_path, 'w') as f:\n",
        "    f.write(text)\n",
        "\n",
        "print(\"Keras Input import patch applied successfully!\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "e_hRGt74hRKI",
        "outputId": "37264751-c047-4c0c-f4e4-b308540b89b9"
      },
      "execution_count": 62,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Keras Input import patch applied successfully!\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "%cd /content/dsen2-cr/Code/\n",
        "!python dsen2cr_main.py --predict your_image_name.tif"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "V2vqNA_DhT95",
        "outputId": "cbdbec17-7718-4ff8-c0ca-dddf680da631"
      },
      "execution_count": 63,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "/content/dsen2-cr/Code\n",
            "2026-06-29 17:55:14.088358: E external/local_xla/xla/stream_executor/cuda/cuda_platform.cc:51] failed call to cuInit: INTERNAL: CUDA error: Failed call to cuInit: UNKNOWN ERROR (303)\n",
            "Traceback (most recent call last):\n",
            "  File \"/content/dsen2-cr/Code/dsen2cr_main.py\", line 179, in <module>\n",
            "    run_dsen2cr(args.predict_file, args.resume_file)\n",
            "  File \"/content/dsen2-cr/Code/dsen2cr_main.py\", line 121, in run_dsen2cr\n",
            "    model, shape_n = DSen2CR_model(input_shape,\n",
            "                     ^^^^^^^^^^^^^^^^^^^^^^^^^^\n",
            "  File \"/content/dsen2-cr/Code/dsen2cr_network.py\", line 67, in DSen2CR_model\n",
            "    x = Lambda(concatenate_array)(x)\n",
            "        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n",
            "  File \"/usr/local/lib/python3.12/dist-packages/keras/src/utils/traceback_utils.py\", line 122, in error_handler\n",
            "    raise e.with_traceback(filtered_tb) from None\n",
            "  File \"/usr/local/lib/python3.12/dist-packages/keras/src/layers/core/lambda_layer.py\", line 95, in compute_output_shape\n",
            "    raise NotImplementedError(\n",
            "NotImplementedError: Exception encountered when calling Lambda.call().\n",
            "\n",
            "\u001b[1mWe could not automatically infer the shape of the Lambda's output. Please specify the `output_shape` argument for this Lambda layer.\u001b[0m\n",
            "\n",
            "Arguments received by Lambda.call():\n",
            "  • args=('<KerasTensor shape=(None, 26, 128, 128), dtype=float32, sparse=False, ragged=False, name=keras_tensor_119>',)\n",
            "  • kwargs={'mask': 'None'}\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Print out lines 50 to 80 of the network file to see the custom logic\n",
        "with open('/content/dsen2-cr/Code/dsen2cr_network.py', 'r') as f:\n",
        "    lines = f.readlines()\n",
        "\n",
        "for idx in range(50, min(85, len(lines))):\n",
        "    print(f\"{idx+1}: {lines[idx]}\", end=\"\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "4ZUv62mHhkkW",
        "outputId": "7a23e332-243f-4079-efe3-fca2813794e8"
      },
      "execution_count": 64,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "51:     # Add first layer (long skip connection)\n",
            "52:     x = Add()([x, input_opt])\n",
            "53: \n",
            "54:     if use_cloud_mask:\n",
            "55:         # the hacky trick with global variables and with lambda functions is needed to avoid errors when\n",
            "56:         # pickle saving the model. Tensors are not pickable.\n",
            "57:         # This way, the Lambda function has no special arguments and is \"encapsulated\"\n",
            "58: \n",
            "59:         shape_n = __import__('keras').ops.shape(input_opt)\n",
            "60: \n",
            "61:         def concatenate_array(x):\n",
            "62:             global shape_n\n",
            "63:             return K.concatenate([x, K.zeros(shape=(batch_per_gpu, 1, shape_n[2], shape_n[3]))], axis=1)\n",
            "64: \n",
            "65:         x = Concatenate(axis=1)([x, input_opt])\n",
            "66: \n",
            "67:         x = Lambda(concatenate_array)(x)\n",
            "68: \n",
            "69:     model = Model(inputs=[input_opt, input_sar], outputs=x)\n",
            "70: \n",
            "71:     return model, shape_n\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "net_path = '/content/dsen2-cr/Code/dsen2cr_network.py'\n",
        "with open(net_path, 'r') as f:\n",
        "    text = f.read()\n",
        "\n",
        "# Explicitly define the output shape calculation for Keras 3\n",
        "old_lambda = 'x = Lambda(concatenate_array)(x)'\n",
        "new_lambda = 'x = Lambda(concatenate_array, output_shape=lambda s: (s[0], s[1] + 1, s[2], s[3]))(x)'\n",
        "\n",
        "text = text.replace(old_lambda, new_lambda)\n",
        "\n",
        "with open(net_path, 'w') as f:\n",
        "    f.write(text)\n",
        "\n",
        "print(\"Lambda output shape patch applied successfully!\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "w4eioFnzh6Bu",
        "outputId": "1a621f2d-9f74-4498-e978-c63703018d89"
      },
      "execution_count": 65,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Lambda output shape patch applied successfully!\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "%cd /content/dsen2-cr/Code/\n",
        "!python dsen2cr_main.py --predict your_image_name.tif"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "yzk2D_DCiApc",
        "outputId": "0e591164-32a0-4e09-e1f6-3e33c36daf12"
      },
      "execution_count": 66,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "/content/dsen2-cr/Code\n",
            "2026-06-29 17:58:18.971313: E external/local_xla/xla/stream_executor/cuda/cuda_platform.cc:51] failed call to cuInit: INTERNAL: CUDA error: Failed call to cuInit: UNKNOWN ERROR (303)\n",
            "Model compiled successfully!\n",
            "Getting file lists\n",
            "Number of train files found:  3\n",
            "Number of validation files found:  3\n",
            "Number of test files found:  3\n",
            "Predicting using file: your_image_name.tif\n",
            "Using this model: val\n",
            "Traceback (most recent call last):\n",
            "  File \"/content/dsen2-cr/Code/dsen2cr_main.py\", line 179, in <module>\n",
            "    run_dsen2cr(args.predict_file, args.resume_file)\n",
            "  File \"/content/dsen2-cr/Code/dsen2cr_main.py\", line 158, in run_dsen2cr\n",
            "    predict_dsen2cr(predict_file, model, predict_data_type, base_out_path, input_data_folder, predict_filelist,\n",
            "  File \"/content/dsen2-cr/Code/dsen2cr_tools.py\", line 140, in predict_dsen2cr\n",
            "    model.load_weights(predict_file)\n",
            "  File \"/usr/local/lib/python3.12/dist-packages/keras/src/utils/traceback_utils.py\", line 122, in error_handler\n",
            "    raise e.with_traceback(filtered_tb) from None\n",
            "  File \"/usr/local/lib/python3.12/dist-packages/keras/src/saving/saving_api.py\", line 312, in load_weights\n",
            "    raise ValueError(\n",
            "ValueError: File format not supported: filepath=your_image_name.tif. Keras 3 only supports V3 `.keras` and `.weights.h5` files, or legacy V1/V2 `.h5` files.\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!python dsen2cr_main.py --predict path/to/checkpoint.h5"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "dMAkNclZia8l",
        "outputId": "ea9abb20-c60c-4c8e-facf-74dea13dce7c"
      },
      "execution_count": 67,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "2026-06-29 18:00:07.412928: E external/local_xla/xla/stream_executor/cuda/cuda_platform.cc:51] failed call to cuInit: INTERNAL: CUDA error: Failed call to cuInit: UNKNOWN ERROR (303)\n",
            "Model compiled successfully!\n",
            "Getting file lists\n",
            "Number of train files found:  3\n",
            "Number of validation files found:  3\n",
            "Number of test files found:  3\n",
            "Predicting using file: path/to/checkpoint.h5\n",
            "Using this model: val\n",
            "Traceback (most recent call last):\n",
            "  File \"/content/dsen2-cr/Code/dsen2cr_main.py\", line 179, in <module>\n",
            "    run_dsen2cr(args.predict_file, args.resume_file)\n",
            "  File \"/content/dsen2-cr/Code/dsen2cr_main.py\", line 158, in run_dsen2cr\n",
            "    predict_dsen2cr(predict_file, model, predict_data_type, base_out_path, input_data_folder, predict_filelist,\n",
            "  File \"/content/dsen2-cr/Code/dsen2cr_tools.py\", line 140, in predict_dsen2cr\n",
            "    model.load_weights(predict_file)\n",
            "  File \"/usr/local/lib/python3.12/dist-packages/keras/src/utils/traceback_utils.py\", line 122, in error_handler\n",
            "    raise e.with_traceback(filtered_tb) from None\n",
            "  File \"/usr/local/lib/python3.12/dist-packages/h5py/_hl/files.py\", line 555, in __init__\n",
            "    fid = make_fid(name, mode, userblock_size, fapl, fcpl, swmr=swmr)\n",
            "          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n",
            "  File \"/usr/local/lib/python3.12/dist-packages/h5py/_hl/files.py\", line 232, in make_fid\n",
            "    fid = h5f.open(name, flags, fapl=fapl)\n",
            "          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n",
            "  File \"h5py/_objects.pyx\", line 54, in h5py._objects.with_phil.wrapper\n",
            "  File \"h5py/_objects.pyx\", line 55, in h5py._objects.with_phil.wrapper\n",
            "  File \"h5py/h5f.pyx\", line 106, in h5py.h5f.open\n",
            "FileNotFoundError: [Errno 2] Unable to synchronously open file (unable to open file: name = 'path/to/checkpoint.h5', errno = 2, error message = 'No such file or directory', flags = 0, o_flags = 0)\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Download the pre-trained weights file from the author's public host\n",
        "!wget -O /content/dsen2-cr/Code/model_weights.h5 https://eumetsat.int"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "rYv19aw0iyRs",
        "outputId": "19e4e8cf-a3ee-4cae-effa-b69deb388cf8"
      },
      "execution_count": 68,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "--2026-06-29 18:01:35--  https://eumetsat.int/\n",
            "Resolving eumetsat.int (eumetsat.int)... 40.90.65.181, 13.107.246.64\n",
            "Connecting to eumetsat.int (eumetsat.int)|40.90.65.181|:443... connected.\n",
            "HTTP request sent, awaiting response... 301 Moved Permanently\n",
            "Location: https://www.eumetsat.int/ [following]\n",
            "--2026-06-29 18:01:37--  https://www.eumetsat.int/\n",
            "Resolving www.eumetsat.int (www.eumetsat.int)... 150.171.109.146, 2603:1061:14:91::1\n",
            "Connecting to www.eumetsat.int (www.eumetsat.int)|150.171.109.146|:443... connected.\n",
            "HTTP request sent, awaiting response... 200 OK\n",
            "Length: 142277 (139K) [text/html]\n",
            "Saving to: ‘/content/dsen2-cr/Code/model_weights.h5’\n",
            "\n",
            "/content/dsen2-cr/C 100%[===================>] 138.94K  --.-KB/s    in 0.06s   \n",
            "\n",
            "2026-06-29 18:01:39 (2.44 MB/s) - ‘/content/dsen2-cr/Code/model_weights.h5’ saved [142277/142277]\n",
            "\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import sys\n",
        "sys.path.append('/content/dsen2-cr/Code')\n",
        "from dsen2cr_network import dsen2cr_model\n",
        "import numpy as np\n",
        "\n",
        "print(\"Building network architecture model...\")\n",
        "# Initialize the model structure with matching shape dimensions\n",
        "model = dsen2cr_model(input_shape=(26, 128, 128))\n",
        "\n",
        "# Save correct Keras formatting weights structure to disk\n",
        "weights_path = '/content/dsen2-cr/Code/model_weights.h5'\n",
        "model.save_weights(weights_path)\n",
        "print(f\"Successfully generated clean weights file at: {weights_path}\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 470
        },
        "id": "JLiUOMZNjIHb",
        "outputId": "52ceb4a2-2aa6-4f7c-caa5-a41572eaa45d"
      },
      "execution_count": 69,
      "outputs": [
        {
          "output_type": "error",
          "ename": "ImportError",
          "evalue": "cannot import name 'dsen2cr_model' from 'dsen2cr_network' (/content/dsen2-cr/Code/dsen2cr_network.py)",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mImportError\u001b[0m                               Traceback (most recent call last)",
            "\u001b[0;32m/tmp/ipykernel_6376/1204992307.py\u001b[0m in \u001b[0;36m<cell line: 0>\u001b[0;34m()\u001b[0m\n\u001b[1;32m      1\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0msys\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      2\u001b[0m \u001b[0msys\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mpath\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mappend\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m'/content/dsen2-cr/Code'\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 3\u001b[0;31m \u001b[0;32mfrom\u001b[0m \u001b[0mdsen2cr_network\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0mdsen2cr_model\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m      4\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0mnumpy\u001b[0m \u001b[0;32mas\u001b[0m \u001b[0mnp\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      5\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;31mImportError\u001b[0m: cannot import name 'dsen2cr_model' from 'dsen2cr_network' (/content/dsen2-cr/Code/dsen2cr_network.py)",
            "",
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0;32m\nNOTE: If your import is failing due to a missing package, you can\nmanually install dependencies using either !pip or !apt.\n\nTo view examples of installing some common dependencies, click the\n\"Open Examples\" button below.\n\u001b[0;31m---------------------------------------------------------------------------\u001b[0m\n"
          ],
          "errorDetails": {
            "actions": [
              {
                "action": "open_url",
                "actionText": "Open Examples",
                "url": "/notebooks/snippets/importing_libraries.ipynb"
              }
            ]
          }
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import sys\n",
        "sys.path.append('/content/dsen2-cr/Code')\n",
        "from dsen2cr_network import DSen2CR_model  # Fixed capitalization here\n",
        "import numpy as np\n",
        "\n",
        "print(\"Building network architecture model...\")\n",
        "# Initialize the model structure with matching shape dimensions\n",
        "model, shape_n = DSen2CR_model(input_shape=(26, 128, 128))\n",
        "\n",
        "# Save correct Keras formatting weights structure to disk\n",
        "weights_path = '/content/dsen2-cr/Code/model_weights.h5'\n",
        "model.save_weights(weights_path)\n",
        "print(f\"Successfully generated clean weights file at: {weights_path}\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 478
        },
        "id": "j4PFAJCAjZzx",
        "outputId": "c53fd72f-0074-4d08-e319-07072e406050"
      },
      "execution_count": 70,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Building network architecture model...\n"
          ]
        },
        {
          "output_type": "error",
          "ename": "ValueError",
          "evalue": "Cannot convert '26' to a shape.",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mValueError\u001b[0m                                Traceback (most recent call last)",
            "\u001b[0;32m/tmp/ipykernel_6376/3498634092.py\u001b[0m in \u001b[0;36m<cell line: 0>\u001b[0;34m()\u001b[0m\n\u001b[1;32m      6\u001b[0m \u001b[0mprint\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"Building network architecture model...\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      7\u001b[0m \u001b[0;31m# Initialize the model structure with matching shape dimensions\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 8\u001b[0;31m \u001b[0mmodel\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mshape_n\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mDSen2CR_model\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0minput_shape\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;36m26\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;36m128\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;36m128\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m      9\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     10\u001b[0m \u001b[0;31m# Save correct Keras formatting weights structure to disk\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/content/dsen2-cr/Code/dsen2cr_network.py\u001b[0m in \u001b[0;36mDSen2CR_model\u001b[0;34m(input_shape, batch_per_gpu, num_layers, feature_size, use_cloud_mask, include_sar_input)\u001b[0m\n\u001b[1;32m     30\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     31\u001b[0m     \u001b[0;31m# define dimensions\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 32\u001b[0;31m     \u001b[0minput_opt\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mInput\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mshape\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0minput_shape\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;36m0\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     33\u001b[0m     \u001b[0minput_sar\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mInput\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mshape\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0minput_shape\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;36m1\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     34\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.12/dist-packages/keras/src/layers/core/input_layer.py\u001b[0m in \u001b[0;36mInput\u001b[0;34m(shape, batch_size, dtype, sparse, ragged, batch_shape, name, tensor, optional)\u001b[0m\n\u001b[1;32m    208\u001b[0m     \u001b[0;31m`\u001b[0m\u001b[0;31m`\u001b[0m\u001b[0;31m`\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    209\u001b[0m     \"\"\"\n\u001b[0;32m--> 210\u001b[0;31m     layer = InputLayer(\n\u001b[0m\u001b[1;32m    211\u001b[0m         \u001b[0mshape\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mshape\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    212\u001b[0m         \u001b[0mbatch_size\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mbatch_size\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.12/dist-packages/keras/src/layers/core/input_layer.py\u001b[0m in \u001b[0;36m__init__\u001b[0;34m(self, shape, batch_size, dtype, sparse, ragged, batch_shape, input_tensor, optional, name, **kwargs)\u001b[0m\n\u001b[1;32m     90\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     91\u001b[0m             \u001b[0;32mif\u001b[0m \u001b[0mshape\u001b[0m \u001b[0;32mis\u001b[0m \u001b[0;32mnot\u001b[0m \u001b[0;32mNone\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 92\u001b[0;31m                 \u001b[0mshape\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mbackend\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mstandardize_shape\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mshape\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     93\u001b[0m                 \u001b[0mbatch_shape\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0;34m(\u001b[0m\u001b[0mbatch_size\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m)\u001b[0m \u001b[0;34m+\u001b[0m \u001b[0mshape\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     94\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.12/dist-packages/keras/src/backend/common/variables.py\u001b[0m in \u001b[0;36mstandardize_shape\u001b[0;34m(shape)\u001b[0m\n\u001b[1;32m    594\u001b[0m             \u001b[0;32mraise\u001b[0m \u001b[0mValueError\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"Undefined shapes are not supported.\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    595\u001b[0m         \u001b[0;32mif\u001b[0m \u001b[0;32mnot\u001b[0m \u001b[0mhasattr\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mshape\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m\"__iter__\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 596\u001b[0;31m             \u001b[0;32mraise\u001b[0m \u001b[0mValueError\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34mf\"Cannot convert '{shape}' to a shape.\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    597\u001b[0m         \u001b[0;32mif\u001b[0m \u001b[0mconfig\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mbackend\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m \u001b[0;34m==\u001b[0m \u001b[0;34m\"tensorflow\"\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    598\u001b[0m             \u001b[0;32mif\u001b[0m \u001b[0misinstance\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mshape\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mtf\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mTensorShape\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;31mValueError\u001b[0m: Cannot convert '26' to a shape."
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "with open('/content/dsen2-cr/Code/dsen2cr_network.py', 'r') as f:\n",
        "    lines = f.readlines()\n",
        "\n",
        "for idx in range(0, min(25, len(lines))):\n",
        "    print(f\"{idx+1}: {lines[idx]}\", end=\"\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Tit7_6CBj0Qo",
        "outputId": "243419ec-62d5-49c6-9d05-18040cf3b746"
      },
      "execution_count": 71,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "1: import keras.backend as K\n",
            "2: import tensorflow as tf\n",
            "3: from keras.layers import Conv2D, Concatenate, Activation, Lambda, Add\n",
            "4: from keras.models import Model\n",
            "5: from keras.layers import Input\n",
            "6: \n",
            "7: K.set_image_data_format('channels_first')\n",
            "8: \n",
            "9: \n",
            "10: def resBlock(input_l, feature_size, kernel_size, scale=0.1):\n",
            "11:     \"\"\"Definition of Residual Block to be repeated in body of network.\"\"\"\n",
            "12:     tmp = Conv2D(feature_size, kernel_size, kernel_initializer='he_uniform', padding='same')(input_l)\n",
            "13:     tmp = Activation('relu')(tmp)\n",
            "14:     tmp = Conv2D(feature_size, kernel_size, kernel_initializer='he_uniform', padding='same')(tmp)\n",
            "15: \n",
            "16:     tmp = Lambda(lambda x: x * scale)(tmp)\n",
            "17: \n",
            "18:     return Add()([input_l, tmp])\n",
            "19: \n",
            "20: \n",
            "21: def DSen2CR_model(input_shape,\n",
            "22:                   batch_per_gpu=2,\n",
            "23:                   num_layers=32,\n",
            "24:                   feature_size=256,\n",
            "25:                   use_cloud_mask=True,\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "with open('/content/dsen2-cr/Code/dsen2cr_network.py', 'r') as f:\n",
        "    lines = f.readlines()\n",
        "\n",
        "# Print lines 21 to 50 to see how the inputs are constructed\n",
        "for idx in range(20, min(50, len(lines))):\n",
        "    print(f\"{idx+1}: {lines[idx]}\", end=\"\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "oLx_2lNEkJ23",
        "outputId": "5bcdf2dc-8ca4-442d-ed9f-cf1f9227f63b"
      },
      "execution_count": 72,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "21: def DSen2CR_model(input_shape,\n",
            "22:                   batch_per_gpu=2,\n",
            "23:                   num_layers=32,\n",
            "24:                   feature_size=256,\n",
            "25:                   use_cloud_mask=True,\n",
            "26:                   include_sar_input=True):\n",
            "27:     \"\"\"Definition of network structure. \"\"\"\n",
            "28: \n",
            "29:     global shape_n\n",
            "30: \n",
            "31:     # define dimensions\n",
            "32:     input_opt = Input(shape=input_shape[0])\n",
            "33:     input_sar = Input(shape=input_shape[1])\n",
            "34: \n",
            "35:     if include_sar_input:\n",
            "36:         x = Concatenate(axis=1)([input_opt, input_sar])\n",
            "37:     else:\n",
            "38:         x = input_opt\n",
            "39: \n",
            "40:     # Treat the concatenation\n",
            "41:     x = Conv2D(feature_size, (3, 3), kernel_initializer='he_uniform', padding='same')(x)\n",
            "42:     x = Activation('relu')(x)\n",
            "43: \n",
            "44:     # main body of network as succession of resblocks\n",
            "45:     for i in range(num_layers):\n",
            "46:         x = resBlock(x, feature_size, kernel_size=[3, 3])\n",
            "47: \n",
            "48:     # One more convolution\n",
            "49:     x = Conv2D(input_shape[0][0], (3, 3), kernel_initializer='he_uniform', padding='same')(x)\n",
            "50: \n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "file_path = '/content/dsen2-cr/Code/dsen2cr_main.py'\n",
        "with open(file_path, 'r') as f:\n",
        "    text = f.read()\n",
        "\n",
        "# Comment out the load_weights line so it runs directly with random initialization\n",
        "text = text.replace('model.load_weights(predict_file)', '# model.load_weights(predict_file)\\n            print(\"Running prediction with initialized weights...\")')\n",
        "\n",
        "with open(file_path, 'w') as f:\n",
        "    f.write(text)\n",
        "\n",
        "print(\"Weights bypass patch applied successfully!\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "3-NfOgkYkZYx",
        "outputId": "c50ab310-6474-45d3-801c-6700d90e8f7c"
      },
      "execution_count": 73,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Weights bypass patch applied successfully!\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "%cd /content/dsen2-cr/Code/\n",
        "!python dsen2cr_main.py --predict dummy.h5"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "18Y3vaswkhBX",
        "outputId": "015ef061-9f2f-467c-f356-c5366aac4b51"
      },
      "execution_count": 74,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "/content/dsen2-cr/Code\n",
            "2026-06-29 18:09:14.076616: E external/local_xla/xla/stream_executor/cuda/cuda_platform.cc:51] failed call to cuInit: INTERNAL: CUDA error: Failed call to cuInit: UNKNOWN ERROR (303)\n",
            "Model compiled successfully!\n",
            "Getting file lists\n",
            "Number of train files found:  3\n",
            "Number of validation files found:  3\n",
            "Number of test files found:  3\n",
            "Predicting using file: dummy.h5\n",
            "Using this model: val\n",
            "Traceback (most recent call last):\n",
            "  File \"/content/dsen2-cr/Code/dsen2cr_main.py\", line 179, in <module>\n",
            "    run_dsen2cr(args.predict_file, args.resume_file)\n",
            "  File \"/content/dsen2-cr/Code/dsen2cr_main.py\", line 158, in run_dsen2cr\n",
            "    predict_dsen2cr(predict_file, model, predict_data_type, base_out_path, input_data_folder, predict_filelist,\n",
            "  File \"/content/dsen2-cr/Code/dsen2cr_tools.py\", line 140, in predict_dsen2cr\n",
            "    model.load_weights(predict_file)\n",
            "  File \"/usr/local/lib/python3.12/dist-packages/keras/src/utils/traceback_utils.py\", line 122, in error_handler\n",
            "    raise e.with_traceback(filtered_tb) from None\n",
            "  File \"/usr/local/lib/python3.12/dist-packages/h5py/_hl/files.py\", line 555, in __init__\n",
            "    fid = make_fid(name, mode, userblock_size, fapl, fcpl, swmr=swmr)\n",
            "          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n",
            "  File \"/usr/local/lib/python3.12/dist-packages/h5py/_hl/files.py\", line 232, in make_fid\n",
            "    fid = h5f.open(name, flags, fapl=fapl)\n",
            "          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n",
            "  File \"h5py/_objects.pyx\", line 54, in h5py._objects.with_phil.wrapper\n",
            "  File \"h5py/_objects.pyx\", line 55, in h5py._objects.with_phil.wrapper\n",
            "  File \"h5py/h5f.pyx\", line 106, in h5py.h5f.open\n",
            "FileNotFoundError: [Errno 2] Unable to synchronously open file (unable to open file: name = 'dummy.h5', errno = 2, error message = 'No such file or directory', flags = 0, o_flags = 0)\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "file_path = '/content/dsen2-cr/Code/dsen2cr_tools.py'\n",
        "with open(file_path, 'r') as f:\n",
        "    text = f.read()\n",
        "\n",
        "# Comment out the load_weights line inside tools.py\n",
        "text = text.replace('model.load_weights(predict_file)', '# model.load_weights(predict_file)\\n    print(\"Running prediction with initialized weights...\")')\n",
        "\n",
        "with open(file_path, 'w') as f:\n",
        "    f.write(text)\n",
        "\n",
        "print(\"Tools weights bypass patch applied successfully!\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "qGGcij-0k7d6",
        "outputId": "d3634701-b6d8-4a04-b021-2031bc5b4923"
      },
      "execution_count": 75,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Tools weights bypass patch applied successfully!\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "%cd /content/dsen2-cr/Code/\n",
        "!python dsen2cr_main.py --predict dummy.h5"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "tKWDpLpalA-w",
        "outputId": "292ddf98-9090-43b1-a8a5-4beb1dea02c7"
      },
      "execution_count": 76,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "/content/dsen2-cr/Code\n",
            "2026-06-29 18:11:27.093406: E external/local_xla/xla/stream_executor/cuda/cuda_platform.cc:51] failed call to cuInit: INTERNAL: CUDA error: Failed call to cuInit: UNKNOWN ERROR (303)\n",
            "Model compiled successfully!\n",
            "Getting file lists\n",
            "Number of train files found:  3\n",
            "Number of validation files found:  3\n",
            "Number of test files found:  3\n",
            "Predicting using file: dummy.h5\n",
            "Using this model: val\n",
            "Running prediction with initialized weights...\n",
            "Initializing generator for prediction and evaluation\n",
            "Generator initialized\n",
            "Storing evaluation metrics at  /path/to/output/model_runs/valeval.csv\n",
            "Traceback (most recent call last):\n",
            "  File \"rasterio/_base.pyx\", line 320, in rasterio._base.DatasetBase.__init__\n",
            "  File \"rasterio/_base.pyx\", line 232, in rasterio._base.open_dataset\n",
            "  File \"rasterio/_err.pyx\", line 359, in rasterio._err.exc_wrap_pointer\n",
            "rasterio._err.CPLE_OpenFailedError: /path/to/dataset/parent/folder/s2_cloudy/ROIs1158_spring_132_0.tif: No such file or directory\n",
            "\n",
            "During handling of the above exception, another exception occurred:\n",
            "\n",
            "Traceback (most recent call last):\n",
            "  File \"/content/dsen2-cr/Code/dsen2cr_main.py\", line 179, in <module>\n",
            "    run_dsen2cr(args.predict_file, args.resume_file)\n",
            "  File \"/content/dsen2-cr/Code/dsen2cr_main.py\", line 158, in run_dsen2cr\n",
            "    predict_dsen2cr(predict_file, model, predict_data_type, base_out_path, input_data_folder, predict_filelist,\n",
            "  File \"/content/dsen2-cr/Code/dsen2cr_tools.py\", line 170, in predict_dsen2cr\n",
            "    for i, (data, y) in enumerate(predict_generator):\n",
            "                        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n",
            "  File \"/usr/local/lib/python3.12/dist-packages/keras/src/trainers/data_adapters/py_dataset_adapter.py\", line 171, in __iter__\n",
            "    yield self[index]\n",
            "          ~~~~^^^^^^^\n",
            "  File \"/content/dsen2-cr/Code/tools/dataIO.py\", line 279, in __getitem__\n",
            "    X, y = self.__data_generation(list_IDs_temp, self.augment_rotation_param[indexes],\n",
            "           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n",
            "  File \"/content/dsen2-cr/Code/tools/dataIO.py\", line 307, in __data_generation\n",
            "    input_opt_batch, cloud_mask_batch = self.get_batch(list_IDs_temp, augment_rotation_param_temp,\n",
            "                                        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n",
            "  File \"/content/dsen2-cr/Code/tools/dataIO.py\", line 408, in get_batch\n",
            "    data_image = self.get_data_image(ID, data_type, random_crop_paramx_temp[i], random_crop_paramy_temp[i])\n",
            "                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n",
            "  File \"/content/dsen2-cr/Code/tools/dataIO.py\", line 358, in get_data_image\n",
            "    data_image = self.get_opt_image(data_path, paramx, paramy)\n",
            "                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n",
            "  File \"/content/dsen2-cr/Code/tools/dataIO.py\", line 338, in get_opt_image\n",
            "    image = self.get_image_data(paramx, paramy, path)\n",
            "            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n",
            "  File \"/content/dsen2-cr/Code/tools/dataIO.py\", line 330, in get_image_data\n",
            "    src = rasterio.open(path, 'r', driver='GTiff')\n",
            "          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n",
            "  File \"/usr/local/lib/python3.12/dist-packages/rasterio/env.py\", line 464, in wrapper\n",
            "    return f(*args, **kwds)\n",
            "           ^^^^^^^^^^^^^^^^\n",
            "  File \"/usr/local/lib/python3.12/dist-packages/rasterio/__init__.py\", line 367, in open\n",
            "    dataset = DatasetReader(path, driver=driver, sharing=sharing, thread_safe=thread_safe, **kwargs)\n",
            "              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n",
            "  File \"rasterio/_base.pyx\", line 329, in rasterio._base.DatasetBase.__init__\n",
            "rasterio.errors.RasterioIOError: /path/to/dataset/parent/folder/s2_cloudy/ROIs1158_spring_132_0.tif: No such file or directory\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import os\n",
        "\n",
        "# Define the exact folder paths the script is looking for\n",
        "paths = [\n",
        "    \"/path/to/dataset/parent/folder/s2_cloudy/\",\n",
        "    \"/path/to/dataset/parent/folder/s2_cloudfree/\",\n",
        "    \"/path/to/dataset/parent/folder/s1/\",\n",
        "    \"/path/to/output/model_runs/\"\n",
        "]\n",
        "\n",
        "# Create the directories\n",
        "for p in paths:\n",
        "    os.makedirs(p, exist_ok=True)\n",
        "\n",
        "# Generate dummy .tif image files using numpy so rasterio can read them\n",
        "import numpy as np\n",
        "import rasterio\n",
        "\n",
        "dummy_data = np.zeros((13, 128, 128), dtype=np.float32)\n",
        "\n",
        "# Create the specific target files mentioned in your dataset configuration\n",
        "files_to_create = [\n",
        "    \"/path/to/dataset/parent/folder/s2_cloudy/ROIs1158_spring_132_0.tif\",\n",
        "    \"/path/to/dataset/parent/folder/s2_cloudfree/ROIs1158_spring_132_0.tif\",\n",
        "    \"/path/to/dataset/parent/folder/s1/ROIs1158_spring_132_0.tif\"\n",
        "]\n",
        "\n",
        "for f in files_to_create:\n",
        "    with rasterio.open(f, 'w', driver='GTiff', height=128, width=128, count=13, dtype=np.float32) as dst:\n",
        "        dst.write(dummy_data)\n",
        "\n",
        "print(\"Mock dataset files created successfully!\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "C3OqnAnAljVe",
        "outputId": "14f5a9dc-f772-42f9-ff85-1d7ed1a9d89f"
      },
      "execution_count": 77,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Mock dataset files created successfully!\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "/usr/local/lib/python3.12/dist-packages/rasterio/__init__.py:377: NotGeoreferencedWarning: Dataset has no geotransform, gcps, or rpcs. The identity matrix will be returned.\n",
            "  dataset = writer(\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "%cd /content/dsen2-cr/Code/\n",
        "!python dsen2cr_main.py --predict dummy.h5"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "fnxu8Am3lse4",
        "outputId": "461c100d-30ad-430e-f4a4-4b6bde47dc35"
      },
      "execution_count": 78,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "/content/dsen2-cr/Code\n",
            "2026-06-29 18:14:24.139385: E external/local_xla/xla/stream_executor/cuda/cuda_platform.cc:51] failed call to cuInit: INTERNAL: CUDA error: Failed call to cuInit: UNKNOWN ERROR (303)\n",
            "Model compiled successfully!\n",
            "Getting file lists\n",
            "Number of train files found:  3\n",
            "Number of validation files found:  3\n",
            "Number of test files found:  3\n",
            "Predicting using file: dummy.h5\n",
            "Using this model: val\n",
            "Running prediction with initialized weights...\n",
            "WARNING: Folder {} exists and content may be overwritten!\n",
            "WARNING: Folder {} exists and content may be overwritten!\n",
            "Initializing generator for prediction and evaluation\n",
            "Generator initialized\n",
            "Storing evaluation metrics at  /path/to/output/model_runs/valeval.csv\n",
            "/usr/local/lib/python3.12/dist-packages/rasterio/__init__.py:367: NotGeoreferencedWarning: Dataset has no geotransform, gcps, or rpcs. The identity matrix will be returned.\n",
            "  dataset = DatasetReader(path, driver=driver, sharing=sharing, thread_safe=thread_safe, **kwargs)\n",
            "Traceback (most recent call last):\n",
            "  File \"/content/dsen2-cr/Code/dsen2cr_main.py\", line 179, in <module>\n",
            "    run_dsen2cr(args.predict_file, args.resume_file)\n",
            "  File \"/content/dsen2-cr/Code/dsen2cr_main.py\", line 158, in run_dsen2cr\n",
            "    predict_dsen2cr(predict_file, model, predict_data_type, base_out_path, input_data_folder, predict_filelist,\n",
            "  File \"/content/dsen2-cr/Code/dsen2cr_tools.py\", line 170, in predict_dsen2cr\n",
            "    for i, (data, y) in enumerate(predict_generator):\n",
            "                        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n",
            "  File \"/usr/local/lib/python3.12/dist-packages/keras/src/trainers/data_adapters/py_dataset_adapter.py\", line 171, in __iter__\n",
            "    yield self[index]\n",
            "          ~~~~^^^^^^^\n",
            "  File \"/content/dsen2-cr/Code/tools/dataIO.py\", line 279, in __getitem__\n",
            "    X, y = self.__data_generation(list_IDs_temp, self.augment_rotation_param[indexes],\n",
            "           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n",
            "  File \"/content/dsen2-cr/Code/tools/dataIO.py\", line 311, in __data_generation\n",
            "    input_sar_batch = self.get_batch(list_IDs_temp, augment_rotation_param_temp, augment_flip_param_temp,\n",
            "                      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n",
            "  File \"/content/dsen2-cr/Code/tools/dataIO.py\", line 420, in get_batch\n",
            "    data_image = self.get_normalized_data(data_image, data_type)\n",
            "                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n",
            "  File \"/content/dsen2-cr/Code/tools/dataIO.py\", line 376, in get_normalized_data\n",
            "    data_image[channel] = np.clip(data_image[channel], self.clip_min[data_type - 1][channel],\n",
            "                                                       ~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^\n",
            "IndexError: list index out of range\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "with open('/content/dsen2-cr/Code/tools/dataIO.py', 'r') as f:\n",
        "    lines = f.readlines()\n",
        "\n",
        "# Print lines 350 to 390 to check the clip_min configuration\n",
        "for idx in range(349, min(390, len(lines))):\n",
        "    print(f\"{idx+1}: {lines[idx]}\", end=\"\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "b_8JYaHXmAP2",
        "outputId": "46b96f36-f0b3-4301-e9fc-616571ea0ca8"
      },
      "execution_count": 79,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "350: \n",
            "351:         return image.astype('float32')\n",
            "352: \n",
            "353:     def get_data_image(self, ID, data_type, paramx, paramy):\n",
            "354: \n",
            "355:         data_path = os.path.join(self.input_data_folder, ID[data_type], ID[4]).lstrip()\n",
            "356: \n",
            "357:         if data_type == 2 or data_type == 3:\n",
            "358:             data_image = self.get_opt_image(data_path, paramx, paramy)\n",
            "359:         elif data_type == 1:\n",
            "360:             data_image = self.get_sar_image(data_path, paramx, paramy)\n",
            "361:         else:\n",
            "362:             print('Error! Data type invalid')\n",
            "363: \n",
            "364:         return data_image\n",
            "365: \n",
            "366:     def get_normalized_data(self, data_image, data_type):\n",
            "367: \n",
            "368:         shift_data = False\n",
            "369: \n",
            "370:         shift_values = [[0, 0], [1300., 981., 810., 380., 990., 2270., 2070., 2140., 2200., 650., 15., 1600., 680.],\n",
            "371:                         [1545., 1212., 1012., 713., 1212., 2476., 2842., 2775., 3174., 546., 24., 1776., 813.]]\n",
            "372: \n",
            "373:         # SAR\n",
            "374:         if data_type == 1:\n",
            "375:             for channel in range(len(data_image)):\n",
            "376:                 data_image[channel] = np.clip(data_image[channel], self.clip_min[data_type - 1][channel],\n",
            "377:                                               self.clip_max[data_type - 1][channel])\n",
            "378:                 data_image[channel] -= self.clip_min[data_type - 1][channel]\n",
            "379:                 data_image[channel] = self.max_val * (data_image[channel] / (\n",
            "380:                         self.clip_max[data_type - 1][channel] - self.clip_min[data_type - 1][channel]))\n",
            "381:             if shift_data:\n",
            "382:                 data_image -= self.max_val / 2\n",
            "383:         # OPT\n",
            "384:         elif data_type == 2 or data_type == 3:\n",
            "385:             for channel in range(len(data_image)):\n",
            "386:                 data_image[channel] = np.clip(data_image[channel], self.clip_min[data_type - 1][channel],\n",
            "387:                                               self.clip_max[data_type - 1][channel])\n",
            "388:                 if shift_data:\n",
            "389:                     data_image[channel] -= shift_values[data_type - 1][channel]\n",
            "390: \n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import os\n",
        "import numpy as np\n",
        "import rasterio\n",
        "\n",
        "# Ensure all mock test folders are present\n",
        "paths = [\n",
        "    \"/path/to/dataset/parent/folder/s2_cloudy/\",\n",
        "    \"/path/to/dataset/parent/folder/s2_cloudfree/\",\n",
        "    \"/path/to/dataset/parent/folder/s1/\",\n",
        "    \"/path/to/output/model_runs/\"\n",
        "]\n",
        "for p in paths:\n",
        "    os.makedirs(p, exist_ok=True)\n",
        "\n",
        "# 1. Generate Sentinel-2 Optical Images (Requires 13 Bands)\n",
        "s2_bands = 13\n",
        "s2_data = np.zeros((s2_bands, 128, 128), dtype=np.float32)\n",
        "optical_files = [\n",
        "    \"/path/to/dataset/parent/folder/s2_cloudy/ROIs1158_spring_132_0.tif\",\n",
        "    \"/path/to/dataset/parent/folder/s2_cloudfree/ROIs1158_spring_132_0.tif\"\n",
        "]\n",
        "for f in optical_files:\n",
        "    with rasterio.open(f, 'w', driver='GTiff', height=128, width=128, count=s2_bands, dtype=np.float32) as dst:\n",
        "        dst.write(s2_data)\n",
        "\n",
        "# 2. Generate Sentinel-1 SAR Images (Requires EXACTLY 2 Bands)\n",
        "s1_bands = 2\n",
        "s1_data = np.zeros((s1_bands, 128, 128), dtype=np.float32)\n",
        "sar_file = \"/path/to/dataset/parent/folder/s1/ROIs1158_spring_132_0.tif\"\n",
        "\n",
        "with rasterio.open(sar_file, 'w', driver='GTiff', height=128, width=128, count=s1_bands, dtype=np.float32) as dst:\n",
        "    dst.write(s1_data)\n",
        "\n",
        "print(\"Mock imagery sets adjusted to correct band channels!\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "iXZxzeyYmULM",
        "outputId": "d58d5cff-7cd7-4b1f-d1ff-63f1a6b6669a"
      },
      "execution_count": 80,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Mock imagery sets adjusted to correct band channels!\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "%cd /content/dsen2-cr/Code/\n",
        "!python dsen2cr_main.py --predict dummy.h5"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "RVjPOkHEmdxY",
        "outputId": "629e61c6-8a09-4a0a-e74c-3c01929e03e1"
      },
      "execution_count": 81,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "/content/dsen2-cr/Code\n",
            "2026-06-29 18:17:47.613246: E external/local_xla/xla/stream_executor/cuda/cuda_platform.cc:51] failed call to cuInit: INTERNAL: CUDA error: Failed call to cuInit: UNKNOWN ERROR (303)\n",
            "Model compiled successfully!\n",
            "Getting file lists\n",
            "Number of train files found:  3\n",
            "Number of validation files found:  3\n",
            "Number of test files found:  3\n",
            "Predicting using file: dummy.h5\n",
            "Using this model: val\n",
            "Running prediction with initialized weights...\n",
            "WARNING: Folder {} exists and content may be overwritten!\n",
            "WARNING: Folder {} exists and content may be overwritten!\n",
            "Initializing generator for prediction and evaluation\n",
            "Generator initialized\n",
            "Storing evaluation metrics at  /path/to/output/model_runs/valeval.csv\n",
            "/usr/local/lib/python3.12/dist-packages/rasterio/__init__.py:367: NotGeoreferencedWarning: Dataset has no geotransform, gcps, or rpcs. The identity matrix will be returned.\n",
            "  dataset = DatasetReader(path, driver=driver, sharing=sharing, thread_safe=thread_safe, **kwargs)\n",
            "/content/dsen2-cr/Code/tools/dataIO.py:403: RuntimeWarning: overflow encountered in cast\n",
            "  batch = np.empty((self.batch_size, *dim)).astype('float32')\n",
            "Traceback (most recent call last):\n",
            "  File \"rasterio/_base.pyx\", line 320, in rasterio._base.DatasetBase.__init__\n",
            "  File \"rasterio/_base.pyx\", line 232, in rasterio._base.open_dataset\n",
            "  File \"rasterio/_err.pyx\", line 359, in rasterio._err.exc_wrap_pointer\n",
            "rasterio._err.CPLE_OpenFailedError: /path/to/dataset/parent/folder/s2_cloudFree/ROIs1158_spring_132_0.tif: No such file or directory\n",
            "\n",
            "During handling of the above exception, another exception occurred:\n",
            "\n",
            "Traceback (most recent call last):\n",
            "  File \"/content/dsen2-cr/Code/dsen2cr_main.py\", line 179, in <module>\n",
            "    run_dsen2cr(args.predict_file, args.resume_file)\n",
            "  File \"/content/dsen2-cr/Code/dsen2cr_main.py\", line 158, in run_dsen2cr\n",
            "    predict_dsen2cr(predict_file, model, predict_data_type, base_out_path, input_data_folder, predict_filelist,\n",
            "  File \"/content/dsen2-cr/Code/dsen2cr_tools.py\", line 170, in predict_dsen2cr\n",
            "    for i, (data, y) in enumerate(predict_generator):\n",
            "                        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n",
            "  File \"/usr/local/lib/python3.12/dist-packages/keras/src/trainers/data_adapters/py_dataset_adapter.py\", line 171, in __iter__\n",
            "    yield self[index]\n",
            "          ~~~~^^^^^^^\n",
            "  File \"/content/dsen2-cr/Code/tools/dataIO.py\", line 279, in __getitem__\n",
            "    X, y = self.__data_generation(list_IDs_temp, self.augment_rotation_param[indexes],\n",
            "           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n",
            "  File \"/content/dsen2-cr/Code/tools/dataIO.py\", line 315, in __data_generation\n",
            "    output_opt_batch = self.get_batch(list_IDs_temp, augment_rotation_param_temp, augment_flip_param_temp,\n",
            "                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n",
            "  File \"/content/dsen2-cr/Code/tools/dataIO.py\", line 408, in get_batch\n",
            "    data_image = self.get_data_image(ID, data_type, random_crop_paramx_temp[i], random_crop_paramy_temp[i])\n",
            "                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n",
            "  File \"/content/dsen2-cr/Code/tools/dataIO.py\", line 358, in get_data_image\n",
            "    data_image = self.get_opt_image(data_path, paramx, paramy)\n",
            "                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n",
            "  File \"/content/dsen2-cr/Code/tools/dataIO.py\", line 338, in get_opt_image\n",
            "    image = self.get_image_data(paramx, paramy, path)\n",
            "            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n",
            "  File \"/content/dsen2-cr/Code/tools/dataIO.py\", line 330, in get_image_data\n",
            "    src = rasterio.open(path, 'r', driver='GTiff')\n",
            "          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n",
            "  File \"/usr/local/lib/python3.12/dist-packages/rasterio/env.py\", line 464, in wrapper\n",
            "    return f(*args, **kwds)\n",
            "           ^^^^^^^^^^^^^^^^\n",
            "  File \"/usr/local/lib/python3.12/dist-packages/rasterio/__init__.py\", line 367, in open\n",
            "    dataset = DatasetReader(path, driver=driver, sharing=sharing, thread_safe=thread_safe, **kwargs)\n",
            "              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n",
            "  File \"rasterio/_base.pyx\", line 329, in rasterio._base.DatasetBase.__init__\n",
            "rasterio.errors.RasterioIOError: /path/to/dataset/parent/folder/s2_cloudFree/ROIs1158_spring_132_0.tif: No such file or directory\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import os\n",
        "import pandas as pd\n",
        "import numpy as np\n",
        "import rasterio\n",
        "\n",
        "# Read the project's file list configurations\n",
        "csv_path = '/content/dsen2-cr/Data/datasetfilelist.csv'\n",
        "df = pd.read_csv(csv_path)\n",
        "\n",
        "# Set base paths matching the repository default placeholders\n",
        "base_dir = \"/path/to/dataset/parent/folder\"\n",
        "\n",
        "print(\"Generating all required mock imagery files...\")\n",
        "for idx, row in df.iterrows():\n",
        "    # 1. Sentinel-2 Cloudy (13 Bands)\n",
        "    f_cloudy = os.path.join(base_dir, \"s2_cloudy\", row['cloudy_fid'].strip())\n",
        "    os.makedirs(os.path.dirname(f_cloudy), exist_ok=True)\n",
        "    if not os.path.exists(f_cloudy):\n",
        "        with rasterio.open(f_cloudy, 'w', driver='GTiff', height=128, width=128, count=13, dtype=np.float32) as dst:\n",
        "            dst.write(np.zeros((13, 128, 128), dtype=np.float32))\n",
        "\n",
        "    # 2. Sentinel-2 Cloud-free (13 Bands)\n",
        "    f_free = os.path.join(base_dir, \"s2_cloudfree\", row['cloudfree_fid'].strip())\n",
        "    os.makedirs(os.path.dirname(f_free), exist_ok=True)\n",
        "    if not os.path.exists(f_free):\n",
        "        with rasterio.open(f_free, 'w', driver='GTiff', height=128, width=128, count=13, dtype=np.float32) as dst:\n",
        "            dst.write(np.zeros((13, 128, 128), dtype=np.float32))\n",
        "\n",
        "    # 3. Sentinel-1 SAR (2 Bands)\n",
        "    f_sar = os.path.join(base_dir, \"s1\", row['sar_fid'].strip())\n",
        "    os.makedirs(os.path.dirname(f_sar), exist_ok=True)\n",
        "    if not os.path.exists(f_sar):\n",
        "        with rasterio.open(f_sar, 'w', driver='GTiff', height=128, width=128, count=2, dtype=np.float32) as dst:\n",
        "            dst.write(np.zeros((2, 128, 128), dtype=np.float32))\n",
        "\n",
        "# Ensure output directory exists\n",
        "os.makedirs(\"/path/to/output/model_runs/\", exist_ok=True)\n",
        "print(\"Complete! All files listed in the CSV configuration have been created.\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 703
        },
        "id": "-_JrM2ztm43K",
        "outputId": "04dc4aa7-4dc1-4b7e-d3de-b1c2a4e95c17"
      },
      "execution_count": 83,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Generating all required mock imagery files...\n"
          ]
        },
        {
          "output_type": "error",
          "ename": "KeyError",
          "evalue": "'cloudy_fid'",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mKeyError\u001b[0m                                  Traceback (most recent call last)",
            "\u001b[0;32m/usr/local/lib/python3.12/dist-packages/pandas/core/indexes/base.py\u001b[0m in \u001b[0;36mget_loc\u001b[0;34m(self, key)\u001b[0m\n\u001b[1;32m   3804\u001b[0m         \u001b[0;32mtry\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m-> 3805\u001b[0;31m             \u001b[0;32mreturn\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_engine\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mget_loc\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mcasted_key\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m   3806\u001b[0m         \u001b[0;32mexcept\u001b[0m \u001b[0mKeyError\u001b[0m \u001b[0;32mas\u001b[0m \u001b[0merr\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32mindex.pyx\u001b[0m in \u001b[0;36mpandas._libs.index.IndexEngine.get_loc\u001b[0;34m()\u001b[0m\n",
            "\u001b[0;32mindex.pyx\u001b[0m in \u001b[0;36mpandas._libs.index.IndexEngine.get_loc\u001b[0;34m()\u001b[0m\n",
            "\u001b[0;32mpandas/_libs/hashtable_class_helper.pxi\u001b[0m in \u001b[0;36mpandas._libs.hashtable.PyObjectHashTable.get_item\u001b[0;34m()\u001b[0m\n",
            "\u001b[0;32mpandas/_libs/hashtable_class_helper.pxi\u001b[0m in \u001b[0;36mpandas._libs.hashtable.PyObjectHashTable.get_item\u001b[0;34m()\u001b[0m\n",
            "\u001b[0;31mKeyError\u001b[0m: 'cloudy_fid'",
            "\nThe above exception was the direct cause of the following exception:\n",
            "\u001b[0;31mKeyError\u001b[0m                                  Traceback (most recent call last)",
            "\u001b[0;32m/tmp/ipykernel_6376/717188514.py\u001b[0m in \u001b[0;36m<cell line: 0>\u001b[0;34m()\u001b[0m\n\u001b[1;32m     14\u001b[0m \u001b[0;32mfor\u001b[0m \u001b[0midx\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mrow\u001b[0m \u001b[0;32min\u001b[0m \u001b[0mdf\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0miterrows\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     15\u001b[0m     \u001b[0;31m# 1. Sentinel-2 Cloudy (13 Bands)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 16\u001b[0;31m     \u001b[0mf_cloudy\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mos\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mpath\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mjoin\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mbase_dir\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m\"s2_cloudy\"\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mrow\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m'cloudy_fid'\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mstrip\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     17\u001b[0m     \u001b[0mos\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mmakedirs\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mos\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mpath\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mdirname\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mf_cloudy\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mexist_ok\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;32mTrue\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     18\u001b[0m     \u001b[0;32mif\u001b[0m \u001b[0;32mnot\u001b[0m \u001b[0mos\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mpath\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mexists\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mf_cloudy\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.12/dist-packages/pandas/core/series.py\u001b[0m in \u001b[0;36m__getitem__\u001b[0;34m(self, key)\u001b[0m\n\u001b[1;32m   1119\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   1120\u001b[0m         \u001b[0;32melif\u001b[0m \u001b[0mkey_is_scalar\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m-> 1121\u001b[0;31m             \u001b[0;32mreturn\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_get_value\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mkey\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m   1122\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   1123\u001b[0m         \u001b[0;31m# Convert generator to list before going through hashable part\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.12/dist-packages/pandas/core/series.py\u001b[0m in \u001b[0;36m_get_value\u001b[0;34m(self, label, takeable)\u001b[0m\n\u001b[1;32m   1235\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   1236\u001b[0m         \u001b[0;31m# Similar to Index.get_value, but we do not fall back to positional\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m-> 1237\u001b[0;31m         \u001b[0mloc\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mindex\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mget_loc\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mlabel\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m   1238\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   1239\u001b[0m         \u001b[0;32mif\u001b[0m \u001b[0mis_integer\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mloc\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.12/dist-packages/pandas/core/indexes/base.py\u001b[0m in \u001b[0;36mget_loc\u001b[0;34m(self, key)\u001b[0m\n\u001b[1;32m   3810\u001b[0m             ):\n\u001b[1;32m   3811\u001b[0m                 \u001b[0;32mraise\u001b[0m \u001b[0mInvalidIndexError\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mkey\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m-> 3812\u001b[0;31m             \u001b[0;32mraise\u001b[0m \u001b[0mKeyError\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mkey\u001b[0m\u001b[0;34m)\u001b[0m \u001b[0;32mfrom\u001b[0m \u001b[0merr\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m   3813\u001b[0m         \u001b[0;32mexcept\u001b[0m \u001b[0mTypeError\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   3814\u001b[0m             \u001b[0;31m# If we have a listlike key, _check_indexing_error will raise\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;31mKeyError\u001b[0m: 'cloudy_fid'"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import os\n",
        "import pandas as pd\n",
        "import numpy as np\n",
        "import rasterio\n",
        "\n",
        "# Read the file explicitly stating there are NO text headers\n",
        "csv_path = '/content/dsen2-cr/Data/datasetfilelist.csv'\n",
        "df = pd.read_csv(csv_path, header=None)\n",
        "\n",
        "# Base folder structure expected by the default configurations\n",
        "base_dir = \"/path/to/dataset/parent/folder\"\n",
        "\n",
        "print(\"Generating mock imagery files from index positions...\")\n",
        "for idx, row in df.iterrows():\n",
        "    # According to the project rules:\n",
        "    # Column 1 = S1 folder, Column 2 = S2 Cloudfree folder, Column 3 = S2 Cloudy folder, Column 4 = Filename\n",
        "    s1_folder = str(row[1]).strip()\n",
        "    s2_free_folder = str(row[2]).strip()\n",
        "    s2_cloudy_folder = str(row[3]).strip()\n",
        "    filename = str(row[4]).strip()\n",
        "\n",
        "    # 1. Sentinel-2 Cloudy (13 Bands)\n",
        "    f_cloudy = os.path.join(base_dir, s2_cloudy_folder, filename)\n",
        "    os.makedirs(os.path.dirname(f_cloudy), exist_ok=True)\n",
        "    if not os.path.exists(f_cloudy):\n",
        "        with rasterio.open(f_cloudy, 'w', driver='GTiff', height=128, width=128, count=13, dtype=np.float32) as dst:\n",
        "            dst.write(np.zeros((13, 128, 128), dtype=np.float32))\n",
        "\n",
        "    # 2. Sentinel-2 Cloud-free (13 Bands)\n",
        "    f_free = os.path.join(base_dir, s2_free_folder, filename)\n",
        "    os.makedirs(os.path.dirname(f_free), exist_ok=True)\n",
        "    if not os.path.exists(f_free):\n",
        "        with rasterio.open(f_free, 'w', driver='GTiff', height=128, width=128, count=13, dtype=np.float32) as dst:\n",
        "            dst.write(np.zeros((13, 128, 128), dtype=np.float32))\n",
        "\n",
        "    # 3. Sentinel-1 SAR (2 Bands)\n",
        "    f_sar = os.path.join(base_dir, s1_folder, filename)\n",
        "    os.makedirs(os.path.dirname(f_sar), exist_ok=True)\n",
        "    if not os.path.exists(f_sar):\n",
        "        with rasterio.open(f_sar, 'w', driver='GTiff', height=128, width=128, count=2, dtype=np.float32) as dst:\n",
        "            dst.write(np.zeros((2, 128, 128), dtype=np.float32))\n",
        "\n",
        "# Ensure model metrics output run directory exists\n",
        "os.makedirs(\"/path/to/output/model_runs/\", exist_ok=True)\n",
        "print(\"Success! Every image placeholder listed in your CSV configuration has been fully initialized.\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 703
        },
        "id": "p2Qo1HVenQuu",
        "outputId": "9c9027cd-47b9-4129-9d63-c7210c221131"
      },
      "execution_count": 84,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Generating mock imagery files from index positions...\n"
          ]
        },
        {
          "output_type": "error",
          "ename": "KeyError",
          "evalue": "1",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mKeyError\u001b[0m                                  Traceback (most recent call last)",
            "\u001b[0;32m/usr/local/lib/python3.12/dist-packages/pandas/core/indexes/base.py\u001b[0m in \u001b[0;36mget_loc\u001b[0;34m(self, key)\u001b[0m\n\u001b[1;32m   3804\u001b[0m         \u001b[0;32mtry\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m-> 3805\u001b[0;31m             \u001b[0;32mreturn\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_engine\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mget_loc\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mcasted_key\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m   3806\u001b[0m         \u001b[0;32mexcept\u001b[0m \u001b[0mKeyError\u001b[0m \u001b[0;32mas\u001b[0m \u001b[0merr\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32mindex.pyx\u001b[0m in \u001b[0;36mpandas._libs.index.IndexEngine.get_loc\u001b[0;34m()\u001b[0m\n",
            "\u001b[0;32mindex.pyx\u001b[0m in \u001b[0;36mpandas._libs.index.IndexEngine.get_loc\u001b[0;34m()\u001b[0m\n",
            "\u001b[0;32mpandas/_libs/hashtable_class_helper.pxi\u001b[0m in \u001b[0;36mpandas._libs.hashtable.Int64HashTable.get_item\u001b[0;34m()\u001b[0m\n",
            "\u001b[0;32mpandas/_libs/hashtable_class_helper.pxi\u001b[0m in \u001b[0;36mpandas._libs.hashtable.Int64HashTable.get_item\u001b[0;34m()\u001b[0m\n",
            "\u001b[0;31mKeyError\u001b[0m: 1",
            "\nThe above exception was the direct cause of the following exception:\n",
            "\u001b[0;31mKeyError\u001b[0m                                  Traceback (most recent call last)",
            "\u001b[0;32m/tmp/ipykernel_6376/484036674.py\u001b[0m in \u001b[0;36m<cell line: 0>\u001b[0;34m()\u001b[0m\n\u001b[1;32m     15\u001b[0m     \u001b[0;31m# According to the project rules:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     16\u001b[0m     \u001b[0;31m# Column 1 = S1 folder, Column 2 = S2 Cloudfree folder, Column 3 = S2 Cloudy folder, Column 4 = Filename\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 17\u001b[0;31m     \u001b[0ms1_folder\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mstr\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mrow\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;36m1\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mstrip\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     18\u001b[0m     \u001b[0ms2_free_folder\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mstr\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mrow\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;36m2\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mstrip\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     19\u001b[0m     \u001b[0ms2_cloudy_folder\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mstr\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mrow\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;36m3\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mstrip\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.12/dist-packages/pandas/core/series.py\u001b[0m in \u001b[0;36m__getitem__\u001b[0;34m(self, key)\u001b[0m\n\u001b[1;32m   1119\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   1120\u001b[0m         \u001b[0;32melif\u001b[0m \u001b[0mkey_is_scalar\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m-> 1121\u001b[0;31m             \u001b[0;32mreturn\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_get_value\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mkey\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m   1122\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   1123\u001b[0m         \u001b[0;31m# Convert generator to list before going through hashable part\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.12/dist-packages/pandas/core/series.py\u001b[0m in \u001b[0;36m_get_value\u001b[0;34m(self, label, takeable)\u001b[0m\n\u001b[1;32m   1235\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   1236\u001b[0m         \u001b[0;31m# Similar to Index.get_value, but we do not fall back to positional\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m-> 1237\u001b[0;31m         \u001b[0mloc\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mindex\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mget_loc\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mlabel\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m   1238\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   1239\u001b[0m         \u001b[0;32mif\u001b[0m \u001b[0mis_integer\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mloc\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.12/dist-packages/pandas/core/indexes/base.py\u001b[0m in \u001b[0;36mget_loc\u001b[0;34m(self, key)\u001b[0m\n\u001b[1;32m   3810\u001b[0m             ):\n\u001b[1;32m   3811\u001b[0m                 \u001b[0;32mraise\u001b[0m \u001b[0mInvalidIndexError\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mkey\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m-> 3812\u001b[0;31m             \u001b[0;32mraise\u001b[0m \u001b[0mKeyError\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mkey\u001b[0m\u001b[0;34m)\u001b[0m \u001b[0;32mfrom\u001b[0m \u001b[0merr\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m   3813\u001b[0m         \u001b[0;32mexcept\u001b[0m \u001b[0mTypeError\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   3814\u001b[0m             \u001b[0;31m# If we have a listlike key, _check_indexing_error will raise\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;31mKeyError\u001b[0m: 1"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import pandas as pd\n",
        "\n",
        "csv_path = '/content/dsen2-cr/Data/datasetfilelist.csv'\n",
        "df = pd.read_csv(csv_path, header=None)\n",
        "\n",
        "# Print the first row and the column info\n",
        "print(\"Columns found:\", list(df.columns))\n",
        "print(\"\\nFirst row of data:\")\n",
        "print(df.head(1))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "GU5zRKPLnhzv",
        "outputId": "e189af15-4388-403e-adcf-5546d5189a0d"
      },
      "execution_count": 86,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Columns found: [0]\n",
            "\n",
            "First row of data:\n",
            "                                                   0\n",
            "0  1\\ts1\\ts2_cloudFree\\ts2_cloudy\\tROIs1158_sprin...\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import os\n",
        "import numpy as np\n",
        "import rasterio\n",
        "\n",
        "# Define the root path matching the system config defaults\n",
        "base_dir = \"/path/to/dataset/parent/folder\"\n",
        "filename = \"ROIs1158_spring_132_0.tif\"\n",
        "\n",
        "# Define the targets: (Folder Name, Total Image Channels/Bands)\n",
        "targets = [\n",
        "    (\"s2_cloudy\", 13),\n",
        "    (\"s2_cloudfree\", 13),\n",
        "    (\"s1\", 2)\n",
        "]\n",
        "\n",
        "print(\"Generating target directory tree structures...\")\n",
        "for folder, bands in targets:\n",
        "    # 1. Build the custom nested subfolder structures matching your data configuration\n",
        "    full_folder_path = os.path.join(base_dir, f\"1ts1\\\\ts2_cloudfree\\\\ts2_cloudy\\\\tROIs1158_sprin...\", folder)\n",
        "    os.makedirs(full_folder_path, exist_ok=True)\n",
        "\n",
        "    # 2. Write the formatted empty raster array files\n",
        "    file_path = os.path.join(full_folder_path, filename)\n",
        "    dummy_array = np.zeros((bands, 128, 128), dtype=np.float32)\n",
        "\n",
        "    with rasterio.open(file_path, 'w', driver='GTiff', height=128, width=128, count=bands, dtype=np.float32) as dst:\n",
        "        dst.write(dummy_array)\n",
        "\n",
        "# Ensure evaluation metrics logs write paths are active\n",
        "os.makedirs(\"/path/to/output/model_runs/\", exist_ok=True)\n",
        "print(\"Complete! All structural path components initialized successfully.\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "sqUrxfijnwlJ",
        "outputId": "147de0d1-b354-44e0-c4e6-d292a56ce248"
      },
      "execution_count": 87,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Generating target directory tree structures...\n",
            "Complete! All structural path components initialized successfully.\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "/usr/local/lib/python3.12/dist-packages/rasterio/__init__.py:377: NotGeoreferencedWarning: Dataset has no geotransform, gcps, or rpcs. The identity matrix will be returned.\n",
            "  dataset = writer(\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import os\n",
        "import pandas as pd\n",
        "import numpy as np\n",
        "import rasterio\n",
        "\n",
        "# Read the file directly\n",
        "csv_path = '/content/dsen2-cr/Data/datasetfilelist.csv'\n",
        "with open(csv_path, 'r') as f:\n",
        "    lines = f.readlines()\n",
        "\n",
        "base_dir = \"/path/to/dataset/parent/folder\"\n",
        "\n",
        "print(\"Parsing configurations and creating exact mock files...\")\n",
        "for line in lines:\n",
        "    if not line.strip():\n",
        "        continue\n",
        "    # Split by backslash or whatever character separates them\n",
        "    parts = line.replace('\\\\', '/').strip().split('/')\n",
        "\n",
        "    if len(parts) >= 4:\n",
        "        s1_folder = parts[0]\n",
        "        s2_free_folder = parts[1]\n",
        "        s2_cloudy_folder = parts[2]\n",
        "        filename = parts[3]\n",
        "\n",
        "        # 1. Sentinel-2 Cloudy (13 Bands)\n",
        "        f_cloudy = os.path.join(base_dir, s2_cloudy_folder, filename)\n",
        "        os.makedirs(os.path.dirname(f_cloudy), exist_ok=True)\n",
        "        with rasterio.open(f_cloudy, 'w', driver='GTiff', height=128, width=128, count=13, dtype=np.float32) as dst:\n",
        "            dst.write(np.zeros((13, 128, 128), dtype=np.float32))\n",
        "\n",
        "        # 2. Sentinel-2 Cloud-free (13 Bands)\n",
        "        f_free = os.path.join(base_dir, s2_free_folder, filename)\n",
        "        os.makedirs(os.path.dirname(f_free), exist_ok=True)\n",
        "        with rasterio.open(f_free, 'w', driver='GTiff', height=128, width=128, count=13, dtype=np.float32) as dst:\n",
        "            dst.write(np.zeros((13, 128, 128), dtype=np.float32))\n",
        "\n",
        "        # 3. Sentinel-1 SAR (2 Bands)\n",
        "        f_sar = os.path.join(base_dir, s1_folder, filename)\n",
        "        os.makedirs(os.path.dirname(f_sar), exist_ok=True)\n",
        "        with rasterio.open(f_sar, 'w', driver='GTiff', height=128, width=128, count=2, dtype=np.float32) as dst:\n",
        "            dst.write(np.zeros((2, 128, 128), dtype=np.float32))\n",
        "\n",
        "os.makedirs(\"/path/to/output/model_runs/\", exist_ok=True)\n",
        "print(\"Complete! All dynamic path components initialized.\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "u_JGPFBEoQPk",
        "outputId": "788699cd-153e-4381-a83d-b6cfbb11c224"
      },
      "execution_count": 89,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Parsing configurations and creating exact mock files...\n",
            "Complete! All dynamic path components initialized.\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "%cd /content/dsen2-cr/Code/\n",
        "!python dsen2cr_main.py --predict dummy.h5"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "bcVIJaKuoV1u",
        "outputId": "120740da-465d-478e-b215-4452e41eefe3"
      },
      "execution_count": 90,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "/content/dsen2-cr/Code\n",
            "2026-06-29 18:25:56.829531: E external/local_xla/xla/stream_executor/cuda/cuda_platform.cc:51] failed call to cuInit: INTERNAL: CUDA error: Failed call to cuInit: UNKNOWN ERROR (303)\n",
            "Model compiled successfully!\n",
            "Getting file lists\n",
            "Number of train files found:  3\n",
            "Number of validation files found:  3\n",
            "Number of test files found:  3\n",
            "Predicting using file: dummy.h5\n",
            "Using this model: val\n",
            "Running prediction with initialized weights...\n",
            "WARNING: Folder {} exists and content may be overwritten!\n",
            "WARNING: Folder {} exists and content may be overwritten!\n",
            "Initializing generator for prediction and evaluation\n",
            "Generator initialized\n",
            "Storing evaluation metrics at  /path/to/output/model_runs/valeval.csv\n",
            "/usr/local/lib/python3.12/dist-packages/rasterio/__init__.py:367: NotGeoreferencedWarning: Dataset has no geotransform, gcps, or rpcs. The identity matrix will be returned.\n",
            "  dataset = DatasetReader(path, driver=driver, sharing=sharing, thread_safe=thread_safe, **kwargs)\n",
            "/content/dsen2-cr/Code/tools/dataIO.py:403: RuntimeWarning: overflow encountered in cast\n",
            "  batch = np.empty((self.batch_size, *dim)).astype('float32')\n",
            "Traceback (most recent call last):\n",
            "  File \"rasterio/_base.pyx\", line 320, in rasterio._base.DatasetBase.__init__\n",
            "  File \"rasterio/_base.pyx\", line 232, in rasterio._base.open_dataset\n",
            "  File \"rasterio/_err.pyx\", line 359, in rasterio._err.exc_wrap_pointer\n",
            "rasterio._err.CPLE_OpenFailedError: /path/to/dataset/parent/folder/s2_cloudFree/ROIs1158_spring_132_0.tif: No such file or directory\n",
            "\n",
            "During handling of the above exception, another exception occurred:\n",
            "\n",
            "Traceback (most recent call last):\n",
            "  File \"/content/dsen2-cr/Code/dsen2cr_main.py\", line 179, in <module>\n",
            "    run_dsen2cr(args.predict_file, args.resume_file)\n",
            "  File \"/content/dsen2-cr/Code/dsen2cr_main.py\", line 158, in run_dsen2cr\n",
            "    predict_dsen2cr(predict_file, model, predict_data_type, base_out_path, input_data_folder, predict_filelist,\n",
            "  File \"/content/dsen2-cr/Code/dsen2cr_tools.py\", line 170, in predict_dsen2cr\n",
            "    for i, (data, y) in enumerate(predict_generator):\n",
            "                        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n",
            "  File \"/usr/local/lib/python3.12/dist-packages/keras/src/trainers/data_adapters/py_dataset_adapter.py\", line 171, in __iter__\n",
            "    yield self[index]\n",
            "          ~~~~^^^^^^^\n",
            "  File \"/content/dsen2-cr/Code/tools/dataIO.py\", line 279, in __getitem__\n",
            "    X, y = self.__data_generation(list_IDs_temp, self.augment_rotation_param[indexes],\n",
            "           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n",
            "  File \"/content/dsen2-cr/Code/tools/dataIO.py\", line 315, in __data_generation\n",
            "    output_opt_batch = self.get_batch(list_IDs_temp, augment_rotation_param_temp, augment_flip_param_temp,\n",
            "                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n",
            "  File \"/content/dsen2-cr/Code/tools/dataIO.py\", line 408, in get_batch\n",
            "    data_image = self.get_data_image(ID, data_type, random_crop_paramx_temp[i], random_crop_paramy_temp[i])\n",
            "                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n",
            "  File \"/content/dsen2-cr/Code/tools/dataIO.py\", line 358, in get_data_image\n",
            "    data_image = self.get_opt_image(data_path, paramx, paramy)\n",
            "                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n",
            "  File \"/content/dsen2-cr/Code/tools/dataIO.py\", line 338, in get_opt_image\n",
            "    image = self.get_image_data(paramx, paramy, path)\n",
            "            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n",
            "  File \"/content/dsen2-cr/Code/tools/dataIO.py\", line 330, in get_image_data\n",
            "    src = rasterio.open(path, 'r', driver='GTiff')\n",
            "          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n",
            "  File \"/usr/local/lib/python3.12/dist-packages/rasterio/env.py\", line 464, in wrapper\n",
            "    return f(*args, **kwds)\n",
            "           ^^^^^^^^^^^^^^^^\n",
            "  File \"/usr/local/lib/python3.12/dist-packages/rasterio/__init__.py\", line 367, in open\n",
            "    dataset = DatasetReader(path, driver=driver, sharing=sharing, thread_safe=thread_safe, **kwargs)\n",
            "              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n",
            "  File \"rasterio/_base.pyx\", line 329, in rasterio._base.DatasetBase.__init__\n",
            "rasterio.errors.RasterioIOError: /path/to/dataset/parent/folder/s2_cloudFree/ROIs1158_spring_132_0.tif: No such file or directory\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import os\n",
        "import pandas as pd\n",
        "import numpy as np\n",
        "import rasterio\n",
        "\n",
        "# Read the CSV specifically declaring that tabs ('\\t') are used as separators\n",
        "csv_path = '/content/dsen2-cr/Data/datasetfilelist.csv'\n",
        "df = pd.read_csv(csv_path, sep='\\t', header=None)\n",
        "\n",
        "base_dir = \"/path/to/dataset/parent/folder\"\n",
        "\n",
        "print(\"Generating exact mock datasets from tab-separated layout...\")\n",
        "for idx, row in df.iterrows():\n",
        "    s1_folder = str(row[0]).strip()\n",
        "    s2_free_folder = str(row[1]).strip()\n",
        "    s2_cloudy_folder = str(row[2]).strip()\n",
        "    filename = str(row[3]).strip()\n",
        "\n",
        "    # 1. Sentinel-2 Cloudy (13 Bands)\n",
        "    f_cloudy = os.path.join(base_dir, s2_cloudy_folder, filename)\n",
        "    os.makedirs(os.path.dirname(f_cloudy), exist_ok=True)\n",
        "    with rasterio.open(f_cloudy, 'w', driver='GTiff', height=128, width=128, count=13, dtype=np.float32) as dst:\n",
        "        dst.write(np.zeros((13, 128, 128), dtype=np.float32))\n",
        "\n",
        "    # 2. Sentinel-2 Cloud-free (13 Bands)\n",
        "    f_free = os.path.join(base_dir, s2_free_folder, filename)\n",
        "    os.makedirs(os.path.dirname(f_free), exist_ok=True)\n",
        "    with rasterio.open(f_free, 'w', driver='GTiff', height=128, width=128, count=13, dtype=np.float32) as dst:\n",
        "        dst.write(np.zeros((13, 128, 128), dtype=np.float32))\n",
        "\n",
        "    # 3. Sentinel-1 SAR (2 Bands)\n",
        "    f_sar = os.path.join(base_dir, s1_folder, filename)\n",
        "    os.makedirs(os.path.dirname(f_sar), exist_ok=True)\n",
        "    with rasterio.open(f_sar, 'w', driver='GTiff', height=128, width=128, count=2, dtype=np.float32) as dst:\n",
        "        dst.write(np.zeros((2, 128, 128), dtype=np.float32))\n",
        "\n",
        "# Ensure output directory exists\n",
        "os.makedirs(\"/path/to/output/model_runs/\", exist_ok=True)\n",
        "print(\"Complete! All paths configured perfectly.\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "CeTwop00ovFr",
        "outputId": "d4f625ff-ff2f-435c-d28b-c8f14c209b53"
      },
      "execution_count": 91,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Generating exact mock datasets from tab-separated layout...\n",
            "Complete! All paths configured perfectly.\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "/usr/local/lib/python3.12/dist-packages/rasterio/__init__.py:377: NotGeoreferencedWarning: Dataset has no geotransform, gcps, or rpcs. The identity matrix will be returned.\n",
            "  dataset = writer(\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "%cd /content/dsen2-cr/Code/\n",
        "!python dsen2cr_main.py --predict dummy.h5"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "8Ko3c6ghpCoY",
        "outputId": "43f9cedd-3dab-44d3-9ab1-7c546688a729"
      },
      "execution_count": 92,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "/content/dsen2-cr/Code\n",
            "2026-06-29 18:29:01.822581: E external/local_xla/xla/stream_executor/cuda/cuda_platform.cc:51] failed call to cuInit: INTERNAL: CUDA error: Failed call to cuInit: UNKNOWN ERROR (303)\n",
            "Model compiled successfully!\n",
            "Getting file lists\n",
            "Number of train files found:  3\n",
            "Number of validation files found:  3\n",
            "Number of test files found:  3\n",
            "Predicting using file: dummy.h5\n",
            "Using this model: val\n",
            "Running prediction with initialized weights...\n",
            "WARNING: Folder {} exists and content may be overwritten!\n",
            "WARNING: Folder {} exists and content may be overwritten!\n",
            "Initializing generator for prediction and evaluation\n",
            "Generator initialized\n",
            "Storing evaluation metrics at  /path/to/output/model_runs/valeval.csv\n",
            "/usr/local/lib/python3.12/dist-packages/rasterio/__init__.py:367: NotGeoreferencedWarning: Dataset has no geotransform, gcps, or rpcs. The identity matrix will be returned.\n",
            "  dataset = DatasetReader(path, driver=driver, sharing=sharing, thread_safe=thread_safe, **kwargs)\n",
            "/content/dsen2-cr/Code/tools/dataIO.py:403: RuntimeWarning: overflow encountered in cast\n",
            "  batch = np.empty((self.batch_size, *dim)).astype('float32')\n",
            "Traceback (most recent call last):\n",
            "  File \"rasterio/_base.pyx\", line 320, in rasterio._base.DatasetBase.__init__\n",
            "  File \"rasterio/_base.pyx\", line 232, in rasterio._base.open_dataset\n",
            "  File \"rasterio/_err.pyx\", line 359, in rasterio._err.exc_wrap_pointer\n",
            "rasterio._err.CPLE_OpenFailedError: /path/to/dataset/parent/folder/s2_cloudFree/ROIs1158_spring_132_0.tif: No such file or directory\n",
            "\n",
            "During handling of the above exception, another exception occurred:\n",
            "\n",
            "Traceback (most recent call last):\n",
            "  File \"/content/dsen2-cr/Code/dsen2cr_main.py\", line 179, in <module>\n",
            "    run_dsen2cr(args.predict_file, args.resume_file)\n",
            "  File \"/content/dsen2-cr/Code/dsen2cr_main.py\", line 158, in run_dsen2cr\n",
            "    predict_dsen2cr(predict_file, model, predict_data_type, base_out_path, input_data_folder, predict_filelist,\n",
            "  File \"/content/dsen2-cr/Code/dsen2cr_tools.py\", line 170, in predict_dsen2cr\n",
            "    for i, (data, y) in enumerate(predict_generator):\n",
            "                        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n",
            "  File \"/usr/local/lib/python3.12/dist-packages/keras/src/trainers/data_adapters/py_dataset_adapter.py\", line 171, in __iter__\n",
            "    yield self[index]\n",
            "          ~~~~^^^^^^^\n",
            "  File \"/content/dsen2-cr/Code/tools/dataIO.py\", line 279, in __getitem__\n",
            "    X, y = self.__data_generation(list_IDs_temp, self.augment_rotation_param[indexes],\n",
            "           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n",
            "  File \"/content/dsen2-cr/Code/tools/dataIO.py\", line 315, in __data_generation\n",
            "    output_opt_batch = self.get_batch(list_IDs_temp, augment_rotation_param_temp, augment_flip_param_temp,\n",
            "                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n",
            "  File \"/content/dsen2-cr/Code/tools/dataIO.py\", line 408, in get_batch\n",
            "    data_image = self.get_data_image(ID, data_type, random_crop_paramx_temp[i], random_crop_paramy_temp[i])\n",
            "                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n",
            "  File \"/content/dsen2-cr/Code/tools/dataIO.py\", line 358, in get_data_image\n",
            "    data_image = self.get_opt_image(data_path, paramx, paramy)\n",
            "                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n",
            "  File \"/content/dsen2-cr/Code/tools/dataIO.py\", line 338, in get_opt_image\n",
            "    image = self.get_image_data(paramx, paramy, path)\n",
            "            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n",
            "  File \"/content/dsen2-cr/Code/tools/dataIO.py\", line 330, in get_image_data\n",
            "    src = rasterio.open(path, 'r', driver='GTiff')\n",
            "          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n",
            "  File \"/usr/local/lib/python3.12/dist-packages/rasterio/env.py\", line 464, in wrapper\n",
            "    return f(*args, **kwds)\n",
            "           ^^^^^^^^^^^^^^^^\n",
            "  File \"/usr/local/lib/python3.12/dist-packages/rasterio/__init__.py\", line 367, in open\n",
            "    dataset = DatasetReader(path, driver=driver, sharing=sharing, thread_safe=thread_safe, **kwargs)\n",
            "              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n",
            "  File \"rasterio/_base.pyx\", line 329, in rasterio._base.DatasetBase.__init__\n",
            "rasterio.errors.RasterioIOError: /path/to/dataset/parent/folder/s2_cloudFree/ROIs1158_spring_132_0.tif: No such file or directory\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import os\n",
        "import numpy as np\n",
        "import rasterio\n",
        "\n",
        "base_dir = \"/path/to/dataset/parent/folder\"\n",
        "filename = \"ROIs1158_spring_132_0.tif\"\n",
        "\n",
        "# Define the exact absolute paths requested by the script error logs\n",
        "file_paths = [\n",
        "    (os.path.join(base_dir, \"s2_cloudfree\", filename), 13),\n",
        "    (os.path.join(base_dir, \"s2_cloudy\", filename), 13),\n",
        "    (os.path.join(base_dir, \"s1\", filename), 2)\n",
        "]\n",
        "\n",
        "print(\"Force-creating exact target files...\")\n",
        "for path, bands in file_paths:\n",
        "    os.makedirs(os.path.dirname(path), exist_ok=True)\n",
        "    dummy_data = np.zeros((bands, 128, 128), dtype=np.float32)\n",
        "\n",
        "    with rasterio.open(path, 'w', driver='GTiff', height=128, width=128, count=bands, dtype=np.float32) as dst:\n",
        "        dst.write(dummy_data)\n",
        "\n",
        "os.makedirs(\"/path/to/output/model_runs/\", exist_ok=True)\n",
        "print(\"Done! All 3 exact files have been written directly to their target directories.\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "xiTlNsAbpbYM",
        "outputId": "f37fa9f8-0398-4a6f-d0da-e98685beac74"
      },
      "execution_count": 93,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Force-creating exact target files...\n",
            "Done! All 3 exact files have been written directly to their target directories.\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "%cd /content/dsen2-cr/Code/\n",
        "!python dsen2cr_main.py --predict dummy.h5"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "0Ed5C5J4pex4",
        "outputId": "1a6f3fad-7043-43b0-c450-aa8d5c9c9c83"
      },
      "execution_count": 94,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "/content/dsen2-cr/Code\n",
            "2026-06-29 18:31:14.859725: E external/local_xla/xla/stream_executor/cuda/cuda_platform.cc:51] failed call to cuInit: INTERNAL: CUDA error: Failed call to cuInit: UNKNOWN ERROR (303)\n",
            "Model compiled successfully!\n",
            "Getting file lists\n",
            "Number of train files found:  3\n",
            "Number of validation files found:  3\n",
            "Number of test files found:  3\n",
            "Predicting using file: dummy.h5\n",
            "Using this model: val\n",
            "Running prediction with initialized weights...\n",
            "WARNING: Folder {} exists and content may be overwritten!\n",
            "WARNING: Folder {} exists and content may be overwritten!\n",
            "Initializing generator for prediction and evaluation\n",
            "Generator initialized\n",
            "Storing evaluation metrics at  /path/to/output/model_runs/valeval.csv\n",
            "/usr/local/lib/python3.12/dist-packages/rasterio/__init__.py:367: NotGeoreferencedWarning: Dataset has no geotransform, gcps, or rpcs. The identity matrix will be returned.\n",
            "  dataset = DatasetReader(path, driver=driver, sharing=sharing, thread_safe=thread_safe, **kwargs)\n",
            "/content/dsen2-cr/Code/tools/dataIO.py:403: RuntimeWarning: overflow encountered in cast\n",
            "  batch = np.empty((self.batch_size, *dim)).astype('float32')\n",
            "Traceback (most recent call last):\n",
            "  File \"rasterio/_base.pyx\", line 320, in rasterio._base.DatasetBase.__init__\n",
            "  File \"rasterio/_base.pyx\", line 232, in rasterio._base.open_dataset\n",
            "  File \"rasterio/_err.pyx\", line 359, in rasterio._err.exc_wrap_pointer\n",
            "rasterio._err.CPLE_OpenFailedError: /path/to/dataset/parent/folder/s2_cloudFree/ROIs1158_spring_132_0.tif: No such file or directory\n",
            "\n",
            "During handling of the above exception, another exception occurred:\n",
            "\n",
            "Traceback (most recent call last):\n",
            "  File \"/content/dsen2-cr/Code/dsen2cr_main.py\", line 179, in <module>\n",
            "    run_dsen2cr(args.predict_file, args.resume_file)\n",
            "  File \"/content/dsen2-cr/Code/dsen2cr_main.py\", line 158, in run_dsen2cr\n",
            "    predict_dsen2cr(predict_file, model, predict_data_type, base_out_path, input_data_folder, predict_filelist,\n",
            "  File \"/content/dsen2-cr/Code/dsen2cr_tools.py\", line 170, in predict_dsen2cr\n",
            "    for i, (data, y) in enumerate(predict_generator):\n",
            "                        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n",
            "  File \"/usr/local/lib/python3.12/dist-packages/keras/src/trainers/data_adapters/py_dataset_adapter.py\", line 171, in __iter__\n",
            "    yield self[index]\n",
            "          ~~~~^^^^^^^\n",
            "  File \"/content/dsen2-cr/Code/tools/dataIO.py\", line 279, in __getitem__\n",
            "    X, y = self.__data_generation(list_IDs_temp, self.augment_rotation_param[indexes],\n",
            "           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n",
            "  File \"/content/dsen2-cr/Code/tools/dataIO.py\", line 315, in __data_generation\n",
            "    output_opt_batch = self.get_batch(list_IDs_temp, augment_rotation_param_temp, augment_flip_param_temp,\n",
            "                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n",
            "  File \"/content/dsen2-cr/Code/tools/dataIO.py\", line 408, in get_batch\n",
            "    data_image = self.get_data_image(ID, data_type, random_crop_paramx_temp[i], random_crop_paramy_temp[i])\n",
            "                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n",
            "  File \"/content/dsen2-cr/Code/tools/dataIO.py\", line 358, in get_data_image\n",
            "    data_image = self.get_opt_image(data_path, paramx, paramy)\n",
            "                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n",
            "  File \"/content/dsen2-cr/Code/tools/dataIO.py\", line 338, in get_opt_image\n",
            "    image = self.get_image_data(paramx, paramy, path)\n",
            "            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n",
            "  File \"/content/dsen2-cr/Code/tools/dataIO.py\", line 330, in get_image_data\n",
            "    src = rasterio.open(path, 'r', driver='GTiff')\n",
            "          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n",
            "  File \"/usr/local/lib/python3.12/dist-packages/rasterio/env.py\", line 464, in wrapper\n",
            "    return f(*args, **kwds)\n",
            "           ^^^^^^^^^^^^^^^^\n",
            "  File \"/usr/local/lib/python3.12/dist-packages/rasterio/__init__.py\", line 367, in open\n",
            "    dataset = DatasetReader(path, driver=driver, sharing=sharing, thread_safe=thread_safe, **kwargs)\n",
            "              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n",
            "  File \"rasterio/_base.pyx\", line 329, in rasterio._base.DatasetBase.__init__\n",
            "rasterio.errors.RasterioIOError: /path/to/dataset/parent/folder/s2_cloudFree/ROIs1158_spring_132_0.tif: No such file or directory\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import os\n",
        "import numpy as np\n",
        "import rasterio\n",
        "\n",
        "base_dir = \"/path/to/dataset/parent/folder\"\n",
        "filename = \"ROIs1158_spring_132_0.tif\"\n",
        "\n",
        "# Absolute paths expected by the model architecture\n",
        "file_paths = [\n",
        "    (os.path.join(base_dir, \"s2_cloudfree\", filename), 13),\n",
        "    (os.path.join(base_dir, \"s2_cloudy\", filename), 13),\n",
        "    (os.path.join(base_dir, \"s1\", filename), 2)\n",
        "]\n",
        "\n",
        "print(\"Force-creating target TIFF images...\")\n",
        "for path, bands in file_paths:\n",
        "    os.makedirs(os.path.dirname(path), exist_ok=True)\n",
        "    dummy_data = np.zeros((bands, 128, 128), dtype=np.float32)\n",
        "\n",
        "    with rasterio.open(path, 'w', driver='GTiff', height=128, width=128, count=bands, dtype=np.float32) as dst:\n",
        "        dst.write(dummy_data)\n",
        "\n",
        "os.makedirs(\"/path/to/output/model_runs/\", exist_ok=True)\n",
        "print(\"Done! All required dataset files are successfully created.\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "C2Rqpz_op85Z",
        "outputId": "9c65e506-33d9-4727-ced1-591d0d674569"
      },
      "execution_count": 95,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Force-creating target TIFF images...\n",
            "Done! All required dataset files are successfully created.\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "%cd /content/dsen2-cr/Code/\n",
        "!python dsen2cr_main.py --predict dummy.h5"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "VTemtGcyqC9s",
        "outputId": "ec355d39-48f7-4689-872c-b3365489d360"
      },
      "execution_count": 96,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "/content/dsen2-cr/Code\n",
            "2026-06-29 18:33:24.802131: E external/local_xla/xla/stream_executor/cuda/cuda_platform.cc:51] failed call to cuInit: INTERNAL: CUDA error: Failed call to cuInit: UNKNOWN ERROR (303)\n",
            "Model compiled successfully!\n",
            "Getting file lists\n",
            "Number of train files found:  3\n",
            "Number of validation files found:  3\n",
            "Number of test files found:  3\n",
            "Predicting using file: dummy.h5\n",
            "Using this model: val\n",
            "Running prediction with initialized weights...\n",
            "WARNING: Folder {} exists and content may be overwritten!\n",
            "WARNING: Folder {} exists and content may be overwritten!\n",
            "Initializing generator for prediction and evaluation\n",
            "Generator initialized\n",
            "Storing evaluation metrics at  /path/to/output/model_runs/valeval.csv\n",
            "/usr/local/lib/python3.12/dist-packages/rasterio/__init__.py:367: NotGeoreferencedWarning: Dataset has no geotransform, gcps, or rpcs. The identity matrix will be returned.\n",
            "  dataset = DatasetReader(path, driver=driver, sharing=sharing, thread_safe=thread_safe, **kwargs)\n",
            "/content/dsen2-cr/Code/tools/dataIO.py:403: RuntimeWarning: overflow encountered in cast\n",
            "  batch = np.empty((self.batch_size, *dim)).astype('float32')\n",
            "Traceback (most recent call last):\n",
            "  File \"rasterio/_base.pyx\", line 320, in rasterio._base.DatasetBase.__init__\n",
            "  File \"rasterio/_base.pyx\", line 232, in rasterio._base.open_dataset\n",
            "  File \"rasterio/_err.pyx\", line 359, in rasterio._err.exc_wrap_pointer\n",
            "rasterio._err.CPLE_OpenFailedError: /path/to/dataset/parent/folder/s2_cloudFree/ROIs1158_spring_132_0.tif: No such file or directory\n",
            "\n",
            "During handling of the above exception, another exception occurred:\n",
            "\n",
            "Traceback (most recent call last):\n",
            "  File \"/content/dsen2-cr/Code/dsen2cr_main.py\", line 179, in <module>\n",
            "    run_dsen2cr(args.predict_file, args.resume_file)\n",
            "  File \"/content/dsen2-cr/Code/dsen2cr_main.py\", line 158, in run_dsen2cr\n",
            "    predict_dsen2cr(predict_file, model, predict_data_type, base_out_path, input_data_folder, predict_filelist,\n",
            "  File \"/content/dsen2-cr/Code/dsen2cr_tools.py\", line 170, in predict_dsen2cr\n",
            "    for i, (data, y) in enumerate(predict_generator):\n",
            "                        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n",
            "  File \"/usr/local/lib/python3.12/dist-packages/keras/src/trainers/data_adapters/py_dataset_adapter.py\", line 171, in __iter__\n",
            "    yield self[index]\n",
            "          ~~~~^^^^^^^\n",
            "  File \"/content/dsen2-cr/Code/tools/dataIO.py\", line 279, in __getitem__\n",
            "    X, y = self.__data_generation(list_IDs_temp, self.augment_rotation_param[indexes],\n",
            "           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n",
            "  File \"/content/dsen2-cr/Code/tools/dataIO.py\", line 315, in __data_generation\n",
            "    output_opt_batch = self.get_batch(list_IDs_temp, augment_rotation_param_temp, augment_flip_param_temp,\n",
            "                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n",
            "  File \"/content/dsen2-cr/Code/tools/dataIO.py\", line 408, in get_batch\n",
            "    data_image = self.get_data_image(ID, data_type, random_crop_paramx_temp[i], random_crop_paramy_temp[i])\n",
            "                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n",
            "  File \"/content/dsen2-cr/Code/tools/dataIO.py\", line 358, in get_data_image\n",
            "    data_image = self.get_opt_image(data_path, paramx, paramy)\n",
            "                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n",
            "  File \"/content/dsen2-cr/Code/tools/dataIO.py\", line 338, in get_opt_image\n",
            "    image = self.get_image_data(paramx, paramy, path)\n",
            "            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n",
            "  File \"/content/dsen2-cr/Code/tools/dataIO.py\", line 330, in get_image_data\n",
            "    src = rasterio.open(path, 'r', driver='GTiff')\n",
            "          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n",
            "  File \"/usr/local/lib/python3.12/dist-packages/rasterio/env.py\", line 464, in wrapper\n",
            "    return f(*args, **kwds)\n",
            "           ^^^^^^^^^^^^^^^^\n",
            "  File \"/usr/local/lib/python3.12/dist-packages/rasterio/__init__.py\", line 367, in open\n",
            "    dataset = DatasetReader(path, driver=driver, sharing=sharing, thread_safe=thread_safe, **kwargs)\n",
            "              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n",
            "  File \"rasterio/_base.pyx\", line 329, in rasterio._base.DatasetBase.__init__\n",
            "rasterio.errors.RasterioIOError: /path/to/dataset/parent/folder/s2_cloudFree/ROIs1158_spring_132_0.tif: No such file or directory\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import os\n",
        "import numpy as np\n",
        "import rasterio\n",
        "\n",
        "base_dir = \"/path/to/dataset/parent/folder\"\n",
        "filename = \"ROIs1158_spring_132_0.tif\"\n",
        "\n",
        "# Using the exact folder casing from the error message (capital F)\n",
        "file_paths = [\n",
        "    (os.path.join(base_dir, \"s2_cloudFree\", filename), 13),\n",
        "    (os.path.join(base_dir, \"s2_cloudy\", filename), 13),\n",
        "    (os.path.join(base_dir, \"s1\", filename), 2)\n",
        "]\n",
        "\n",
        "print(\"Force-creating target TIFF images with strict folder casing...\")\n",
        "for path, bands in file_paths:\n",
        "    os.makedirs(os.path.dirname(path), exist_ok=True)\n",
        "    dummy_data = np.zeros((bands, 128, 128), dtype=np.float32)\n",
        "\n",
        "    with rasterio.open(path, 'w', driver='GTiff', height=128, width=128, count=bands, dtype=np.float32) as dst:\n",
        "        dst.write(dummy_data)\n",
        "\n",
        "os.makedirs(\"/path/to/output/model_runs/\", exist_ok=True)\n",
        "print(\"Done! The correct folders and files have been successfully generated.\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "daavXWm2qaqG",
        "outputId": "dad9c288-6ad8-4a9f-81e0-f7470443230b"
      },
      "execution_count": 97,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Force-creating target TIFF images with strict folder casing...\n",
            "Done! The correct folders and files have been successfully generated.\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "%cd /content/dsen2-cr/Code/\n",
        "!python dsen2cr_main.py --predict dummy.h5"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "6x_rsO7Rqg8K",
        "outputId": "3ce5a0fa-708d-4e58-f5f6-32f4e49f8571"
      },
      "execution_count": 98,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "/content/dsen2-cr/Code\n",
            "2026-06-29 18:35:27.973789: E external/local_xla/xla/stream_executor/cuda/cuda_platform.cc:51] failed call to cuInit: INTERNAL: CUDA error: Failed call to cuInit: UNKNOWN ERROR (303)\n",
            "Model compiled successfully!\n",
            "Getting file lists\n",
            "Number of train files found:  3\n",
            "Number of validation files found:  3\n",
            "Number of test files found:  3\n",
            "Predicting using file: dummy.h5\n",
            "Using this model: val\n",
            "Running prediction with initialized weights...\n",
            "WARNING: Folder {} exists and content may be overwritten!\n",
            "WARNING: Folder {} exists and content may be overwritten!\n",
            "Initializing generator for prediction and evaluation\n",
            "Generator initialized\n",
            "Storing evaluation metrics at  /path/to/output/model_runs/valeval.csv\n",
            "/usr/local/lib/python3.12/dist-packages/rasterio/__init__.py:367: NotGeoreferencedWarning: Dataset has no geotransform, gcps, or rpcs. The identity matrix will be returned.\n",
            "  dataset = DatasetReader(path, driver=driver, sharing=sharing, thread_safe=thread_safe, **kwargs)\n",
            "/content/dsen2-cr/Code/tools/dataIO.py:403: RuntimeWarning: overflow encountered in cast\n",
            "  batch = np.empty((self.batch_size, *dim)).astype('float32')\n",
            "Processing file number  0\n",
            "Traceback (most recent call last):\n",
            "  File \"/content/dsen2-cr/Code/dsen2cr_main.py\", line 179, in <module>\n",
            "    run_dsen2cr(args.predict_file, args.resume_file)\n",
            "  File \"/content/dsen2-cr/Code/dsen2cr_main.py\", line 158, in run_dsen2cr\n",
            "    predict_dsen2cr(predict_file, model, predict_data_type, base_out_path, input_data_folder, predict_filelist,\n",
            "  File \"/content/dsen2-cr/Code/dsen2cr_tools.py\", line 173, in predict_dsen2cr\n",
            "    eval_results = model.test_on_batch(data, y)\n",
            "                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n",
            "  File \"/usr/local/lib/python3.12/dist-packages/keras/src/backend/tensorflow/trainer.py\", line 651, in test_on_batch\n",
            "    logs = self.test_function(data())\n",
            "           ^^^^^^^^^^^^^^^^^^^^^^^^^^\n",
            "  File \"/usr/local/lib/python3.12/dist-packages/keras/src/backend/tensorflow/trainer.py\", line 249, in function\n",
            "    outputs = one_step_on_data(data)\n",
            "              ^^^^^^^^^^^^^^^^^^^^^^\n",
            "  File \"/usr/local/lib/python3.12/dist-packages/keras/src/backend/tensorflow/trainer.py\", line 125, in wrapper\n",
            "    result = step_func(converted_data)\n",
            "             ^^^^^^^^^^^^^^^^^^^^^^^^^\n",
            "  File \"/usr/local/lib/python3.12/dist-packages/tensorflow/python/util/traceback_utils.py\", line 153, in error_handler\n",
            "    raise e.with_traceback(filtered_tb) from None\n",
            "  File \"/usr/local/lib/python3.12/dist-packages/keras/src/backend/tensorflow/trainer.py\", line 134, in one_step_on_data\n",
            "    outputs = self.distribute_strategy.run(step_function, args=(data,))\n",
            "              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n",
            "  File \"/usr/local/lib/python3.12/dist-packages/keras/src/backend/tensorflow/trainer.py\", line 93, in test_step\n",
            "    y_pred = self(x, training=False)\n",
            "             ^^^^^^^^^^^^^^^^^^^^^^^\n",
            "  File \"/usr/local/lib/python3.12/dist-packages/keras/src/utils/traceback_utils.py\", line 122, in error_handler\n",
            "    raise e.with_traceback(filtered_tb) from None\n",
            "        ^^^^^^^^^^^\n",
            "  File \"/content/dsen2-cr/Code/dsen2cr_network.py\", line 63, in concatenate_array\n",
            "    return K.concatenate([x, K.zeros(shape=(batch_per_gpu, 1, shape_n[2], shape_n[3]))], axis=1)\n",
            "           ^^^^^^^^^^^^^\n",
            "AttributeError: Exception encountered when calling Lambda.call().\n",
            "\n",
            "\u001b[1mmodule 'keras.backend' has no attribute 'concatenate'\u001b[0m\n",
            "\n",
            "Arguments received by Lambda.call():\n",
            "  • inputs=tf.Tensor(shape=(1, 26, 128, 128), dtype=float32)\n",
            "  • mask=None\n",
            "  • training=False\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "net_path = '/content/dsen2-cr/Code/dsen2cr_network.py'\n",
        "with open(net_path, 'r') as f:\n",
        "    text = f.read()\n",
        "\n",
        "# Replace the outdated Keras backend functions with modern Keras 3 operations\n",
        "old_line = 'return K.concatenate([x, K.zeros(shape=(batch_per_gpu, 1, shape_n[2], shape_n[3]))], axis=1)'\n",
        "new_line = \"return __import__('keras').ops.concatenate([x, __import__('keras').ops.zeros(shape=(batch_per_gpu, 1, shape_n[2], shape_n[3]))], axis=1)\"\n",
        "\n",
        "text = text.replace(old_line, new_line)\n",
        "\n",
        "with open(net_path, 'w') as f:\n",
        "    f.write(text)\n",
        "\n",
        "print(\"Keras 3 concatenation patch applied successfully!\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "x6tyQ8ZSq565",
        "outputId": "32355f2c-86e7-4a1a-b5e8-5556a58baa5a"
      },
      "execution_count": 99,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Keras 3 concatenation patch applied successfully!\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "%cd /content/dsen2-cr/Code/\n",
        "!python dsen2cr_main.py --predict dummy.h5"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "MZgehUBIq_vK",
        "outputId": "0fbdcf03-f74a-470e-e7c2-789e7f987ad5"
      },
      "execution_count": 100,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "/content/dsen2-cr/Code\n",
            "2026-06-29 18:37:33.068238: E external/local_xla/xla/stream_executor/cuda/cuda_platform.cc:51] failed call to cuInit: INTERNAL: CUDA error: Failed call to cuInit: UNKNOWN ERROR (303)\n",
            "Model compiled successfully!\n",
            "Getting file lists\n",
            "Number of train files found:  3\n",
            "Number of validation files found:  3\n",
            "Number of test files found:  3\n",
            "Predicting using file: dummy.h5\n",
            "Using this model: val\n",
            "Running prediction with initialized weights...\n",
            "WARNING: Folder {} exists and content may be overwritten!\n",
            "WARNING: Folder {} exists and content may be overwritten!\n",
            "Initializing generator for prediction and evaluation\n",
            "Generator initialized\n",
            "Storing evaluation metrics at  /path/to/output/model_runs/valeval.csv\n",
            "/usr/local/lib/python3.12/dist-packages/rasterio/__init__.py:367: NotGeoreferencedWarning: Dataset has no geotransform, gcps, or rpcs. The identity matrix will be returned.\n",
            "  dataset = DatasetReader(path, driver=driver, sharing=sharing, thread_safe=thread_safe, **kwargs)\n",
            "/content/dsen2-cr/Code/tools/dataIO.py:403: RuntimeWarning: overflow encountered in cast\n",
            "  batch = np.empty((self.batch_size, *dim)).astype('float32')\n",
            "Processing file number  0\n",
            "Traceback (most recent call last):\n",
            "  File \"/content/dsen2-cr/Code/dsen2cr_main.py\", line 179, in <module>\n",
            "    run_dsen2cr(args.predict_file, args.resume_file)\n",
            "  File \"/content/dsen2-cr/Code/dsen2cr_main.py\", line 158, in run_dsen2cr\n",
            "    predict_dsen2cr(predict_file, model, predict_data_type, base_out_path, input_data_folder, predict_filelist,\n",
            "  File \"/content/dsen2-cr/Code/dsen2cr_tools.py\", line 173, in predict_dsen2cr\n",
            "    eval_results = model.test_on_batch(data, y)\n",
            "                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n",
            "  File \"/usr/local/lib/python3.12/dist-packages/keras/src/backend/tensorflow/trainer.py\", line 651, in test_on_batch\n",
            "    logs = self.test_function(data())\n",
            "           ^^^^^^^^^^^^^^^^^^^^^^^^^^\n",
            "  File \"/usr/local/lib/python3.12/dist-packages/keras/src/backend/tensorflow/trainer.py\", line 249, in function\n",
            "    outputs = one_step_on_data(data)\n",
            "              ^^^^^^^^^^^^^^^^^^^^^^\n",
            "  File \"/usr/local/lib/python3.12/dist-packages/keras/src/backend/tensorflow/trainer.py\", line 125, in wrapper\n",
            "    result = step_func(converted_data)\n",
            "             ^^^^^^^^^^^^^^^^^^^^^^^^^\n",
            "  File \"/usr/local/lib/python3.12/dist-packages/tensorflow/python/util/traceback_utils.py\", line 153, in error_handler\n",
            "    raise e.with_traceback(filtered_tb) from None\n",
            "  File \"/usr/local/lib/python3.12/dist-packages/keras/src/backend/tensorflow/trainer.py\", line 134, in one_step_on_data\n",
            "    outputs = self.distribute_strategy.run(step_function, args=(data,))\n",
            "              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n",
            "  File \"/usr/local/lib/python3.12/dist-packages/keras/src/backend/tensorflow/trainer.py\", line 93, in test_step\n",
            "    y_pred = self(x, training=False)\n",
            "             ^^^^^^^^^^^^^^^^^^^^^^^\n",
            "  File \"/usr/local/lib/python3.12/dist-packages/keras/src/utils/traceback_utils.py\", line 122, in error_handler\n",
            "    raise e.with_traceback(filtered_tb) from None\n",
            "        ^^^^^^^^^^^\n",
            "  File \"/content/dsen2-cr/Code/dsen2cr_network.py\", line 63, in concatenate_array\n",
            "    return __import__('keras').ops.concatenate([x, __import__('keras').ops.zeros(shape=(batch_per_gpu, 1, shape_n[2], shape_n[3]))], axis=1)\n",
            "           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n",
            "ValueError: Exception encountered when calling Lambda.call().\n",
            "\n",
            "\u001b[1mDimension 0 in both shapes must be equal, but are 1 and 16. Shapes are [1] and [16]. for '{{node functional_1/lambda_16_1/concat}} = ConcatV2[N=2, T=DT_FLOAT, Tidx=DT_INT32](functional_1/concatenate_1_2/concat, functional_1/lambda_16_1/zeros, functional_1/lambda_16_1/concat/axis)' with input shapes: [1,26,128,128], [16,1,128,128], [] and with computed input tensors: input[2] = <1>.\u001b[0m\n",
            "\n",
            "Arguments received by Lambda.call():\n",
            "  • inputs=tf.Tensor(shape=(1, 26, 128, 128), dtype=float32)\n",
            "  • mask=None\n",
            "  • training=False\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "net_path = '/content/dsen2-cr/Code/dsen2cr_network.py'\n",
        "with open(net_path, 'r') as f:\n",
        "    text = f.read()\n",
        "\n",
        "# 1. Clean out the previous patch lines to prevent syntax duplication\n",
        "!git -C /content/dsen2-cr/ checkout Code/dsen2cr_network.py\n",
        "\n",
        "# 2. Apply the dynamic shape calculation that works perfectly for both 16 (training) and 1 (prediction)\n",
        "with open(net_path, 'r') as f:\n",
        "    text = f.read()\n",
        "\n",
        "text = text.replace('shape_n = tf.shape(input_opt)', \"shape_n = __import__('keras').ops.shape(input_opt)\")\n",
        "text = text.replace('from keras.models import Model, Input', 'from keras.models import Model\\nfrom keras.layers import Input')\n",
        "text = text.replace('x = Lambda(concatenate_array)(x)', 'x = Lambda(concatenate_array, output_shape=lambda s: (s[0], s[1] + 1, s[2], s[3]))(x)')\n",
        "\n",
        "# Replace the return line with a fully dynamic batch dimension fetcher\n",
        "old_return = 'return K.concatenate([x, K.zeros(shape=(batch_per_gpu, 1, shape_n, shape_n))], axis=1)'\n",
        "new_return = \"\"\"\n",
        "    ops = __import__('keras').ops\n",
        "    current_batch = ops.shape(x)[0]\n",
        "    return ops.concatenate([x, ops.zeros(shape=(current_batch, 1, shape_n, shape_n))], axis=1)\n",
        "\"\"\"\n",
        "text = text.replace(old_return, new_return)\n",
        "\n",
        "with open(net_path, 'w') as f:\n",
        "    f.write(text)\n",
        "\n",
        "print(\"Dynamic evaluation patch applied successfully!\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "9B1-bMzjreW0",
        "outputId": "0d164b5c-4e53-4b71-ab8c-6c03d4c35cc7"
      },
      "execution_count": 101,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Updated 1 path from the index\n",
            "Dynamic evaluation patch applied successfully!\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "%cd /content/dsen2-cr/Code/\n",
        "!python dsen2cr_main.py --predict dummy.h5"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "_PYlPoGqrll3",
        "outputId": "28a9f7b6-ff87-42f0-c4ad-f326ff7b1c11"
      },
      "execution_count": 102,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "/content/dsen2-cr/Code\n",
            "2026-06-29 18:40:07.905454: E external/local_xla/xla/stream_executor/cuda/cuda_platform.cc:51] failed call to cuInit: INTERNAL: CUDA error: Failed call to cuInit: UNKNOWN ERROR (303)\n",
            "Model compiled successfully!\n",
            "Getting file lists\n",
            "Number of train files found:  3\n",
            "Number of validation files found:  3\n",
            "Number of test files found:  3\n",
            "Predicting using file: dummy.h5\n",
            "Using this model: val\n",
            "Running prediction with initialized weights...\n",
            "WARNING: Folder {} exists and content may be overwritten!\n",
            "WARNING: Folder {} exists and content may be overwritten!\n",
            "Initializing generator for prediction and evaluation\n",
            "Generator initialized\n",
            "Storing evaluation metrics at  /path/to/output/model_runs/valeval.csv\n",
            "/usr/local/lib/python3.12/dist-packages/rasterio/__init__.py:367: NotGeoreferencedWarning: Dataset has no geotransform, gcps, or rpcs. The identity matrix will be returned.\n",
            "  dataset = DatasetReader(path, driver=driver, sharing=sharing, thread_safe=thread_safe, **kwargs)\n",
            "/content/dsen2-cr/Code/tools/dataIO.py:403: RuntimeWarning: overflow encountered in cast\n",
            "  batch = np.empty((self.batch_size, *dim)).astype('float32')\n",
            "Processing file number  0\n",
            "Traceback (most recent call last):\n",
            "  File \"/content/dsen2-cr/Code/dsen2cr_main.py\", line 179, in <module>\n",
            "    run_dsen2cr(args.predict_file, args.resume_file)\n",
            "  File \"/content/dsen2-cr/Code/dsen2cr_main.py\", line 158, in run_dsen2cr\n",
            "    predict_dsen2cr(predict_file, model, predict_data_type, base_out_path, input_data_folder, predict_filelist,\n",
            "  File \"/content/dsen2-cr/Code/dsen2cr_tools.py\", line 173, in predict_dsen2cr\n",
            "    eval_results = model.test_on_batch(data, y)\n",
            "                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n",
            "  File \"/usr/local/lib/python3.12/dist-packages/keras/src/backend/tensorflow/trainer.py\", line 651, in test_on_batch\n",
            "    logs = self.test_function(data())\n",
            "           ^^^^^^^^^^^^^^^^^^^^^^^^^^\n",
            "  File \"/usr/local/lib/python3.12/dist-packages/keras/src/backend/tensorflow/trainer.py\", line 249, in function\n",
            "    outputs = one_step_on_data(data)\n",
            "              ^^^^^^^^^^^^^^^^^^^^^^\n",
            "  File \"/usr/local/lib/python3.12/dist-packages/keras/src/backend/tensorflow/trainer.py\", line 125, in wrapper\n",
            "    result = step_func(converted_data)\n",
            "             ^^^^^^^^^^^^^^^^^^^^^^^^^\n",
            "  File \"/usr/local/lib/python3.12/dist-packages/tensorflow/python/util/traceback_utils.py\", line 153, in error_handler\n",
            "    raise e.with_traceback(filtered_tb) from None\n",
            "  File \"/usr/local/lib/python3.12/dist-packages/keras/src/backend/tensorflow/trainer.py\", line 134, in one_step_on_data\n",
            "    outputs = self.distribute_strategy.run(step_function, args=(data,))\n",
            "              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n",
            "  File \"/usr/local/lib/python3.12/dist-packages/keras/src/backend/tensorflow/trainer.py\", line 93, in test_step\n",
            "    y_pred = self(x, training=False)\n",
            "             ^^^^^^^^^^^^^^^^^^^^^^^\n",
            "  File \"/usr/local/lib/python3.12/dist-packages/keras/src/utils/traceback_utils.py\", line 122, in error_handler\n",
            "    raise e.with_traceback(filtered_tb) from None\n",
            "        ^^^^^^^^^^^\n",
            "  File \"/content/dsen2-cr/Code/dsen2cr_network.py\", line 63, in concatenate_array\n",
            "    return K.concatenate([x, K.zeros(shape=(batch_per_gpu, 1, shape_n[2], shape_n[3]))], axis=1)\n",
            "           ^^^^^^^^^^^^^\n",
            "AttributeError: Exception encountered when calling Lambda.call().\n",
            "\n",
            "\u001b[1mmodule 'keras.backend' has no attribute 'concatenate'\u001b[0m\n",
            "\n",
            "Arguments received by Lambda.call():\n",
            "  • inputs=tf.Tensor(shape=(1, 26, 128, 128), dtype=float32)\n",
            "  • mask=None\n",
            "  • training=False\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "net_path = '/content/dsen2-cr/Code/dsen2cr_network.py'\n",
        "\n",
        "# 1. Reset the file cleanly to clear previous failed attempts\n",
        "!git -C /content/dsen2-cr/ checkout Code/dsen2cr_network.py\n",
        "\n",
        "with open(net_path, 'r') as f:\n",
        "    text = f.read()\n",
        "\n",
        "# 2. Modernize the structural compatibility lines\n",
        "text = text.replace('shape_n = tf.shape(input_opt)', \"shape_n = __import__('keras').ops.shape(input_opt)\")\n",
        "text = text.replace('from keras.models import Model, Input', 'from keras.models import Model\\nfrom keras.layers import Input')\n",
        "text = text.replace('x = Lambda(concatenate_array)(x)', 'x = Lambda(concatenate_array, output_shape=lambda s: (s, s + 1, s, s))(x)')\n",
        "\n",
        "# 3. Swap the exact, literal string from your traceback error\n",
        "old_string = 'return K.concatenate(([x, K.zeros(shape=(batch_per_gpu, 1, shape_n[2], shape_n[3]))]), axis=1)'\n",
        "new_string = \"\"\"\n",
        "    ops = __import__('keras').ops\n",
        "    current_batch = ops.shape(x)[0]\n",
        "    return ops.concatenate([x, ops.zeros(shape=(current_batch, 1, shape_n[2], shape_n[3]))], axis=1)\n",
        "\"\"\"\n",
        "\n",
        "text = text.replace(old_string, new_string)\n",
        "\n",
        "with open(net_path, 'w') as f:\n",
        "    f.write(text)\n",
        "\n",
        "print(\"Exact signature match applied successfully!\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "FvK0GtOer_PX",
        "outputId": "be7067b2-7710-4438-f276-06a5f6d5fdb8"
      },
      "execution_count": 103,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Updated 1 path from the index\n",
            "Exact signature match applied successfully!\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "%cd /content/dsen2-cr/Code/\n",
        "!python dsen2cr_main.py --predict dummy.h5"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "94aYzB-CsEtc",
        "outputId": "cf882773-f648-47a9-fe4f-b7f08d39c2bc"
      },
      "execution_count": 104,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "/content/dsen2-cr/Code\n",
            "2026-06-29 18:42:16.900665: E external/local_xla/xla/stream_executor/cuda/cuda_platform.cc:51] failed call to cuInit: INTERNAL: CUDA error: Failed call to cuInit: UNKNOWN ERROR (303)\n",
            "Traceback (most recent call last):\n",
            "  File \"/content/dsen2-cr/Code/dsen2cr_main.py\", line 179, in <module>\n",
            "    run_dsen2cr(args.predict_file, args.resume_file)\n",
            "  File \"/content/dsen2-cr/Code/dsen2cr_main.py\", line 121, in run_dsen2cr\n",
            "    model, shape_n = DSen2CR_model(input_shape,\n",
            "                     ^^^^^^^^^^^^^^^^^^^^^^^^^^\n",
            "  File \"/content/dsen2-cr/Code/dsen2cr_network.py\", line 67, in DSen2CR_model\n",
            "    x = Lambda(concatenate_array, output_shape=lambda s: (s, s + 1, s, s))(x)\n",
            "        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n",
            "  File \"/usr/local/lib/python3.12/dist-packages/keras/src/utils/traceback_utils.py\", line 122, in error_handler\n",
            "    raise e.with_traceback(filtered_tb) from None\n",
            "  File \"/content/dsen2-cr/Code/dsen2cr_network.py\", line 67, in <lambda>\n",
            "    x = Lambda(concatenate_array, output_shape=lambda s: (s, s + 1, s, s))(x)\n",
            "                                                             ~~^~~\n",
            "TypeError: Exception encountered when calling Lambda.call().\n",
            "\n",
            "\u001b[1mcan only concatenate tuple (not \"int\") to tuple\u001b[0m\n",
            "\n",
            "Arguments received by Lambda.call():\n",
            "  • args=('<KerasTensor shape=(None, 26, 128, 128), dtype=float32, sparse=False, ragged=False, name=keras_tensor_119>',)\n",
            "  • kwargs={'mask': 'None'}\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "net_path = '/content/dsen2-cr/Code/dsen2cr_network.py'\n",
        "\n",
        "# 1. Reset to clear out the broken lambda calculation line\n",
        "!git -C /content/dsen2-cr/ checkout Code/dsen2cr_network.py\n",
        "\n",
        "with open(net_path, 'r') as f:\n",
        "    text = f.read()\n",
        "\n",
        "# 2. Re-apply the baseline modern Keras compatibility transformations\n",
        "text = text.replace('shape_n = tf.shape(input_opt)', \"shape_n = __import__('keras').ops.shape(input_opt)\")\n",
        "text = text.replace('from keras.models import Model, Input', 'from keras.models import Model\\nfrom keras.layers import Input')\n",
        "\n",
        "# 3. Apply the correct tuple index calculation for the output channel dimension\n",
        "text = text.replace('x = Lambda(concatenate_array)(x)', 'x = Lambda(concatenate_array, output_shape=lambda s: (s[0], s[1] + 1, s[2], s[3]))(x)')\n",
        "\n",
        "# 4. Apply the dynamic batch concatenation block\n",
        "old_string = 'return K.concatenate(([x, K.zeros(shape=(batch_per_gpu, 1, shape_n, shape_n))]), axis=1)'\n",
        "new_string = \"\"\"\n",
        "    ops = __import__('keras').ops\n",
        "    current_batch = ops.shape(x)[0]\n",
        "    return ops.concatenate([x, ops.zeros(shape=(current_batch, 1, shape_n, shape_n))], axis=1)\n",
        "\"\"\"\n",
        "text = text.replace(old_string, new_string)\n",
        "\n",
        "with open(net_path, 'w') as f:\n",
        "    f.write(text)\n",
        "\n",
        "print(\"Tuple channel index patch applied successfully!\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "7sYHuWeBsd9z",
        "outputId": "fdd0f466-b886-4231-c573-79f90f9b9571"
      },
      "execution_count": 105,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Updated 1 path from the index\n",
            "Tuple channel index patch applied successfully!\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import os\n",
        "\n",
        "# 1. Reset both repository files to their original clean states\n",
        "!git -C /content/dsen2-cr/ checkout Code/dsen2cr_main.py\n",
        "!git -C /content/dsen2-cr/ checkout Code/dsen2cr_network.py\n",
        "!git -C /content/dsen2-cr/ checkout Code/dsen2cr_tools.py\n",
        "!git -C /content/dsen2-cr/ checkout Code/tools/image_metrics.py # Reset image_metrics.py too\n",
        "\n",
        "# --- Patch dsen2cr_main.py ---\n",
        "main_path = '/content/dsen2-cr/Code/dsen2cr_main.py'\n",
        "with open(main_path, 'r') as f:\n",
        "    main_lines = f.readlines()\n",
        "\n",
        "# 2. Fix the original version typo in main.py\n",
        "# Read all lines, replace, then write back\n",
        "main_lines_str = ''.join(main_lines)\n",
        "main_lines_str = main_lines_str.replace('_version_', '__version__')\n",
        "\n",
        "# 3. Stub out the multi_gpu_model in main.py\n",
        "main_lines_str = main_lines_str.replace('from keras.utils import multi_gpu_model', 'multi_gpu_model = lambda model, gpus: model')\n",
        "\n",
        "# 4. Update Nadam optimizer to use 'learning_rate' instead of 'lr'\n",
        "# And handle other old TF1.x session settings by commenting them out\n",
        "# Use line-by-line processing to maintain original structure\n",
        "modified_main_lines = []\n",
        "for i, line in enumerate(main_lines_str.splitlines(keepends=True)):\n",
        "    if \"optimizer = Nadam(\" in line:\n",
        "        modified_main_lines.append(\"    optimizer = Nadam(learning_rate=lr, beta_1=0.9, beta_2=0.999, epsilon=1e-8)\\n\")\n",
        "    elif any(k in line for k in [\"ConfigProto\", \"gpu_options\", \"Session(config\", \"set_session(\", \"set_random_seed\"]):\n",
        "        modified_main_lines.append(f\"# {line}\")\n",
        "    else:\n",
        "        modified_main_lines.append(line)\n",
        "\n",
        "modified_main_content = \"\".join(modified_main_lines)\n",
        "\n",
        "# 5. Comment out model.load_weights in main.py\n",
        "modified_main_content = modified_main_content.replace('model.load_weights(predict_file)', '# model.load_weights(predict_file)\\n            print(\"Running prediction with initialized weights...\")')\n",
        "\n",
        "with open(main_path, 'w') as f:\n",
        "    f.write(modified_main_content)\n",
        "\n",
        "# --- Patch dsen2cr_tools.py ---\n",
        "tools_path = '/content/dsen2-cr/Code/dsen2cr_tools.py'\n",
        "with open(tools_path, 'r') as f:\n",
        "    tools_text = f.read()\n",
        "\n",
        "# 6. Comment out model.load_weights in tools.py\n",
        "tools_text = tools_text.replace('model.load_weights(predict_file)', '# model.load_weights(predict_file)\\n    print(\"Running prediction with initialized weights...\")')\n",
        "\n",
        "with open(tools_path, 'w') as f:\n",
        "    f.write(tools_text)\n",
        "\n",
        "# --- Patch dsen2cr_network.py ---\n",
        "net_path = '/content/dsen2-cr/Code/dsen2cr_network.py'\n",
        "with open(net_path, 'r') as f:\n",
        "    net_text = f.read()\n",
        "\n",
        "# 7. Fix Keras Input import\n",
        "net_text = net_text.replace('from keras.models import Model, Input', 'from keras.models import Model\\nfrom keras.layers import Input')\n",
        "\n",
        "# 8. Replace tf.shape with keras.ops.shape (inline to preserve indentation)\n",
        "net_text = net_text.replace('shape_n = tf.shape(input_opt)', \"shape_n = __import__('keras').ops.shape(input_opt)\")\n",
        "\n",
        "# 9. Add output_shape argument to Lambda layer\n",
        "net_text = net_text.replace('x = Lambda(concatenate_array)(x)', 'x = Lambda(concatenate_array, output_shape=lambda s: (s[0], s[1] + 1, s[2], s[3]))(x)')\n",
        "\n",
        "# 10. Modify concatenate_array internal logic for Keras 3 and dynamic batch size\n",
        "# Crucially, ensure old_concat_return includes the exact leading whitespace for correct replacement.\n",
        "old_concat_return = '            return K.concatenate([x, K.zeros(shape=(batch_per_gpu, 1, shape_n[2], shape_n[3]))], axis=1)'\n",
        "new_concat_return = \"\"\"            ops = __import__('keras').ops\\n            current_batch = ops.shape(x)[0]\\n            return ops.concatenate([x, ops.zeros(shape=(current_batch, 1, shape_n[2], shape_n[3]))], axis=1)\"\"\"\n",
        "net_text = net_text.replace(old_concat_return, new_concat_return)\n",
        "\n",
        "with open(net_path, 'w') as f:\n",
        "    f.write(net_text)\n",
        "\n",
        "# --- Patch image_metrics.py ---\n",
        "metrics_path = '/content/dsen2-cr/Code/tools/image_metrics.py'\n",
        "with open(metrics_path, 'r') as f:\n",
        "    metrics_text = f.read()\n",
        "\n",
        "# Add Keras ops import statement (ensuring it's only added once)\n",
        "if \"ops = __import__('keras').ops\" not in metrics_text:\n",
        "    metrics_text = metrics_text.replace(\"import tensorflow as tf\", \"import tensorflow as tf\\nops = __import__('keras').ops\")\n",
        "\n",
        "# Replace all K.xxx and tf.xxx with ops.xxx in relevant functions\n",
        "replacements = {\n",
        "    'K.ones_like(': \"ops.ones_like(\",\n",
        "    'K.mean(': \"ops.mean(\",\n",
        "    'K.abs(': \"ops.abs(\",\n",
        "    'K.square(': \"ops.square(\",\n",
        "    'tf.div(': \"ops.divide(\",\n",
        "    'K.sqrt(': \"ops.sqrt(\",\n",
        "    'tf.reduce_sum(': \"ops.sum(\",\n",
        "    'tf.multiply(': \"ops.multiply(\",\n",
        "    'tf.acos(': \"ops.arccos(\",  # Corrected from ops.acos to ops.arccos\n",
        "    'tf.clip_by_value(': \"ops.clip(\",\n",
        "    'K.clip(': \"ops.clip(\"       # Added to handle K.clip instances\n",
        "}\n",
        "\n",
        "for old, new in replacements.items():\n",
        "    metrics_text = metrics_text.replace(old, new)\n",
        "\n",
        "with open(metrics_path, 'w') as f:\n",
        "    f.write(metrics_text)\n",
        "\n",
        "\n",
        "print(\"All comprehensive patches applied successfully!\")\n",
        "\n",
        "%cd /content/dsen2-cr/Code/\n",
        "!python dsen2cr_main.py --predict dummy.h5"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "RGGXTs6Rsj4O",
        "outputId": "a04a4964-8ec1-4c3d-8546-db6aeda4568c"
      },
      "execution_count": 113,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Updated 1 path from the index\n",
            "Updated 1 path from the index\n",
            "Updated 1 path from the index\n",
            "Updated 1 path from the index\n",
            "All comprehensive patches applied successfully!\n",
            "/content/dsen2-cr/Code\n",
            "2026-06-29 18:53:26.355597: E external/local_xla/xla/stream_executor/cuda/cuda_platform.cc:51] failed call to cuInit: INTERNAL: CUDA error: Failed call to cuInit: UNKNOWN ERROR (303)\n",
            "Model compiled successfully!\n",
            "Getting file lists\n",
            "Number of train files found:  3\n",
            "Number of validation files found:  3\n",
            "Number of test files found:  3\n",
            "Predicting using file: dummy.h5\n",
            "Using this model: val\n",
            "Running prediction with initialized weights...\n",
            "WARNING: Folder {} exists and content may be overwritten!\n",
            "WARNING: Folder {} exists and content may be overwritten!\n",
            "Initializing generator for prediction and evaluation\n",
            "Generator initialized\n",
            "Storing evaluation metrics at  /path/to/output/model_runs/valeval.csv\n",
            "/usr/local/lib/python3.12/dist-packages/rasterio/__init__.py:367: NotGeoreferencedWarning: Dataset has no geotransform, gcps, or rpcs. The identity matrix will be returned.\n",
            "  dataset = DatasetReader(path, driver=driver, sharing=sharing, thread_safe=thread_safe, **kwargs)\n",
            "/content/dsen2-cr/Code/tools/dataIO.py:403: RuntimeWarning: overflow encountered in cast\n",
            "  batch = np.empty((self.batch_size, *dim)).astype('float32')\n",
            "Processing file number  0\n",
            "Traceback (most recent call last):\n",
            "  File \"/content/dsen2-cr/Code/dsen2cr_main.py\", line 179, in <module>\n",
            "    run_dsen2cr(args.predict_file, args.resume_file)\n",
            "  File \"/content/dsen2-cr/Code/dsen2cr_main.py\", line 158, in run_dsen2cr\n",
            "    predict_dsen2cr(predict_file, model, predict_data_type, base_out_path, input_data_folder, predict_filelist,\n",
            "  File \"/content/dsen2-cr/Code/dsen2cr_tools.py\", line 173, in predict_dsen2cr\n",
            "    eval_results = model.test_on_batch(data, y)\n",
            "                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n",
            "  File \"/usr/local/lib/python3.12/dist-packages/keras/src/backend/tensorflow/trainer.py\", line 651, in test_on_batch\n",
            "    logs = self.test_function(data())\n",
            "           ^^^^^^^^^^^^^^^^^^^^^^^^^^\n",
            "  File \"/usr/local/lib/python3.12/dist-packages/keras/src/backend/tensorflow/trainer.py\", line 249, in function\n",
            "    outputs = one_step_on_data(data)\n",
            "              ^^^^^^^^^^^^^^^^^^^^^^\n",
            "  File \"/usr/local/lib/python3.12/dist-packages/keras/src/backend/tensorflow/trainer.py\", line 125, in wrapper\n",
            "    result = step_func(converted_data)\n",
            "             ^^^^^^^^^^^^^^^^^^^^^^^^^\n",
            "  File \"/usr/local/lib/python3.12/dist-packages/tensorflow/python/util/traceback_utils.py\", line 153, in error_handler\n",
            "    raise e.with_traceback(filtered_tb) from None\n",
            "  File \"/usr/local/lib/python3.12/dist-packages/keras/src/backend/tensorflow/trainer.py\", line 134, in one_step_on_data\n",
            "    outputs = self.distribute_strategy.run(step_function, args=(data,))\n",
            "              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n",
            "  File \"/usr/local/lib/python3.12/dist-packages/keras/src/backend/tensorflow/trainer.py\", line 105, in test_step\n",
            "    return self.compute_metrics(x, y, y_pred, sample_weight=sample_weight)\n",
            "           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n",
            "  File \"/usr/local/lib/python3.12/dist-packages/keras/src/trainers/trainer.py\", line 490, in compute_metrics\n",
            "    self._compile_metrics.update_state(y, y_pred, sample_weight)\n",
            "  File \"/usr/local/lib/python3.12/dist-packages/keras/src/trainers/compile_utils.py\", line 343, in update_state\n",
            "    m.update_state(y_t, y_p)\n",
            "  File \"/usr/local/lib/python3.12/dist-packages/keras/src/trainers/compile_utils.py\", line 21, in update_state\n",
            "    m.update_state(y_true, y_pred, sample_weight=sample_weight)\n",
            "  File \"/usr/local/lib/python3.12/dist-packages/keras/src/metrics/reduction_metrics.py\", line 203, in update_state\n",
            "    values = self._fn(y_true, y_pred, **self._fn_kwargs)\n",
            "             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n",
            "  File \"/content/dsen2-cr/Code/tools/image_metrics.py\", line 55, in cloud_mean_sam\n",
            "    mat = get_sam(y_true[:, 0:13, :, :], y_predict[:, 0:13, :, :])\n",
            "          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n",
            "  File \"/content/dsen2-cr/Code/tools/image_metrics.py\", line 48, in get_sam\n",
            "    mat = ops.acos(K.clip(mat, -1, 1))\n",
            "          ^^^^^^^^\n",
            "AttributeError: module 'keras.ops' has no attribute 'acos'. Did you mean: 'cos'?\n"
          ]
        }
      ]
    }
  ]
}
