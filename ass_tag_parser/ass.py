import parsimonious
import ass_tag_parser.common


GRAMMAR_TEXT = (ass_tag_parser.common.DATA_DIR / 'ass_bnf.txt').read_text()
GRAMMAR = parsimonious.Grammar(GRAMMAR_TEXT)


class NodeVisitor(parsimonious.NodeVisitor):
    def generic_visit(self, node, visited_nodes):
        return visited_nodes

    def visit_ass_line(self, node, visited_nodes):
        return ass_tag_parser.common.flatten(visited_nodes)

    def visit_plain_text(self, node, visited_nodes):
        return {'type': 'plain-text', 'text': node.text}

    def visit_ass_chunk(self, node, visited_nodes):
        return visited_nodes[1]

    def visit_ass_comment(self, node, visited_nodes):
        return {'type': 'comment', 'text': node.children[1].text}

    def visit_ass_tag(self, node, visited_nodes):
        return visited_nodes[1]

    def visit_boolean(self, node, visited_nodes):
        return bool(int(node.text))

    def visit_integer(self, node, _visited_nodes):
        return int(node.text)

    def visit_integer_positive(self, node, _visited_nodes):
        return int(node.text)

    def visit_float(self, node, _visited_nodes):
        return float(node.text)

    def visit_float_positive(self, node, _visited_nodes):
        return float(node.text)

    def visit_byte_value_int(self, node, visited_nodes):
        return int(node.text)

    def visit_byte_value_hex(self, node, visited_nodes):
        return int(node.text, 16)

    def visit_color_value(self, node, visited_nodes):
        return (visited_nodes[1], visited_nodes[2], visited_nodes[3])

    def visit_alpha_value(self, node, visited_nodes):
        return visited_nodes[1]

    def visit_ass_text(self, node, _visited_nodes):
        return node.text

    def visit_ass_tag_italics(self, node, visited_nodes):
        return {'type': 'italics', 'enabled': visited_nodes[1]}

    def visit_ass_tag_bold(self, node, visited_nodes):
        if isinstance(visited_nodes[1][0], bool):
            return {'type': 'bold', 'enabled': visited_nodes[1][0]}
        return {'type': 'bold', 'weight': visited_nodes[1][0]}

    def visit_ass_tag_underline(self, node, visited_nodes):
        return {'type': 'underline', 'enabled': visited_nodes[1]}

    def visit_ass_tag_strikeout(self, node, visited_nodes):
        return {'type': 'strikeout', 'enabled': visited_nodes[1]}

    def visit_ass_tag_border(self, node, visited_nodes):
        return {'type': 'border', 'size': visited_nodes[1]}

    def visit_ass_tag_border_x(self, node, visited_nodes):
        return {'type': 'border-x', 'size': visited_nodes[1]}

    def visit_ass_tag_border_y(self, node, visited_nodes):
        return {'type': 'border-y', 'size': visited_nodes[1]}

    def visit_ass_tag_shadow(self, node, visited_nodes):
        return {'type': 'shadow', 'size': visited_nodes[1]}

    def visit_ass_tag_shadow_x(self, node, visited_nodes):
        return {'type': 'shadow-x', 'size': visited_nodes[1]}

    def visit_ass_tag_shadow_y(self, node, visited_nodes):
        return {'type': 'shadow-y', 'size': visited_nodes[1]}

    def visit_ass_tag_blur_edges(self, node, visited_nodes):
        return {'type': 'blur-edges', 'value': visited_nodes[1]}

    def visit_ass_tag_blur_edges_gauss(self, node, visited_nodes):
        return {'type': 'blur-edges-gauss', 'value': visited_nodes[1]}

    def visit_ass_tag_font_name(self, node, visited_nodes):
        return {'type': 'font-name', 'name': visited_nodes[0][1]}

    def visit_ass_tag_font_encoding(self, node, visited_nodes):
        return {'type': 'font-encoding', 'encoding': visited_nodes[1]}

    def visit_ass_tag_font_size(self, node, visited_nodes):
        return {'type': 'font-size', 'size': visited_nodes[1]}

    def visit_ass_tag_font_scale_x(self, node, visited_nodes):
        return {'type': 'font-scale-x', 'scale': visited_nodes[1]}

    def visit_ass_tag_font_scale_y(self, node, visited_nodes):
        return {'type': 'font-scale-y', 'scale': visited_nodes[1]}

    def visit_ass_tag_letter_spacing(self, node, visited_nodes):
        return {'type': 'letter-spacing', 'value': visited_nodes[1]}

    def visit_ass_tag_rotation_x(self, node, visited_nodes):
        return {'type': 'rotation-x', 'angle': visited_nodes[1]}

    def visit_ass_tag_rotation_y(self, node, visited_nodes):
        return {'type': 'rotation-y', 'angle': visited_nodes[1]}

    def visit_ass_tag_rotation_z(self, node, visited_nodes):
        return {'type': 'rotation-z', 'angle': visited_nodes[0][1]}

    def visit_ass_tag_rotation_origin(self, node, visited_nodes):
        return {
            'type': 'rotation-origin',
            'x': visited_nodes[1],
            'y': visited_nodes[3],
        }

    def visit_ass_tag_shear_x(self, node, visited_nodes):
        return {'type': 'shear-x', 'value': visited_nodes[1]}

    def visit_ass_tag_shear_y(self, node, visited_nodes):
        return {'type': 'shear-y', 'value': visited_nodes[1]}

    def visit_ass_tag_color_primary(self, node, visited_nodes):
        return {
            'type': 'color-primary',
            'red': visited_nodes[1][2],
            'green': visited_nodes[1][1],
            'blue': visited_nodes[1][0],
        }

    def visit_ass_tag_color_secondary(self, node, visited_nodes):
        return {
            'type': 'color-secondary',
            'red': visited_nodes[1][2],
            'green': visited_nodes[1][1],
            'blue': visited_nodes[1][0],
        }

    def visit_ass_tag_color_border(self, node, visited_nodes):
        return {
            'type': 'color-border',
            'red': visited_nodes[1][2],
            'green': visited_nodes[1][1],
            'blue': visited_nodes[1][0],
        }

    def visit_ass_tag_color_shadow(self, node, visited_nodes):
        return {
            'type': 'color-shadow',
            'red': visited_nodes[1][2],
            'green': visited_nodes[1][1],
            'blue': visited_nodes[1][0],
        }

    def visit_ass_tag_alpha_all(self, node, visited_nodes):
        return {'type': 'alpha-all', 'value': visited_nodes[1]}

    def visit_ass_tag_alpha_primary(self, node, visited_nodes):
        return {'type': 'alpha-primary', 'value': visited_nodes[1]}

    def visit_ass_tag_alpha_secondary(self, node, visited_nodes):
        return {'type': 'alpha-secondary', 'value': visited_nodes[1]}

    def visit_ass_tag_alpha_border(self, node, visited_nodes):
        return {'type': 'alpha-border', 'value': visited_nodes[1]}

    def visit_ass_tag_alpha_shadow(self, node, visited_nodes):
        return {'type': 'alpha-shadow', 'value': visited_nodes[1]}

    def visit_ass_tag_karaoke_1(self, node, visited_nodes):
        return {'type': 'karaoke-1', 'duration': visited_nodes[1] * 10}

    def visit_ass_tag_karaoke_2(self, node, visited_nodes):
        return {'type': 'karaoke-2', 'duration': visited_nodes[1] * 10}

    def visit_ass_tag_karaoke_3(self, node, visited_nodes):
        return {'type': 'karaoke-3', 'duration': visited_nodes[1] * 10}

    def visit_ass_tag_karaoke_4(self, node, visited_nodes):
        return {'type': 'karaoke-4', 'duration': visited_nodes[1] * 10}

    def visit_ass_tag_alignment(self, node, visited_nodes):
        return {
            'type': 'alignment',
            'alignment': int(node.children[1].text),
            'legacy': False,
        }

    def visit_ass_tag_alignment_legacy(self, node, visited_nodes):
        value = int(node.children[1].text)
        if value >= 9:
            value -= 2
        elif value >= 5:
            value -= 1
        return {'type': 'alignment', 'alignment': value, 'legacy': True}

    def visit_ass_tag_wrap_style(self, node, visited_nodes):
        return {'type': 'wrap-style', 'value': int(node.children[1].text)}

    def visit_ass_tag_reset_style(self, node, visited_nodes):
        return {
            'type': 'reset-style',
            'style': visited_nodes[1][0] if visited_nodes[1] else None,
        }

    def visit_ass_tag_position(self, node, visited_nodes):
        return {
            'type': 'position',
            'x': visited_nodes[1],
            'y': visited_nodes[3],
        }

    def visit_ass_tag_movement(self, node, visited_nodes):
        return {
            'type': 'movement',
            'x1': visited_nodes[1],
            'y1': visited_nodes[3],
            'x2': visited_nodes[5],
            'y2': visited_nodes[7],
            'start': visited_nodes[8][0][1] if visited_nodes[8] else None,
            'end': visited_nodes[8][0][3] if visited_nodes[8] else None,
        }

    def visit_ass_tag_fade_simple(self, node, visited_nodes):
        return {
            'type': 'fade-simple',
            'start': visited_nodes[1],
            'end': visited_nodes[3],
        }

    def visit_ass_tag_fade_complex(self, node, visited_nodes):
        return {
            'type': 'fade-complex',
            'alpha1': visited_nodes[1],
            'alpha2': visited_nodes[3],
            'alpha3': visited_nodes[5],
            'time1': visited_nodes[7],
            'time2': visited_nodes[9],
            'time3': visited_nodes[11],
            'time4': visited_nodes[13],
        }

    def visit_ass_tag_animation(self, node, visited_nodes):
        return {
            'type': 'animation',
            'start': visited_nodes[1][0][0] if visited_nodes[1] else None,
            'end': visited_nodes[1][0][2] if visited_nodes[1] else None,
            'accel': visited_nodes[2][0][0] if visited_nodes[2] else None,
            'tags': ass_tag_parser.common.flatten(visited_nodes[3]),
        }

    def visit_ass_tag_clip_rectangle(self, node, visited_nodes):
        return {
            'type': 'clip-rectangle',
            'x1': visited_nodes[2],
            'y1': visited_nodes[4],
            'x2': visited_nodes[6],
            'y2': visited_nodes[8],
            'inverse': node.children[0].text.startswith('i'),
        }

    def visit_ass_tag_clip_vector(self, node, visited_nodes):
        return {
            'type': 'clip-vector',
            'scale': visited_nodes[2][0][0] if visited_nodes[2] else None,
            'inverse': node.children[0].text.startswith('i'),
            'commands': visited_nodes[3],
        }

    def visit_ass_tag_drawing_mode(self, node, visited_nodes):
        return {'type': 'drawing-mode', 'value': visited_nodes[1]}

    def visit_ass_tag_baseline_offset(self, node, visited_nodes):
        return {'type': 'baseline-offset', 'value': visited_nodes[1]}


def parse_ass(text):
    try:
        node = GRAMMAR.parse(text)
        return NodeVisitor().visit(node)
    except parsimonious.exceptions.ParseError as ex:
        raise ass_tag_parser.common.ParsingError(ex)