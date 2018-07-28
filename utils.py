class Surfmappers:
  host = "http://test.surfmappers.com:6555/"

  login = "teste@teste.com"
  password = "123456"

  def route(self, url):
    return "{}{}".format(self.host, url)

# Default Curl
# curl -sSL -D - "http://test.surfmappers.com:6555/users/me" \
#   -X GET \
#   -H "accept: application/json" \
#   -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyTmFtZSI6InRlc3RlQHRlc3RlLmNvbSIsImlhdCI6MTUzMjc1MDAwOH0.9Vg3D_RsQXIt3TBGf2Ipd0Azx-Bdt8UijaauZLBiJuc"