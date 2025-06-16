const PORT = 8000;

const express = require('express');
const cors = require('cors');
const path = require('path');
const spawn = require('child_process').spawn;

const app = express();
app.use(express.json());
app.use(cors());

app.get('/', (request, response) => {
  response.send('Hello Node, This is Root Page!!');
});

app.post('/chat', (req, res) => {
  try {
    const sendedQuestion = req.body.question;
    // console.log(sendedQuestion);

    const scriptPath = path.join(__dirname, 'chat.py');

    const result = spawn('python', [scriptPath, sendedQuestion]);
    let responseData = '';

    result.stdout.on('data', function (data) {
      responseData += data.toString();
    });

    result.stderr.on('data', function (data) {
      console.error(data.toString());
    });

    result.on('close', (code) => {
      if (code === 0) {
        res.status(200).json({ answer: responseData });
      } else {
        res
          .status(500)
          .json({ error: 'Child process exited with code ' + code });
      }
    });
  } catch (error) {
    return res.status(500).json({ error: error.message });
  }
});

// const process = spawn('python', ['chat.py']);

// process.stdout.on('data', function (data) {
//   console.log(data.toString());
// }); // 실행 결과

// process.stderr.on('data', function (data) {
//   console.error(data.toString());
// }); // 실행 에러

app.listen(PORT, () => console.log(`Server is running on port ${PORT}`));