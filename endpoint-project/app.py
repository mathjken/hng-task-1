from flask import Flask, request, jsonify
import datetime

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def get_info():
    slack_name = request.args.get('slack_name', 'Johnkennedy')
    track = request.args.get('track', 'backend')
    current_day = datetime.datetime.now().strftime('%A')
    utc_time = datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')

    response_data = {
        "slack_name": "Johnkennedy",
        "current_day": current_day,
        "utc_time": utc_time,
        "track": "backend",
        "github_file_url": "https://github.com/mathjken/hng-task-1/blob/main/endpoint-project/app.py",
        "github_repo_url": "https://github.com/mathjken/hng-task-1",
        "status_code": 200
    }

    return jsonify(response_data)

if __name__ == '__main__':
    app.run(debug=True)

