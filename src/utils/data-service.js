import axios from 'axios'

let DataService = {
    // 指明了后端服务器的地址, 以便访问数据
    dataServerUrl: 'http://127.0.0.1:5000',

    // 下面定义了一些 HTTP 访问请求, 这些访问请求用来访问后端服务器(dataServerUrl)
    // 后端服务器在 main.py 中定义好了对前端不同访问请求的不同处理方式 — 形成前端和后端的交互

    getFileContent(formData, callback) {
        axios.post(`${this.dataServerUrl}/uploadfile`, formData, {
            headers: {
                "Content-Type": "multipart/form-data",
            }
        })
            .then(function (response) {
                callback(response.data)
            })
            .catch(error => {
                console.error('Error fetching file:', error);
            });

    },

    getWordCloudData(node, noteContext, callback) {
        axios.post(`${this.dataServerUrl}/get-wordclouddata`, {
            nodeId: node.id(),
            noteContext: noteContext
        }, {
            headers: {
                'Content-Type': 'application/json'
            }
        })
            .then(function (response) {
                callback(response.data);
            })
            .catch(error => {
                console.error('Error getting note context:', error);
            });
    },

    getCustomizedNote(callback) {
        // TODO: query backend for customized note.

        // Below load a demo markdown file from assets and handle the document to the renderer.
        fetch('src/assets/MarkdownDemo.md')
            .then(response => {
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                return response.text();
            })
            .then(text => {
                callback(text);
            })
            .catch(error => {
                console.error('There has been a problem with your fetch operation:', error);
            });
    }
}



export default DataService;