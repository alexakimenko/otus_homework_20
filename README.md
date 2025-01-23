# Local development

Start ML inference server
```commandline
sh run.sh
```

Test ml inference API
```commandline
curl -X POST \
  -H "Content-Type: application/json" \
  -d '{"features":[1.2,3.4,5.6]}' \
  http://127.0.0.1:80/predict
```