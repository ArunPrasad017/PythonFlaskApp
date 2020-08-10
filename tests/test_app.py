from unittest.mock import patch
from flask_project.routes import index


def test_index():
    with patch("flask_project.routes.render_template") as mock_render_template:
        result = index()
        print(result)
        mock_render_template.assert_called()
